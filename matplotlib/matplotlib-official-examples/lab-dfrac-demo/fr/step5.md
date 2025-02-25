# Tracer les données avec \dfrac

Nous allons tracer les données avec la macro TeX \dfrac et afficher le tracé résultant.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
