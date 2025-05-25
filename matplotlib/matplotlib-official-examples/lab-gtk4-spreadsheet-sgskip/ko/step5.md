# 모델 생성

마지막으로, 데이터를 저장할 모델을 생성해야 합니다.

```python
    def create_model(self):
        types = [float] * self.num_cols
        store = Gtk.ListStore(*types)
        for row in self.data:
            it = store.insert(-1)
            store.set(it, {i: val for i, val in enumerate(row)})
        return store
```
