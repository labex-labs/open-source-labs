# Komplexere Beschriftungen plotten

In diesem Schritt werden wir komplexere Beschriftungen plotten.

```python
# Definiere Daten für das Diagramm
x = np.linspace(0, 1)

# Erstelle ein Diagramm mit mehreren Linien
fig, (ax0, ax1) = plt.subplots(2, 1)
for n in range(1, 5):
    ax0.plot(x, x**n, label=f"{n=}")

# Erstelle eine Legende mit mehreren Spalten und einem Titel
leg = ax0.legend(loc="upper left", bbox_to_anchor=[0, 1],
                 ncols=2, shadow=True, title="Legende", fancybox=True)
leg.get_title().set_color("rot")

# Erstelle ein Diagramm mit mehreren Linien und Markern
ax1.plot(x, x**2, label="mehrere\nLinien")
half_pi = np.linspace(0, np.pi / 2)
ax1.plot(np.sin(half_pi), np.cos(half_pi), label=r"$\frac{1}{2}\pi$")
ax1.plot(x, 2**(x**2), label="$2^{x^2}$")

# Erstelle eine Legende mit einer Schatteneffekt
ax1.legend(shadow=True, fancybox=True)

# Zeige das Diagramm an
plt.show()
```
