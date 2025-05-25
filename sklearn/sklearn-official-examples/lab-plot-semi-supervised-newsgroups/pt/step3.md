# Treinar e Avaliar o Modelo Supervisionado

Nesta etapa, dividiremos o conjunto de dados em conjuntos de treinamento e teste e, em seguida, treinaremos e avaliaremos o pipeline de modelo supervisionado criado na Etapa 2.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Dividir o conjunto de dados em conjuntos de treinamento e teste
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Treinar e avaliar o pipeline de modelo supervisionado
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Pontuação F1 média no conjunto de teste: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
