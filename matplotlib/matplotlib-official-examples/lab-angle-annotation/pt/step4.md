# Plotar Duas Linhas Cruzadas e Rotular Cada Ângulo Entre Elas com a Ferramenta `AngleAnnotation` Acima.

```python
fig, ax = plt.subplots()
fig.canvas.draw()  # Precisa desenhar a figura para definir o renderizador (renderer)
ax.set_title("Exemplo de AngleLabel")

# Plotar duas linhas cruzadas e rotular cada ângulo entre elas com a ferramenta
# ``AngleAnnotation`` acima.
center = (4.5, 650)
p1 = [(2.5, 710), (6.0, 605)]
p2 = [(3.0, 275), (5.5, 900)]
line1, = ax.plot(*zip(*p1))
line2, = ax.plot(*zip(*p2))
point, = ax.plot(*center, marker="o")

am1 = AngleAnnotation(center, p1[1], p2[1], ax=ax, size=75, text=r"$\alpha$")
am2 = AngleAnnotation(center, p2[1], p1[0], ax=ax, size=35, text=r"$\beta$")
am3 = AngleAnnotation(center, p1[0], p2[0], ax=ax, size=75, text=r"$\gamma$")
am4 = AngleAnnotation(center, p2[0], p1[1], ax=ax, size=35, text=r"$\theta$")


# Apresentar algumas opções de estilo para o arco do ângulo, bem como o texto.
p = [(6.0, 400), (5.3, 410), (5.6, 300)]
ax.plot(*zip(*p))
am5 = AngleAnnotation(p[1], p[0], p[2], ax=ax, size=40, text=r"$\Phi$",
                      linestyle="--", color="gray", textposition="outside",
                      text_kw=dict(fontsize=16, color="gray"))

plt.show()
```
