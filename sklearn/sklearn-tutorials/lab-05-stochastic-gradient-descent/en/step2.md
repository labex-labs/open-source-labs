# Load and preprocess the data

Next, we will load the iris dataset and preprocess it by scaling the features using StandardScaler.

```python
# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```
