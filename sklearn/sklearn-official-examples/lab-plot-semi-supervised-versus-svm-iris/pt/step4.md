# Configurar o classificador SVM

Vamos configurar um classificador SVM com um kernel de função de base radial (RBF). SVM é um algoritmo de aprendizagem supervisionada que encontra o hiperplano ótimo que separa os dados em diferentes classes.

```python
from sklearn.svm import SVC

# Configurar o classificador SVM
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "SVC com kernel rbf")
```
