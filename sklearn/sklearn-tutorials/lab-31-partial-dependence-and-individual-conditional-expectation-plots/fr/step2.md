# Chargez et préparez les données

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# Créez un DataFrame pour faciliter la manipulation des données
df = pd.DataFrame(X, columns=feature_names)
```
