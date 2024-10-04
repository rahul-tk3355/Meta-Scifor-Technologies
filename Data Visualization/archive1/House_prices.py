import pandas as pd 
import tensorflow as tf 
from tensorflow.keras import layers, models 
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error 

# load the dataset
df = pd.read_csv('HousingData.csv')

# preprocessing the dataset
# print(df.isnull().sum())
df[['CRIM', 'AGE', 'LSTAT']] = df[['CRIM', 'AGE', 'LSTAT']].fillna(df[['CRIM', 'AGE', 'LSTAT']].mean())  # fills CRIM and AGE cols. when you are reassigning the df[['CRIM', 'AGE']] directly to df[['CRIM', 'AGE']] again, no need to give "inplace=True". The original DataFrame automatically gets updated.
df = df.drop(['ZN', 'CHAS'], axis=1)  # drop 'ZN' and "CHAS" columns
df['INDUS'] = df['INDUS'].bfill()

# Define X (features) and y (target)
X = df.drop('MEDV', axis=1)  # taking all the columns as features except MEDV column. So dropping it.
y = df['MEDV'] # target 

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)

# initailize the model object from LinearRegression class (house prices prediction)
model = LinearRegression()

# training the model
model.fit(X_train, y_train)

# predicting the model
y_pred = model.predict(X_test)

# evaluate the model
mse = mean_squared_error(y_pred, y_test) #here actual value(y_test) is compared with predicted values(y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# Create a DataFrame for analyzing actual vs predicted values
comparison_df = pd.DataFrame({
    'Actual price': y_test, 
    'Predicted price': y_pred}).reset_index(drop=True)  # to display rows from 0 index number 

print(comparison_df.head()) # only top 5 rows.

# visualize using seaborn
plt.figure(figsize=(8, 6))  # figure size = 8 inches width, 6 inches height
sns.scatterplot(x='Actual price', y='Predicted price', data=comparison_df)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', linewidth=2)
plt.title('Actual vs Predicted Prices (Linear Regression)')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.show()

# the lower the mse value is , better is the model performance . It means that predicted values are much closer to the actual values of the model.
# the higher the mse value is, lower is the model performance.

# TensorFlow Neural Network Model

model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),  # Input layer
    layers.Dense(64, activation='relu'),  # Hidden layer
    layers.Dense(32, activation='relu'),  # Hidden layer
    layers.Dense(1)  # Output layer for regression (no activation function)
])

#compile model
model.compile(optimizer='adam',
                loss='mean_squared_error' 
)

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)

# Predicting the model
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (Neural Network): {mse:.2f}')

# analyzing actual vs predicted values in a dataframe
comparison_df_nn = pd.DataFrame({
    'Actual price': y_test,
    'Predicted price': y_pred.flatten()
}).reset_index(drop=True)

print(comparison_df_nn.head())

# Visualize using seaborn
plt.figure(figsize=(8, 6))  
sns.scatterplot(x='Actual price', y='Predicted price', data=comparison_df_nn)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', linewidth=2)
plt.title('Actual vs Predicted Prices (Neural Network)')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.show()