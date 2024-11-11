import os
from data import read_params, get_data
import argparse
import pandas as pd
import csv

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    
    # Ensure column names have no spaces
    df.columns = [col.replace(" ", "_") for col in df.columns]
    
    # Convert all columns to numeric if possible
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')
    
    # Define the path to save the raw data
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    
    # Save the DataFrame to CSV without extra quotes
    df.to_csv(raw_data_path, sep=",", index=False, quoting=csv.QUOTE_MINIMAL)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)
