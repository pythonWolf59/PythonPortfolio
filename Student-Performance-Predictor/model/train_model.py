import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the dataset
df = pd.read_csv('Student-Performance-Predictor/dataset/student-mat.csv', sep=";")

# Optional: Combine related features (e.g., G1, G2, G3)
df['average_grade'] = df[['G1', 'G2']].mean(axis=1)
df = df.drop(columns=['G1', 'G2'])

# Set target and features
X = df.drop(columns=['G3'])  # G3 = final grade
y = df['G3']

# Encode categorical features
label_cols = X.select_dtypes(include=['object']).columns
X[label_cols] = X[label_cols].apply(LabelEncoder().fit_transform)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'MSE: {mse:.2f}')
print(f'R2 Score: {r2:.2f}')

# Save model
joblib.dump(model, 'D:/PythonPortfolio/Student-Performance-Predictor/model/student_grade_predictor.pkl')
print("Model saved successfully.")