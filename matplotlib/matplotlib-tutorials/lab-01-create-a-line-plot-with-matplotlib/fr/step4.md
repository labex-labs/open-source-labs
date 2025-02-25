# Personnalisez le tracé

Nous pouvons personnaliser le tracé en ajoutant des étiquettes aux axes x et y, un titre au tracé et une légende. Nous pouvons également changer le style et la couleur de la ligne.

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```
