# Treinando um Modelo de Aprendizado de Máquina

Agora que o conjunto de dados foi preparado, podemos treinar um modelo de aprendizado de máquina nos dados de treinamento. Neste exemplo, usaremos um algoritmo de Máquina de Vetores de Suporte (SVM):

```python
from sklearn.svm import SVC

# Criar o classificador SVM
clf = SVC(kernel='linear')

# Treinar o classificador nos dados de treinamento
clf.fit(X_train, y_train)
```
