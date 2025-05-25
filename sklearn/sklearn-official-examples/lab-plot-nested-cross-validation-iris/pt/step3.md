# Definir o Modelo

Utilizamos um classificador de vetores de suporte com um kernel de função de base radial.

```python
from sklearn.svm import SVC

# Usaremos um Classificador de Vetores de Suporte com kernel "rbf"
svm = SVC(kernel="rbf")
```
