# Personnaliser le tracé

Nous pouvons personnaliser le tracé pour le rendre plus visuellement attrayant. Dans cet exemple, nous allons ajouter un titre, des étiquettes d'axe et changer la couleur du tracé.

```python
# Personnaliser le tracé
ax.set_title('Tracé de trame')
ax.set_xlabel('Étiquette X')
ax.set_ylabel('Étiquette Y')
ax.set_zlabel('Étiquette Z')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='green')
```
