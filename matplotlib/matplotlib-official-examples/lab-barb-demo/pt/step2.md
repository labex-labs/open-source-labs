# Criar Dados

Em seguida, criaremos os dados que serão usados para gerar o gráfico de "wind barb". Criaremos uma grade uniforme de 5x5 e um campo vetorial usando as funções `meshgrid` e multiplicação.

```python
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
```
