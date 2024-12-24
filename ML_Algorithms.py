from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd


# Load California Housing dataset
housing = fetch_california_housing()

# Convert to pandas DataFrame for easy manipulation
df = pd.DataFrame(housing.data, columns=housing.feature_names)

# Add target (house prices) to the DataFrame
df['target'] = housing.target


def linear_regression_model(data):
    '''
        Using Linear Regression to predict house prices on California Housing Dataset

        data => A pandas dataframe 
        mse => Mean Squared Error of algorithm
        predictions => House prices predicted by alogrithm

    '''
    # Select features (X) and target (y)
    X = data.drop(columns=["target"])  # Features (drop the target column)
    y = data["target"]  # Target variable (house prices)

    # Split data into Test and Train subsets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on test data
    predictions = model.predict(X_test)

        # Evaluate the model
    mse = mean_squared_error(y_test, predictions)

    return mse,predictions


housing_prices = linear_regression_model(df)
print(f"Mean Squared Error (MSE) => {housing_prices[0]}\n")
print(f"Predictions Made By Algorithm in Thousands of Dollars =>\n{housing_prices[1]}")