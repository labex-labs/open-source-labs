# Ajustar o Modelo

Ajustamos o modelo SVM usando a classe `SVC` do scikit-learn. Definimos o kernel como linear e o parâmetro de penalidade `C` como 1 para o caso não regularizado e 0,05 para o caso regularizado. Em seguida, calculamos o hiperplano separador usando os coeficientes e a intersecção do modelo.

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```
