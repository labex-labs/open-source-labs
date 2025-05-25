# 모델 생성

이 단계에서는 데이터를 저장할 모델을 생성합니다.

```python
def create_model(self):
    types = [float] * self.num_cols
    store = Gtk.ListStore(*types)
    for row in self.data:
        store.append(tuple(row))
    return store
```
