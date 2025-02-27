# Ajuster le modèle de régression

Ensuite, nous ajustons un modèle SVR à notre ensemble de données d'échantillonnage en utilisant un noyau linéaire, polynomial et RBF. Nous définissons les hyperparamètres pour chaque modèle et les entraînons sur notre ensemble de données d'échantillonnage.

```python
from sklearn.svm import SVR

# Ajuster le modèle de régression
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

svrs = [svr_rbf, svr_lin, svr_poly]

for svr in svrs:
    svr.fit(X, y)
```
