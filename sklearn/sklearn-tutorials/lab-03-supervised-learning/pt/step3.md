# Máquinas de Vetores de Suporte (SVMs)

Neste passo, exploraremos o conceito de máquinas de vetores de suporte (SVMs) e como elas podem ser usadas para tarefas de classificação. As SVMs visam encontrar um hiperplano que separe maximizando os pontos de dados de diferentes classes.

#### Criar e Ajustar uma SVM Linear

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### Criar e Ajustar SVMs com Núcleos Diferentes

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
