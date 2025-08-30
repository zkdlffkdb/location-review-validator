#!/usr/bin/env python3

import argparse
import os
import requests

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
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        return "Error: OPENROUTER_API_KEY not found in .env file"
    
    # Load few-shot prompt
    system_prompt = load_few_shot_prompt()
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Build messages with system prompt and user question
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
    
    payload = {
        "model": "openai/gpt-5-mini",
        "messages": messages,
        "max_tokens": 8192, # enough for label + reasoning
        "temperature": 0
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
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
                return label
        
        # Fallback if nothing matches
        return "Irrelevant content"
        
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
