# Configurar os classificadores Self-training

Vamos configurar dois classificadores Self-training com diferentes percentagens de dados rotulados: 30% e 50%. Self-training é um algoritmo de aprendizagem semi-supervisionada que treina um classificador nos dados rotulados e, em seguida, o utiliza para prever os rótulos dos dados não rotulados. As previsões mais confiáveis são adicionadas aos dados rotulados e o processo é repetido até a convergência.

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# Configurar os classificadores Self-training
base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
st30 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_30),
    y_30,
    "Self-training 30% de dados",
)
st50 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_50),
    y_50,
    "Self-training 50% de dados",
)
```
