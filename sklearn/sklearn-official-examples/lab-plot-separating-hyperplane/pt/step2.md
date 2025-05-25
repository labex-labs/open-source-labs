# Ajustar o Modelo SVM

Em seguida, ajustaremos o modelo SVM aos nossos dados utilizando um kernel linear e um parâmetro de regularização de 1000. Usaremos a função `svm.SVC()` do scikit-learn para criar o classificador SVM.

```python
from sklearn import svm

# ajustar o modelo SVM
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```
