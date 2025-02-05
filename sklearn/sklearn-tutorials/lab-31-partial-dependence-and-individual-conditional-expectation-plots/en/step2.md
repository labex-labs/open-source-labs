# Load and prepare the data

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# Create a DataFrame for easier data manipulation
df = pd.DataFrame(X, columns=feature_names)
```
