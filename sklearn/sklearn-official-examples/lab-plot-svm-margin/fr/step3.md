# Ajuster le modèle

Nous ajustons le modèle SVM à l'aide de la classe `SVC` de scikit-learn. Nous définissons le noyau sur linéaire et le paramètre de pénalité `C` sur 1 pour le cas non régularisé et 0,05 pour le cas régularisé. Nous calculons ensuite l'hyperplan de séparation à l'aide des coefficients et de l'intercept du modèle.

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```
