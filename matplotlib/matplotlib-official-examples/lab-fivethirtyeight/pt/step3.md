# Criar Dados para o Gráfico de Linha

Nesta etapa, criaremos dados para nosso gráfico de linha. Usaremos a função `linspace` do NumPy para criar um array (vetor/matriz) de valores espaçados uniformemente entre 0 e 10. Também geraremos algum ruído aleatório usando a função `random.randn` do NumPy.

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```
