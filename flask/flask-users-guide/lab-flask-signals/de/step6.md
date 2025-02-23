# Abonnieren eines Signals

Um sich einem Signal abonnieren zu können, verwenden Sie die `connect`-Methode des Signals. Geben Sie eine Funktion an, die aufgerufen werden soll, wenn das Signal ausgelöst wird:

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```
