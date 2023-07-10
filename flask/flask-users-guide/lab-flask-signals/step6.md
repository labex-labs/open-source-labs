# Subscribing to a Signal

To subscribe to a signal, use the `connect` method of the signal. Provide a function that should be called when the signal is emitted:

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```


