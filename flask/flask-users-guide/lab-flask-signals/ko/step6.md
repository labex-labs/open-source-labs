# 시그널 구독

시그널을 구독하려면 시그널의 `connect` 메서드를 사용합니다. 시그널이 발생했을 때 호출될 함수를 제공합니다.

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```
