# Contorno de Acordo com a Distância dos Cantos do Triângulo

Nesta etapa, faremos o contorno de acordo com a distância dos cantos do triângulo. Definiremos uma função de distância de pontos individuais e faremos o contorno de acordo com essa função.

```python
# Define a nice function of distance from individual pts
def f(x, y, pts):
    z = np.zeros_like(x)
    for p in pts:
        z = z + 1/(np.sqrt((x - p[0])**2 + (y - p[1])**2))
    return 1/z

X, Y = np.meshgrid(np.linspace(-1, 1, 51), np.linspace(-1, 1, 51))
Z = f(X, Y, pts)

CS = plt.contour(X, Y, Z, 20)

tellme('Use o mouse para selecionar as localizações dos rótulos do contorno, botão do meio para finalizar')
CL = plt.clabel(CS, manual=True)
```
