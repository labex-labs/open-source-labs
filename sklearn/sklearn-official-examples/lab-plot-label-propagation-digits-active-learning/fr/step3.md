# Entraîner le modèle de propagation de labels

Nous allons maintenant entraîner un modèle de propagation de labels avec les points de données étiquetés et l'utiliser pour prédire les étiquettes des points de données non étiquetés restants.

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
