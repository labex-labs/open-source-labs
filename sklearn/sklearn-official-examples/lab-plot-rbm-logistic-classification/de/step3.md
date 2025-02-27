# Training

In diesem Schritt trainieren wir das in dem vorherigen Schritt definierte Pipeline-Modell. Wir setzen die Hyperparameter des Modells (Lernrate, Größe der versteckten Schicht, Regularisierung) und passen dann die Trainingsdaten an das Modell an.

```python
from sklearn.base import clone

# Hyperparameter. Diese wurden durch Kreuzvalidierung festgelegt,
# unter Verwendung eines GridSearchCV. Hier führen wir keine Kreuzvalidierung durch,
# um Zeit zu sparen.
rbm.learning_rate = 0.06
rbm.n_iter = 10

# Mehr Komponenten tendieren dazu, eine bessere Vorhersageleistung zu liefern, aber eine längere
# Anpassungszeit
rbm.n_components = 100
logistic.C = 6000

# Training des RBM-Logistic-Pipelines
rbm_features_classifier.fit(X_train, Y_train)
```
