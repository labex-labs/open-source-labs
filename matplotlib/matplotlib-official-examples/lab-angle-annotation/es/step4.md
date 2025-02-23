# Trazar dos líneas que se cruzan y etiquetar cada ángulo entre ellas con la herramienta `AngleAnnotation` descrita anteriormente.

```python
fig, ax = plt.subplots()
fig.canvas.draw()  # Es necesario dibujar la figura para definir el renderer
ax.set_title("Ejemplo de AngleLabel")

# Trazar dos líneas que se cruzan y etiquetar cada ángulo entre ellas con la
# herramienta ``AngleAnnotation`` descrita anteriormente.
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


# Mostrar algunas opciones de estilo para el arco del ángulo, así como para el texto.
p = [(6.0, 400), (5.3, 410), (5.6, 300)]
ax.plot(*zip(*p))
am5 = AngleAnnotation(p[1], p[0], p[2], ax=ax, size=40, text=r"$\Phi$",
                      linestyle="--", color="gray", textposition="outside",
                      text_kw=dict(fontsize=16, color="gray"))

plt.show()
```
