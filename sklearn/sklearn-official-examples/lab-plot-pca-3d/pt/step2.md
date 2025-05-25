# Criar Dados

Vamos gerar um conjunto de dados aleatório para este laboratório. O conjunto de dados terá três variáveis: `x`, `y` e `z`. Definiremos `x` e `y` como variáveis aleatórias normalmente distribuídas com média 0 e desvio padrão de 0,5. `z` também é normalmente distribuída com média 0 e desvio padrão de 0,1.

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```
