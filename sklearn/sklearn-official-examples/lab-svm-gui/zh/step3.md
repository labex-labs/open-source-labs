# 创建模型类

在这一步中，我们将创建一个用于保存数据的模型类。它实现了观察者模式中的可观察对象，并在发生更改事件时通知已注册的观察者。

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
