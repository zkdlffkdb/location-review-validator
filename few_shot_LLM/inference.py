#!/usr/bin/env python3

import argparse
import os
import requests
import json

def load_env():
    """Load environment variables from .env file."""
    env_path = '.env'
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and '=' in line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key] = value

def load_few_shot_prompt():
    """Load few-shot content from few_shot.md file as system prompt."""
    few_shot_path = 'few_shot_materials/few_shot.md'
    if not os.path.exists(few_shot_path):
        return "You are a data analysis assistant."
    
    with open(few_shot_path, 'r') as f:
        content = f.read().strip()
    
    return content if content else "You are a data analysis assistant."

def answer_question(question):
    """Answer questions using OpenRouter API with gpt-5-nano and few-shot examples."""
    load_env()
    
    hf_token = os.getenv('HF_TOKEN')  # Hugging Face API token
    if not hf_token:
        return "Error: HF_TOKEN not found in .env file"
        
    # Load few-shot prompt
    system_prompt = load_few_shot_prompt()
    
    API_URL = "https://router.huggingface.co/v1/chat/completions"
    
    headers = {
            "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    }
    
    # Build messages with system prompt and user question
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
    
    payload = {
        "model": "Qwen/Qwen3-Coder-30B-A3B-Instruct:fireworks-ai",  # Use the Qwen model
        "messages": messages,
        "max_tokens": 150, # enough for label + reasoning
        "temperature": 0
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        data = response.json()
        message = data['choices'][0]['message']
        
        answer = message.get('content', '').strip()
        
        valid_labels = {
            "Relevant",
            "Relevant and quality",
            "Irrelevant content",
            "Rants without visit",
            "Advertisement",
            "Vague"
        }
        
        # Force output to be exactly one valid label
        for label in valid_labels:
            if label.lower() in answer.lower():
                result = {"label": label}
                break
        else:
            # Fallback if nothing matches
            result = {"label": "Irrelevant content"}
        
        # Save the result to a JSON file
        with open("result.json", "w") as json_file:
            json.dump(result, json_file, indent=4)  # Write the result to a JSON file with indentation
        
        return result['label']
        
    except requests.exceptions.RequestException as e:
        return f"Error making API request: {e}"
    except KeyError as e:
        return f"Error parsing API response: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    parser = argparse.ArgumentParser(description="A simple question answering CLI tool")
    parser.add_argument('question', help='The question to answer')
    
    args = parser.parse_args()
    
    answer = answer_question(args.question)
    print(answer)

if __name__ == "__main__":
    main()
