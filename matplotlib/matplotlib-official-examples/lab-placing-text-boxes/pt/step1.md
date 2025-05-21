# Criando um Jupyter Notebook e Preparando os Dados

Neste primeiro passo, criaremos um novo Jupyter Notebook e configuraremos nossos dados para visualização.

## Criando um Novo Notebook

Na primeira célula do notebook, vamos importar as bibliotecas necessárias. Digite o seguinte código e execute-o clicando no botão "Run" ou pressionando Shift+Enter:

```python
import matplotlib.pyplot as plt
import numpy as np
```

![libraries-imported](../assets/screenshot-20250306-Azb1cb3S@2x.png)

Este código importa duas bibliotecas essenciais:

- `matplotlib.pyplot`: Uma coleção de funções que fazem o matplotlib funcionar como o MATLAB
- `numpy`: Um pacote fundamental para computação científica em Python

## Criando Dados de Amostra

Agora, vamos criar alguns dados de amostra que visualizaremos. Em uma nova célula, insira e execute o seguinte código:

```python
# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate 10,000 random numbers from a normal distribution
x = 30 * np.random.randn(10000)

# Calculate basic statistics
mu = x.mean()
median = np.median(x)
sigma = x.std()

# Display the statistics
print(f"Mean (μ): {mu:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
```

Ao executar esta célula, você deverá ver uma saída semelhante a:

```
Mean (μ): -0.31
Median: -0.28
Standard Deviation (σ): 29.86
```

Os valores exatos podem variar ligeiramente. Criamos um conjunto de dados com 10.000 números aleatórios gerados a partir de uma distribuição normal e calculamos três estatísticas importantes:

1. Média (μ): O valor médio de todos os pontos de dados
2. Mediana: O valor do meio quando os dados são organizados em ordem
3. Desvio Padrão (σ): Uma medida de quão dispersos os dados estão

Essas estatísticas serão usadas posteriormente para anotar nossa visualização.
