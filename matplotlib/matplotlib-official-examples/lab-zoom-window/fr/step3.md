# Connecter l'événement à la fonction

Maintenant, nous connectons l'événement de pression de bouton dans la première fenêtre à la fonction on_press que nous venons de définir.

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
