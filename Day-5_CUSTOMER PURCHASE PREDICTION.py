import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# 1. Create Dataset

data = {
    "Age": [20, 22, 25, 28, 30, 32, 35, 38, 40, 45],

    "Income": [
        15000, 18000, 22000, 30000, 35000,
        40000, 45000, 50000, 55000, 60000
    ],

    "Purchased": [
        0, 0, 0, 1, 1,
        1, 1, 1, 1, 1
    ]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. Separate Features and Target

X = df[["Age", "Income"]]
y = df["Purchased"]


# 3. Split Data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 4. Logistic Regression

logistic_model = LogisticRegression()

logistic_model.fit(X_train, y_train)

logistic_pred = logistic_model.predict(X_test)

logistic_accuracy = accuracy_score(
    y_test,
    logistic_pred
)


# 5. Decision Tree

tree_model = DecisionTreeClassifier(
    random_state=42
)

tree_model.fit(X_train, y_train)

tree_pred = tree_model.predict(X_test)

tree_accuracy = accuracy_score(
    y_test,
    tree_pred
)


# 6. Accuracy

print("\nModel Accuracy")

print(
    "Logistic Regression:",
    logistic_accuracy * 100,
    "%"
)

print(
    "Decision Tree:",
    tree_accuracy * 100,
    "%"
)


# 7. New Customer Prediction

new_customer = [[27, 28000]]

logistic_prediction = logistic_model.predict(
    new_customer
)

tree_prediction = tree_model.predict(
    new_customer
)


print("\nNew Customer Prediction")

print(
    "Logistic Regression:",
    logistic_prediction[0]
)

print(
    "Decision Tree:",
    tree_prediction[0]
)


# 8. Convert 0/1 to Meaning

if logistic_prediction[0] == 1:
    print("Logistic Regression → Purchase")
else:
    print("Logistic Regression → No Purchase")


if tree_prediction[0] == 1:
    print("Decision Tree → Purchase")
else:
    print("Decision Tree → No Purchase")