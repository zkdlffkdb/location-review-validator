# location-review-validator
Project for TikTok TechJam 2025 by 4/5Bza

## Project overview
The project aims to improve the quality and relevance of Google Maps reviews by automatically classifying them into meaningful categories and filtering out noise such as spam, advertisements, irrelevant content, or rants from users who have not visited the location. 

## Setup instructions
- On initial setup, run `python -m venv venv`  
- Install requirements on the virtual environment with `pip install -r requirements.txt` (note that the repository uses Python 3.12)  
- (For devs) The repository does not include the data folder, so include it with the required data as per the directory.  
- To run the backend, run `python ./src/main.py` to startup the backend server
- To run the frontend, navigate to the web-app directory and run `npm install` then`npm run dev `.

**This repository uses Git LFS for large model files**  
_if the model.safetensors is not there, ensure you have git lfs installed_
1. Install Git LFS:
```bash
git lfs install
```
1. Clone the repository
2. Model files will be automatically downloaded

**Alternative for users without LFS:**
- They can download the large files directly from GitHub's web interface
- Or install Git LFS after cloning: `git lfs install && git lfs pull`

### Data Setup
1. Run data_processing.py to get the data file for labelling and analysis

## How to reproduce results
For the fine-tuned ML model,  
- Run train_text_classifier.ipynb (use google colab notebook for faster runtime).
- Ensure you have cleaned_labelled_data.csv.

## Directory
location-review-validator/  
│  
├── README.md  
├── data                    # includes raw data, labelled data and train and test data  
│   ├── train/  
│   ├── test/  
│   ├── restaurants-and-shops-detailed-reviews.csv  
│   ├── restaurants-and-shops-overview.csv  
├── notebooks  
│   ├── eda.ipynb           # Exploratory data analysis  
├── requirements.txt  
├── results                 # Tentatively contains evaluation metrics results and prediction results 
│   ├── fine-tuned-distilbert/
│   ├── checkpoint-XXX/ 
├── src                     # Data engineering and ML files  
│   ├── data_processing.py  # Handles data processing, cleaning  
├── venv  
└── web-app                 # Web app files  





