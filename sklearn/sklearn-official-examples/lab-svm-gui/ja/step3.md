# モデルクラスを作成する

このステップでは、データを保持する Model クラスを作成します。これは、オブザーバーパターンにおけるオブザーバ可能なものを実装し、変更イベントが発生したときに登録されたオブザーバーに通知します。

```python
class Model:
    def __init__(self):
        self.observers = []
        self.surface = None
        self.data = []
        self.cls = None
        self.surface_type = 0

    def changed(self, event):
        for observer in self.observers:
            observer.update(event, self)

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_surface(self, surface):
        self.surface = surface

    def dump_svmlight_file(self, file):
        data = np.array(self.data)
        X = data[:, 0:2]
        y = data[:, 2]
        dump_svmlight_file(X, y, file)
```
