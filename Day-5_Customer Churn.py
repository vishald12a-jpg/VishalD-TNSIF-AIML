from sklearn.ensemble import RandomForestClassifier

X = [
    [22, 2, 500],
    [25, 5, 600],
    [30, 1, 800],
    [35, 8, 550],
    [40, 10, 500],
    [28, 3, 900],
    [45, 12, 650],
    [32, 2, 850]
]

y = [1, 0, 1, 0, 0, 1, 0, 1]

model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

model.fit(X, y)

prediction = model.predict([[27, 3, 750]])

print("Prediction:", prediction[0])

if prediction[0] == 1:
    print("Customer will Leave")
else:
    print("Customer will Stay")