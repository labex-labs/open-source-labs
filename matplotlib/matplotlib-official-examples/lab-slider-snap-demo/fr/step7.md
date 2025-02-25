# Connecter les curseurs à la fonction de mise à jour

Dans cette étape, vous allez connecter les curseurs à la fonction de mise à jour. Cela garantira que le tracé est mis à jour chaque fois que les valeurs des curseurs sont modifiées.

```python
sfreq.on_changed(update)
samp.on_changed(update)
```
