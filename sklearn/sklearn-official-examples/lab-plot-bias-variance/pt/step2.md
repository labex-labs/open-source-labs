# Definição dos Parâmetros

Precisamos definir os parâmetros que controlam o tamanho dos conjuntos de dados, o número de iterações e o desvio padrão do ruído.

```python
n_repeat = 50  # Número de iterações para o cálculo das expectativas
n_train = 50  # Tamanho do conjunto de treinamento
n_test = 1000  # Tamanho do conjunto de teste
noise = 0.1  # Desvio padrão do ruído
np.random.seed(0)
```
