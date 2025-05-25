# Método Nystroem para Aproximação de Kernel

O método Nystroem é uma técnica geral para aproximar kernels usando uma aproximação de baixa classificação. Ele subamostra o conjunto de dados no qual o kernel é avaliado. Por padrão, ele usa o kernel RBF, mas pode ser usado com qualquer função kernel ou uma matriz kernel pré-calculada.

Para usar o método Nystroem para aproximação de kernel, siga estas etapas:

1. Inicialize o objeto Nystroem com o número desejado de componentes (ou seja, a dimensionalidade de destino da transformação de características).

```python
from sklearn.kernel_approximation import Nystroem

n_components = 100
nystroem = Nystroem(n_components=n_components)
```

2. Ajuste o objeto Nystroem aos seus dados de treinamento.

```python
nystroem.fit(X_train)
```

3. Transforme seus dados de treinamento e teste usando o objeto Nystroem.

```python
X_train_transformed = nystroem.transform(X_train)
X_test_transformed = nystroem.transform(X_test)
```
