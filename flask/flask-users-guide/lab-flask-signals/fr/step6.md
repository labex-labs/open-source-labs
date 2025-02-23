# S'abonner à un signal

Pour vous abonner à un signal, utilisez la méthode `connect` du signal. Fournissez une fonction qui doit être appelée lorsque le signal est émis :

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```
