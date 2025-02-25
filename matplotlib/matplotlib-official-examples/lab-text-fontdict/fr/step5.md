# Ajoutez du texte au tracé

Nous pouvons ajouter du texte à notre tracé en utilisant la fonction text(). Dans cet exemple, nous allons ajouter une expression LaTeX au tracé en utilisant le dictionnaire de police pour personnaliser le style.

```python
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
```
