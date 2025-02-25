# Formatage simple

Dans cette étape, nous allons montrer comment utiliser un formatteur simple en passant une chaîne de caractères ou une fonction à `~.Axis.set_major_formatter` ou `~.Axis.set_minor_formatter`. Nous allons créer deux tracés, l'un utilisant un formatteur de chaîne de caractères et l'autre un formatteur de fonction.

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Formatage simple')

# Une chaîne de caractères (`str`), en utilisant la syntaxe de la fonction de chaîne de formatage, peut être utilisée directement comme formatteur.
# La variable `x` est la valeur de l'étiquette et la variable `pos` est la position de l'étiquette.
# Cela crée automatiquement un StrMethodFormatter.
setup(axs0[0], titre="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# Une fonction peut également être utilisée directement comme formatteur.
# La fonction doit prendre deux arguments : `x` pour la valeur de l'étiquette et `pos` pour la position de l'étiquette,
# et doit renvoyer une chaîne de caractères (`str`).
# Cela crée automatiquement un FuncFormatter.
setup(axs0[1], titre="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```
