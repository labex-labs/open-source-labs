# Criar a Malha (Mesh)

Em seguida, criaremos a malha em coordenadas polares e calcularemos o Z correspondente. Criaremos um array de valores de raio `r`, um array de valores de ângulo `p` e, em seguida, usaremos a função `meshgrid()` do NumPy para criar uma grade de valores `R` e `P`. Finalmente, usaremos a equação `Z` para calcular a altura de cada ponto na superfície.

```python
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
```
