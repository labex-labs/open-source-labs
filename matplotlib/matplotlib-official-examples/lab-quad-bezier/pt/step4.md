# Criando o Gráfico (Plot)

Agora podemos criar o gráfico adicionando o objeto `PathPatch` aos eixos e plotando um ponto vermelho que deve estar na curva. Também definiremos o título do gráfico como `'Bezier Curve'`.

```python
fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```

O código final deve ser assim:

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath

Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])

bezier_patch = mpatches.PathPatch(bezier_path, fc="none")

fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```
