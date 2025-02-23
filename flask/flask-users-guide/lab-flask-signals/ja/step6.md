# シグナルの購読

シグナルを購読するには、シグナルの `connect` メソッドを使用します。シグナルが発行されたときに呼び出される関数を提供します。

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```
