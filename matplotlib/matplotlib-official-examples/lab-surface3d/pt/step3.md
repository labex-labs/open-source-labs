# Criar Dados

```python
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

Criamos os dados para o gráfico. Criamos os valores `X` e `Y` como arrays com valores espaçados uniformemente de -5 a 5 em incrementos de 0.25. Em seguida, criamos uma malha (meshgrid) de valores `X` e `Y` usando `np.meshgrid()`. Usamos a malha para calcular os valores `R`, que é a distância da origem. Em seguida, calculamos os valores `Z` usando a função `sin()` de `R`.
