# Tracer les données avec \frac

Nous allons tracer les données avec la macro TeX \frac et afficher le tracé résultant.

```python
ax.plot(x, y, label=r'$\frac{sin(x)}{x}$')
ax.legend()
plt.show()
```
