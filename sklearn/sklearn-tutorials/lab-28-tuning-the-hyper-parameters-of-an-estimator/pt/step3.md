# Definir o estimador e a grade de parâmetros

Agora precisamos definir o estimador que queremos afinar e a grade de parâmetros que queremos pesquisar. A grade de parâmetros especifica os valores que queremos testar para cada hiperparâmetro.

```python
from sklearn.svm import SVC

# Criar uma instância do classificador de vetores de suporte
svc = SVC()

# Definir a grade de parâmetros
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```
