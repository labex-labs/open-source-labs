# Calculando as Pontuações de Validação

Usaremos a função `validation_curve` do scikit-learn para calcular as pontuações de treinamento e validação para o classificador SVM com diferentes valores de gama.

```python
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

train_scores, test_scores = validation_curve(
    SVC(),
    X,
    y,
    param_name="gamma",
    param_range=param_range,
    scoring="accuracy",
    n_jobs=2,
)
```
