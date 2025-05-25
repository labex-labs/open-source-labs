# Carregar Dados

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

O conjunto de dados `breast_cancer` é carregado e embaralhado. Em seguida, as etiquetas verdadeiras são copiadas para `y_true`, e todas as etiquetas são removidas, exceto as primeiras 50 amostras de `y`. Isto será usado para simular um cenário de aprendizagem semi-supervisionada.
