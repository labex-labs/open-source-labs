# Tracer la figure de démonstration pour chaque feuille de style

Enfin, vous devez tracer la figure de démonstration pour chaque feuille de style disponible. Vous pouvez le faire en parcourant la liste `style_list` et en appelant la fonction `plot_figure()` pour chaque feuille de style.

```python
if __name__ == "__main__":

    # Configurez une liste de tous les styles disponibles, dans l'ordre alphabétique, mais
    # les styles `default` et `classic`, qui seront forcés respectivement en
    # première et deuxième position.
    # Les styles commençant par un underscore sont destinés à une utilisation interne, telle que les tests
    # et la galerie de types de tracé. Ils sont exclus ici.
    style_list = ['default', 'classic'] + sorted(
        style for style in plt.style.available
        if style!= 'classic' and not style.startswith('_'))

    # Tracez une figure de démonstration pour chaque feuille de style disponible.
    for style_label in style_list:
        with plt.rc_context({"figure.max_open_warning": len(style_list)}):
            with plt.style.context(style_label):
                plot_figure(style_label=style_label)

    plt.show()
```
