from sklearn.linear_model import LinearRegression
import pandas as pd

# Simple Linear Regression
linear_model = LinearRegression()

df = pd.read_csv("auto.csv")

# Create headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# Add headers to the dataframe
df.columns = headers

# Convert 'price' column to numeric, forcing errors to NaN
df['price'] = pd.to_numeric(df['price'], errors='coerce')
# Drop rows with NaN values in 'price' column
df.dropna(subset=['price'], inplace=True)

X = df[['highway-mpg']]
Y = df[['price']]

linear_model.fit(X,Y)

prediction = linear_model.predict(X)
print(f" Predicted Value: {prediction[0]}")
print(f" Actual Value: {df['price'].values[0]}")