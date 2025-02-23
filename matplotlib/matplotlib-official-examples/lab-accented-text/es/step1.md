# Usando Mathtext

Mathtext es una característica de Matplotlib que le permite utilizar comandos TeX para representar símbolos matemáticos y ecuaciones. Mathtext también admite caracteres con tilde.

```python
import matplotlib.pyplot as plt

# Demostración de Mathtext
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_title(r'$\ddot{o}\acute{e}\grave{e}\hat{O}'
             r'\breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)

# También se admite la notación abreviada y las llaves son opcionales
ax.set_xlabel(r"""$\"o\ddot o \'e\`e\~n\.x\^y$""", fontsize=20)
ax.text(4, 0.5, r"$F=m\ddot{x}$")
fig.tight_layout()
```
