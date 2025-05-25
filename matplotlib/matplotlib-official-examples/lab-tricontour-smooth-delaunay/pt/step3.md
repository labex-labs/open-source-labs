# Gerar Pontos de Dados de Teste

Geramos um conjunto de pontos de dados de teste aleatórios, com valores x e y entre -1 e 1. Também geramos um conjunto correspondente de valores z usando a função `experiment_res` definida no passo 2.

```python
# Parâmetros do usuário para pontos de dados de teste

# Número de pontos de dados de teste, testado de 3 a 5000 para subdiv=3
n_test = 200

# Pontos aleatórios
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```
