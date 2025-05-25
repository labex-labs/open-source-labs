# Treinar e Avaliar o Modelo de Autoaprendizagem

Nesta etapa, utilizaremos o Autoaprendizagem (Self-Training) em 20% dos dados rotulados. Selecionaremos aleatoriamente 20% dos dados rotulados, treinaremos o modelo com esses dados e, em seguida, usaremos o modelo para prever rótulos para os dados não rotulados restantes.

```python
import numpy as np

# Selecionar 20% dos dados de treinamento
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# Definir o subconjunto não mascarado como não rotulado
y_train[~y_mask] = -1

# Treinar e avaliar o pipeline de Autoaprendizagem
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "Pontuação F1 média no conjunto de teste: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
