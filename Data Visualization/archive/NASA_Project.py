import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers, models

#Load the dataset
data = pd.read_csv('meteorites.csv')

#Data Preprocessing
data['mass'].fillna(data['mass'].mean())
data['year'].fillna(data['year'].median())
data.dropna(subset=['lat', 'long'], inplace=True)
data['fall_encoded'] = LabelEncoder().fit_transform(data['fall'])
data['class_encoded'] = LabelEncoder().fit_transform(data['class'])

#Data Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x='year', y='mass', hue='fall', data=data)
plt.title('Meteorite Mass over Time')
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(data[['mass', 'year', 'lat', 'long']].corr(), annot=True)
plt.title('Correlation Heatmap')
plt.show()

#Prepare Data for Machine Learning
X = data[['mass', 'year', 'lat', 'long', 'fall_encoded']]
y = data['class_encoded']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#RandomForest Classifier
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f'RandomForest Accuracy: {accuracy_rf * 100:.2f}%')

#Neural Network (TensorFlow)
# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Preprocess the data
train_images = train_images / 255.0  
test_images = test_images / 255.0  

# Build the neural network
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  
    layers.Dense(128, activation='relu'),   
    layers.Dropout(0.2),                    
    layers.Dense(10, activation='softmax')   
])

# Compile the model
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5) 

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels) 
print('Neural Network Test Accuracy:', test_acc)

#Comparison
print(f'RandomForest Accuracy: {accuracy_rf * 100:.2f}%')
print(f'Neural Network Test Accuracy: {test_acc * 100:.2f}%')
