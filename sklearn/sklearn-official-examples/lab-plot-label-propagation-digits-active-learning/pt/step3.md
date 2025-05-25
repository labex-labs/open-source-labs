# Treinar o Modelo de Propagação de Rótulos

Agora, treinaremos um modelo de propagação de rótulos com os pontos de dados rotulados e o usaremos para prever os rótulos dos pontos de dados não rotulados restantes.

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
