# Подписка на сигнал

Для подписки на сигнал используйте метод `connect` сигнала. Предоставьте функцию, которая должна вызываться при отправке сигнала:

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```
