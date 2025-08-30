import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from flask import Flask, request, jsonify
import pandas as pd
import torch.nn as nn
import numpy as np
import os
from safetensors.torch import load_file

# Define the CustomClassifier class exactly as in your training script
class CustomClassifier(nn.Module):
    def __init__(self, text_model_name, num_labels, num_additional_features):
        super(CustomClassifier, self).__init__()

        # Use from_pretrained to load the text model, which will correctly find
        # either pytorch_model.bin or model.safetensors
        self.text_model = AutoModelForSequenceClassification.from_pretrained(
            text_model_name,
            num_labels=num_labels
        )
        self.additional_features_fc = nn.Linear(num_additional_features, 64)
        self.final_classifier = nn.Linear(768 + 64, num_labels)

    def forward(self, input_ids, attention_mask, numerical_features, labels=None):
        text_outputs = self.text_model.distilbert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        cls_hidden_state = text_outputs[0][:, 0, :]
        numerical_output = self.additional_features_fc(numerical_features.view(-1, numerical_features.shape[1]))
        combined_output = torch.cat((cls_hidden_state, numerical_output), dim=1)
        logits = self.final_classifier(combined_output)

        if labels is not None:
            loss_fct = nn.CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.text_model.config.num_labels), labels.view(-1))
            return (loss, logits)
        return (logits,)

# Initialize Flask app
app = Flask(__name__)

# Define the label map
LABEL_MAP = {
    0: 'Relevant and quality',
    1: 'Relevant',
    2: 'no review',
    3: 'Rants without visit',
    4: 'Irrelevant content',
    5: 'Vague',
    6: 'Advertisement'
}

# The full list of one-hot encoded numerical features used in training.
TRAINING_COLUMNS = [
    'rating_person',
    'sentiment_polarity',
    'sentiment_subjectivity',
    'main_category_American restaurant',
    'main_category_Asian fusion restaurant',
    'main_category_Baby store',
    'main_category_Baking supply store',
    'main_category_Balloon store',
    'main_category_Barbecue restaurant',
    'main_category_Bicycle Shop',
    'main_category_Book store',
    'main_category_Buffet restaurant',
    'main_category_Cafe',
    'main_category_Cantonese restaurant',
    'main_category_Car dealer',
    'main_category_Cell phone store',
    'main_category_Chinese restaurant',
    'main_category_Clothing store',
    'main_category_Coffee roasters',
    'main_category_Collectibles store',
    'main_category_Department store',
    'main_category_Designer Clothing Shop',
    'main_category_E-commerce service',
    'main_category_Fashion accessories store',
    'main_category_Fine dining restaurant',
    'main_category_French restaurant',
    'main_category_Furniture store',
    'main_category_Fusion restaurant',
    'main_category_Gift shop',
    'main_category_Greek restaurant',
    'main_category_Halal restaurant',
    'main_category_Hardware store',
    'main_category_Haute French restaurant',
    'main_category_Hong Kong style fast food restaurant',
    'main_category_Hunan restaurant',
    'main_category_Indian Muslim Restaurant',
    'main_category_Indian restaurant',
    'main_category_Italian restaurant',
    'main_category_Japanese curry restaurant',
    'main_category_Japanese restaurant',
    'main_category_Jewelry store',
    'main_category_Lighting products wholesaler',
    'main_category_Lighting store',
    'main_category_Market',
    'main_category_Mattress store',
    'main_category_Mediterranean restaurant',
    'main_category_Modern French restaurant',
    'main_category_Motorcycle parts store',
    'main_category_Motorcycle shop',
    'main_category_Motorsports store',
    'main_category_Nyonya restaurant',
    'main_category_Persian restaurant',
    'main_category_Pet Shop',
    'main_category_Pizza restaurant',
    'main_category_Produce market',
    'main_category_Restaurant',
    'main_category_Seafood restaurant',
    'main_category_Shabu-shabu restaurant',
    'main_category_Shoe Shop',
    'main_category_Shopping mall',
    'main_category_Singaporean restaurant',
    'main_category_Skateboard shop',
    'main_category_Southern Italian restaurant',
    'main_category_Sporting goods store',
    'main_category_Sri Lankan restaurant',
    'main_category_Swimwear store',
    'main_category_Taiwanese restaurant',
    'main_category_Telecommunications service provider',
    'main_category_Thai restaurant',
    'main_category_Tire shop',
    'main_category_Turkish restaurant',
    'main_category_Udon noodle restaurant',
    'main_category_Used furniture store',
    'main_category_Variety store',
    'main_category_Vitamin & supplements store',
    'main_category_Wallpaper store',
    'main_category_Western restaurant',
    'main_category_Women\'s clothing store',
    'main_category_Woodworking supply store',
    'can_claim_1',
    'is_local_guide_1'
]

# Path to your saved model and tokenizer
# Assuming the 'fine-tuned-distilbert' folder is in the same directory as this script.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "../results/fine-tuned-distilbert")

# Load the tokenizer and model
try:
    if not os.path.exists(MODEL_PATH) or (not os.path.exists(os.path.join(MODEL_PATH, "pytorch_model.bin")) and not os.path.exists(os.path.join(MODEL_PATH, "model.safetensors"))):
        raise FileNotFoundError(f"Model directory not found or missing a model file (.bin or .safetensors) at: {MODEL_PATH}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    num_additional_features = len([col for col in TRAINING_COLUMNS if col != 'review_text'])
    model = CustomClassifier("distilbert-base-uncased", num_labels=len(LABEL_MAP), num_additional_features=num_additional_features)
    
    # Load the state dict. from_pretrained will handle which file to load automatically.
    # The default behavior is to look for `pytorch_model.bin` first, then `model.safetensors`.
    # We can load the state dict directly into our custom model
    if os.path.exists(os.path.join(MODEL_PATH, "model.safetensors")):
        state_dict = load_file(os.path.join(MODEL_PATH, "model.safetensors"))
    elif os.path.exists(os.path.join(MODEL_PATH, "pytorch_model.bin")):
        state_dict = torch.load(os.path.join(MODEL_PATH, "pytorch_model.bin"))
    else:
        raise FileNotFoundError("No valid model file (.bin or .safetensors) found in the model directory.")

    model.load_state_dict(state_dict)
    model.eval()
    print("Model and tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    # Exit if the model cannot be loaded to prevent the app from starting without it.
    exit()

def preprocess_input(data):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame([data])
    
    # Initialize all one-hot encoded columns for main_category, setting them to 0
    training_category_cols = [col for col in TRAINING_COLUMNS if col.startswith('main_category_')]
    for col in training_category_cols:
        input_df[col] = 0

    # Find the one-hot encoded column that matches the input category
    input_main_category = input_df['main_category'].iloc[0]
    matched_col_name = f'main_category_{input_main_category}'
    
    # If the input category is one of the training categories, set its column to 1
    if matched_col_name in input_df.columns:
        input_df[matched_col_name] = 1

    # Handle other features by renaming them to match the training data
    input_df['can_claim_1'] = input_df['can_claim'].astype(int)
    input_df['is_local_guide_1'] = input_df['is_local_guide'].astype(int)
    
    # Select and reorder columns to match the training data
    numerical_features_raw = input_df[TRAINING_COLUMNS].astype('float32')
    
    # Tokenize the text
    tokenized_input = tokenizer(
        input_df['review_text'].iloc[0],
        padding="max_length",
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )

    return tokenized_input, torch.tensor(numerical_features_raw.values, dtype=torch.float32)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        review_text = data.get('review_text', '')
        rating_person = float(data.get('rating_person', 0))
        main_category = data.get('main_category', '') # Default to empty string to avoid mismatch
        can_claim = int(data.get('can_claim', 0))
        is_local_guide = int(data.get('is_local_guide', 0))
        sentiment_polarity = float(data.get('sentiment_polarity', 0))
        sentiment_subjectivity = float(data.get('sentiment_subjectivity', 0))

        input_data = {
            'review_text': review_text,
            'rating_person': rating_person,
            'main_category': main_category,
            'can_claim': can_claim,
            'is_local_guide': is_local_guide,
            'sentiment_polarity': sentiment_polarity,
            'sentiment_subjectivity': sentiment_subjectivity
        }

        tokenized_input, numerical_features = preprocess_input(input_data)
        
        with torch.no_grad():
            outputs = model(
                input_ids=tokenized_input['input_ids'],
                attention_mask=tokenized_input['attention_mask'],
                numerical_features=numerical_features
            )
            logits = outputs[0]
            prediction = torch.argmax(logits, dim=1).item()

        predicted_label = LABEL_MAP.get(prediction, 'Unknown')
        return jsonify({'prediction': predicted_label})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
