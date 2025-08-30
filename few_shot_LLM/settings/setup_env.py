import base64
import os

def decode_base64_to_env(encoded_file_path, env_file_path):
    # Read the encoded key from the file
    with open(encoded_file_path, 'r') as f:
        encoded_key = f.read().strip()

    # Decode the key from base64
    decoded_key = base64.b64decode(encoded_key).decode()

    # Write the decoded key to the .env file in the format OPENROUTER_API_KEY==<decoded_key>
    with open(env_file_path, 'w') as f:
        f.write(f"{decoded_key}\n")

def main():
    # Get the absolute path of the current script directory (settings)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Specify the path to the file with the encoded key (relative to script directory)
    encoded_file_path = os.path.join(script_dir, 'apikey.enc')
    
    # Specify the path to save the .env file (relative to script directory, but in parent folder)
    env_file_path = os.path.join(script_dir, '..', '.env')

    # Ensure the .env file is written in the correct location
    decode_base64_to_env(encoded_file_path, env_file_path)

if __name__ == "__main__":
    main()
