# Ajout de texte

Dans cette étape, nous allons ajouter du texte au tracé à l'aide de la fonction `text()`.

```python
tex = r'$\mathcal{R}\prod_{i=\alpha_{i+1}}^\infty a_i\sin(2 \pi f x_i)$'
ax.text(1, 1.6, tex, fontsize=20, va='bottom')
```
