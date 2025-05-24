# Inscrevendo-se em um Sinal

Para se inscrever em um sinal, use o método `connect` do sinal. Forneça uma função que deve ser chamada quando o sinal for emitido:

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```
