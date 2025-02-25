# Créer le widget de zone de texte

Nous créons le widget de zone de texte et l'ajoutons à la figure. La méthode `on_submit` est utilisée pour déclencher la fonction `submit` lorsque l'utilisateur appuie sur Entrée dans la zone de texte ou quitte la zone de texte. Nous définissons également la valeur initiale du widget de zone de texte sur `t ** 2`.

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
