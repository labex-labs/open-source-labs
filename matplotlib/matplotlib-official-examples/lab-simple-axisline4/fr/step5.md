# Définissez les étiquettes d'échelonnage pour le second axe y

Nous pouvons définir les étiquettes d'échelonnage pour le second axe y en utilisant la fonction `set_xticks` et en passant les emplacements et les étiquettes d'échelonnage en tant qu'arguments.

```python
ax2.set_xticks([0.,.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```
