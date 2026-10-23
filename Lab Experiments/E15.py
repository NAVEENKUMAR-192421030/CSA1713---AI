
# Decision Tree Classification

from sklearn.tree import DecisionTreeClassifier

# Sample dataset
# Features: [Weather, Temperature]
# Weather: 0 = Sunny, 1 = Rainy
# Temperature: 0 = Cool, 1 = Hot

X = [
    [0, 1],
    [0, 0],
    [1, 1],
    [1, 0],
    [0, 1],
    [1, 1]
]

# Target: 0 = No, 1 = Yes
y = [0, 0, 1, 1, 0, 1]

# Create the Decision Tree model
model = DecisionTreeClassifier(random_state=0)

# Train the model
model.fit(X, y)

# Predict for new data
weather = int(input("Enter weather (0=Sunny, 1=Rainy): "))
temperature = int(input("Enter temperature (0=Cool, 1=Hot): "))

prediction = model.predict([[weather, temperature]])

# Display the result
if prediction[0] == 1:
    print("Prediction: Yes")
else:
    print("Prediction: No")
