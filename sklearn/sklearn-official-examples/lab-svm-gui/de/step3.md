# Erstellen Sie die Modellklasse

In diesem Schritt werden wir die Modellklasse erstellen, die die Daten enthält. Sie implementiert das Beobachterobjekt im Beobachtermuster und benachrichtigt die registrierten Beobachter bei einem Änderungsereignis.

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
