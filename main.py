
import numpy as np
import pandas as pd #mot clé ici: dataframes
import pdfplumber

def extract_data_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_tables = []
        
        for page in pdf.pages:
            tables = page.extract_tables()
            
            for table in tables:
                all_tables.append(table)
    return all_tables

def process_extracted_tables(tables):
    #convert list of tables into dataframes
    dfs = [pd.DataFrame(table) for table in tables]
    
    #combine in single dataframe
    combined_df = pd.concat(dfs, ignore_index=True)
    
    #remove any rows or columns that are entirely NaN (this is common in table extraction)
    combined_df.dropna(axis=0, how='all', inplace=True)
    combined_df.dropna(axis=1, how='all', inplace=True)
    
    return combined_df


raw_data = extract_data_from_pdf('programmeNova2023.pdf')
processed_data = process_extracted_tables(raw_data)
print(processed_data)
        
 