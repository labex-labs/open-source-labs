# Utilisation de Mathtext

Mathtext est une fonctionnalité de Matplotlib qui vous permet d'utiliser des commandes TeX pour afficher des symboles et des équations mathématiques. Mathtext prend également en charge les caractères accentués.

```python
import matplotlib.pyplot as plt

# Démo Mathtext
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_title(r'$\ddot{o}\acute{e}\grave{e}\hat{O}'
             r'\breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)

# Le raccourci est également pris en charge et les accolades sont facultatives
ax.set_xlabel(r"""$\"o\ddot o \'e\`e\~n\.x\^y$""", fontsize=20)
ax.text(4, 0.5, r"$F=m\ddot{x}$")
fig.tight_layout()
```
