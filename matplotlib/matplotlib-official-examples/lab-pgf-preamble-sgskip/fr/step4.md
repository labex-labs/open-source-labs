# Personnaliser le graphique

Vous pouvez personnaliser le graphique en changeant les couleurs, les styles de ligne et les marqueurs. Voici un exemple :

```python
plt.plot(x, y1, 'r--', label='sin')
plt.plot(x, y2, 'g:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fonctions sinus et cosinus')
plt.legend()
plt.show()
```
