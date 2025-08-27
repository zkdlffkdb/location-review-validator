# location-review-validator
Project for TikTok TechJam 2025 by 4/5Bza

## Project overview

## Setup instructions
On initial setup, run `python -m venv venv`  
Install requirements on  the virtual environment with `pip install -r requirements`
The repository does not include the data folder, so include it with the required data as per the directory.

### Data Setup
1. Run data_processing.py to get the data file for labelling and analysis

## How to reproduce results

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
├── src                     # Data engineering and ML files  
│   ├── data_processing.py  # Handles data processing, cleaning  
├── venv  
└── web-app                 # Web app files  





