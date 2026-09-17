from sklearn.tree import DecisionTreeClassifier

X = [
    [0, 0],  # Sunny, Hot
    [0, 1],  # Sunny, Cool
    [1, 1],  # Rainy, Cool
    [1, 0],  # Rainy, Hot
    [2, 0],  # Cloudy, Hot
    [2, 1],  # Cloudy, Cool
    [0, 0],  # Sunny, Hot
    [1, 1]   # Rainy, Cool
]

y = [0, 1, 1, 0, 1, 1, 0, 1]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

prediction = model.predict([[0, 1]])

print("Prediction:", prediction[0])

if prediction[0] == 1:
    print("Play Game")
else:
    print("Do Not Play")