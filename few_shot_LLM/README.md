
# Few-Shot LLM Classification System

## Overview
This project is designed for classifying reviews using a few-shot learning approach with a Language Model (LLM). It processes reviews and outputs labels based on their content, using a set of predefined categories.

## Folder Structure
- `few_shot_LLM/`: Main folder containing the LLM system setup.
  - `few_shot_materials/few_shot.md`: Contains the few-shot learning examples and system prompt.
  - `inference.py`: Script to handle the inference and classify input reviews.

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone <repo-url>
   ```

2. Install required dependencies (if any). You can include this step if you’re using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables (e.g., `OPENROUTER_API_KEY`) to authenticate with the API.

## Usage

To classify a review, follow these steps:

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repo-url>
   ```

2. **Set up your environment**:
   ```bash
    python settings/setup_env.py
   ```

3. **Run the inference script** to classify a review by providing the review data in JSON format as input:
   ```bash
   python inference.py '{
     "review_text": "Had an amazing dinner here. The wagyu beef was perfectly cooked, and the sommelier recommended an excellent wine pairing. Staff were attentive but not intrusive. Easily one of my top 5 restaurants in Singapore.",
     "rating_person": 5,
     "main_category": "Fine dining restaurant",
     "can_claim": 0,
     "is_local_guide": 1,
     "sentiment_polarity": 0.6,
     "sentiment_subjectivity": 0.8
   }'
   ```
   This will return a **classification label** based on the review content.