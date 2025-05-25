# Configurar os classificadores Label Spreading

Vamos configurar três classificadores Label Spreading com diferentes percentagens de dados rotulados: 30%, 50% e 100%. Label Spreading é um algoritmo de aprendizagem semi-supervisionada que propaga rótulos de pontos de dados rotulados para pontos de dados não rotulados com base na semelhança entre eles.

```python
from sklearn.semi_supervised import LabelSpreading

# Configurar os classificadores Label Spreading
rng = np.random.RandomState(0)
y_rand = rng.rand(y.shape[0])
y_30 = np.copy(y)
y_30[y_rand < 0.3] = -1  # definir amostras aleatórias como não rotuladas
y_50 = np.copy(y)
y_50[y_rand < 0.5] = -1
ls30 = (LabelSpreading().fit(X, y_30), y_30, "Label Spreading 30% de dados")
ls50 = (LabelSpreading().fit(X, y_50), y_50, "Label Spreading 50% de dados")
ls100 = (LabelSpreading().fit(X, y), y, "Label Spreading 100% de dados")
```
