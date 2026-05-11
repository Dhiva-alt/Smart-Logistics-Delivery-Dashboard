import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv(r"C:\Users\Divashini PC\Downloads\Food_Delivery_Times.csv")

# Fill missing values
df = df.ffill()
# Convert text columns into numbers
encoder = LabelEncoder()

df['Weather'] = encoder.fit_transform(df['Weather'])
df['Traffic_Level'] = encoder.fit_transform(df['Traffic_Level'])
df['Time_of_Day'] = encoder.fit_transform(df['Time_of_Day'])
df['Vehicle_Type'] = encoder.fit_transform(df['Vehicle_Type'])

# Input features
X = df[
    [
        'Distance_km',
        'Weather',
        'Traffic_Level',
        'Time_of_Day',
        'Vehicle_Type',
        'Preparation_Time_min',
        'Courier_Experience_yrs'
    ]
]

# Target column
y = df['Delivery_Time_min']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy check
mae = mean_absolute_error(y_test, predictions)

print("Model Trained Successfully")
print("Mean Absolute Error:", mae)

# Sample prediction
sample = [[
    10,  # Distance_km
    0,   # Weather
    1,   # Traffic_Level
    2,   # Time_of_Day
    1,   # Vehicle_Type
    15,  # Preparation_Time_min
    3    # Courier_Experience_yrs
]]

result = model.predict(sample)

print("Predicted Delivery Time:", result[0])
# Create Actual vs Predicted DataFrame

results = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': predictions
})

# Save results to CSV

results.to_csv(r"E:\prediction_results.csv", index=False)

print("Prediction results exported successfully")