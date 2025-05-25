# Carregar e preparar os dados

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# Criar um DataFrame para facilitar a manipulação dos dados
df = pd.DataFrame(X, columns=feature_names)
```
