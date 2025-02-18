import numpy as np
import pandas as pd

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

# Categorical data

drive_wheel_counts = df['drive-wheels'].value_counts().reset_index()

print(drive_wheel_counts)


