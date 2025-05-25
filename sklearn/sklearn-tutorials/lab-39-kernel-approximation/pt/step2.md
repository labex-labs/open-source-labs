# Aproximação de Kernel Radial Basis Function (RBF)

A classe RBFSampler implementa um mapeamento aproximado para o kernel RBF, também conhecido como Random Kitchen Sinks. Essa técnica permite modelar explicitamente um mapeamento de kernel antes de aplicar um algoritmo linear, como SVM linear ou regressão logística.

Para usar o RBFSampler para aproximação de kernel, siga estas etapas:

1. Inicialize o objeto RBFSampler com o valor desejado de gamma (o parâmetro do kernel RBF) e o número de componentes.

```python
from sklearn.kernel_approximation import RBFSampler

gamma = 0.1
n_components = 100
rbf_sampler = RBFSampler(gamma=gamma, n_components=n_components)
```

2. Ajuste o objeto RBFSampler aos seus dados de treinamento.

```python
rbf_sampler.fit(X_train)
```

3. Transforme seus dados de treinamento e teste usando o objeto RBFSampler.

```python
X_train_transformed = rbf_sampler.transform(X_train)
X_test_transformed = rbf_sampler.transform(X_test)
```
