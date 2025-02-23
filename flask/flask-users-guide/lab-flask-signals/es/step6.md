# Suscribiéndose a una Señal

Para suscribirse a una señal, utilice el método `connect` de la señal. Proporcione una función que debe ser llamada cuando la señal se emite:

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```
