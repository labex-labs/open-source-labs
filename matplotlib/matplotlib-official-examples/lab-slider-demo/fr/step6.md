# Enregistrer la fonction de mise à jour avec les curseurs

Ensuite, nous enregistrerons la fonction de mise à jour avec chaque curseur de sorte que la fonction soit appelée chaque fois que nous ajustons les curseurs.

```python
freq_slider.on_changed(update)
amp_slider.on_changed(update)
```
