# Gerar Dados

Em seguida, geraremos alguns dados para usar em nossa regressão. Criaremos uma tendência monotónica não linear com ruído uniforme homocedástico.

```python
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50.0 * np.log1p(np.arange(n))
```
