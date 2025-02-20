import numpy as np
import pandas as pd
import scipy.stats as stats
import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux
    else:
        _ = os.system('clear')


#Download Dataset
# import asyncio
# import aiohttp

# async def download(url, filename):
# 	async with aiohttp.ClientSession() as session:
# 		async with session.get(url) as response:
# 			with open(filename, 'wb') as f:
# 				f.write(await response.read())

# async def main():
# 	await download("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv", "auto.csv")
# 	file_name = "auto.csv"
# 	file_name = "auto.csv"

# asyncio.run(main())

df = pd.read_csv("auto.csv")

# Create headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# Add headers to the dataframe
df.columns = headers

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)

# Find missing data columns with True/False
missing_data = df.isnull()

for column in missing_data.columns.values.tolist():
    print (missing_data[column].value_counts())
    print("")

# Descriptive Statistics

print(df.describe())    # Non numeric data only

# Convert 'price' column to numeric, forcing errors to NaN
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows with NaN values in 'price' column
df.dropna(subset=['price'], inplace=True)

# Categorical data
drive_wheel_counts = df['drive-wheels'].value_counts().reset_index()

df_test = df[['drive-wheels', 'body-style', 'price']]
df_grp = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()

# Pivot table
df_pivot = df_grp.pivot(index='drive-wheels', columns='body-style')
print(df_pivot)

def calculate_pearson_correlation(dataFrame):
    """
    Calculate Pearson correlation coefficient and p-value for two user-selected numeric columns from a DataFrame.
    Provides easy-to-understand output for non-technical users.
    
    Parameters:
    dataFrame (pandas.DataFrame): Input DataFrame containing the data
    
    Returns:
    tuple: (correlation coefficient, p-value)
    """
    clear_console()
    try:
        # Get only numeric columns
        numeric_cols = dataFrame.select_dtypes(include=['int64', 'float64', 'int32', 'float32']).columns
        
        if len(numeric_cols) < 2:
            raise ValueError("DataFrame must contain at least 2 numeric columns")
            
        # Display available numeric columns
        print("Available numeric columns in the DataFrame:")
        print(list(numeric_cols))
        
        # Get column names from user
        col1 = input("Enter the name of the first numeric column: ")
        if col1 not in numeric_cols:
            raise ValueError(f"Column '{col1}' is either not numeric or not found in DataFrame")
            
        col2 = input("Enter the name of the second numeric column: ")
        if col2 not in numeric_cols:
            raise ValueError(f"Column '{col2}' is either not numeric or not found in DataFrame")
            
        # Remove any NaN values and ensure we have paired observations
        paired_data = dataFrame[[col1, col2]].dropna()
        
        if len(paired_data) < 2:
            raise ValueError("Need at least 2 complete observations for correlation")
            
        # Calculate Pearson correlation coefficient and p-value
        correlation, p_value = stats.pearsonr(paired_data[col1], paired_data[col2])
        
        # Print raw results
        print(f"\nResults for '{col1}' and '{col2}':")
        print(f"Correlation strength (technical): {correlation:.4f}")
        print(f"Confidence level (technical): {p_value:.4f}")
        
        # Easy-to-understand interpretation
        print("\nWhat this means in simple terms:")
        if p_value < 0.05:  # Statistically significant
            if correlation > 0.7:
                print(f"There’s a strong positive relationship: As {col1} increases, {col2} tends to increase a lot.")
            elif 0.5 <= correlation <= 0.7:
                print(f"There’s a moderate positive relationship: As {col1} increases, {col2} tends to increase some.")
            elif 0 < correlation < 0.5:
                print(f"There’s a weak positive relationship: As {col1} increases, {col2} tends to increase a little.")
            elif -0.5 < correlation < 0:
                print(f"There’s a weak negative relationship: As {col1} increases, {col2} tends to decrease a little.")
            elif -0.7 <= correlation <= -0.5:
                print(f"There’s a moderate negative relationship: As {col1} increases, {col2} tends to decrease some.")
            elif correlation < -0.7:
                print(f"There’s a strong negative relationship: As {col1} increases, {col2} tends to decrease a lot.")
        else:  # Not statistically significant
            if correlation >= 0:
                print(f"There’s no clear positive relationship: Changes in {col1} don’t reliably affect {col2}.")
            else:
                print(f"There’s no clear negative relationship: Changes in {col1} don’t reliably affect {col2}.")
        
        return ""
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None

print(calculate_pearson_correlation(df))