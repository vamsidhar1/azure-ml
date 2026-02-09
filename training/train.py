
---

## 🔹 training/train.py

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import mlflow
import mlflow.sklearn

df = pd.read_csv("data/sample-data.csv")

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)

mlflow.log_metric("accuracy", accuracy)

joblib.dump(model, "model.pkl")

mlflow.sklearn.log_model(
    sk_model=model,
    artifact_path="model",
    registered_model_name="support-ticket-classifier"
)

