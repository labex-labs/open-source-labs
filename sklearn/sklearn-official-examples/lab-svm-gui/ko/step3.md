# 모델 클래스 생성

이 단계에서는 데이터를 저장하는 Model 클래스를 생성합니다. 이 클래스는 관찰자 패턴의 관찰자를 구현하며, 변경 이벤트가 발생하면 등록된 관찰자에게 알립니다.

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
