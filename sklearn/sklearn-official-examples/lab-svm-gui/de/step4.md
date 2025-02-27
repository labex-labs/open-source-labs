# Erstellen Sie die Steuerelementklasse

Die Steuerelementklasse wird verwendet, um die Modellklasse zu steuern. Sie enthält Methoden zum Anpassen des Modells, Hinzufügen von Beispielen, Löschen der Daten und erneuten Anpassen des Modells.

```python
class Controller:
    def __init__(self, model):
        self.model = model
        self.kernel = Tk.IntVar()
        self.surface_type = Tk.IntVar()
        self.fitted = False

    def fit(self):
        train = np.array(self.model.data)
        X = train[:, 0:2]
        y = train[:, 2]
        C = float(self.complexity.get())
        gamma = float(self.gamma.get())
        coef0 = float(self.coef0.get())
        degree = int(self.degree.get())
        kernel_map = {0: "linear", 1: "rbf", 2: "poly"}
        if len(np.unique(y)) == 1:
            clf = svm.OneClassSVM(
                kernel=kernel_map[self.kernel.get()],
                gamma=gamma,
                coef0=coef0,
                degree=degree,
            )
            clf.fit(X)
        else:
            clf = svm.SVC(
                kernel=kernel_map[self.kernel.get()],
                C=C,
                gamma=gamma,
                coef0=coef0,
                degree=degree,
            )
            clf.fit(X, y)
        if hasattr(clf, "score"):
            print("Accuracy:", clf.score(X, y) * 100)
        X1, X2, Z = self.decision_surface(clf)
        self.model.clf = clf
        self.model.set_surface((X1, X2, Z))
        self.model.surface_type = self.surface_type.get()
        self.fitted = True
        self.model.changed("surface")

    def decision_surface(self, cls):
        delta = 1
        x = np.arange(x_min, x_max + delta, delta)
        y = np.arange(y_min, y_max + delta, delta)
        X1, X2 = np.meshgrid(x, y)
        Z = cls.decision_function(np.c_[X1.ravel(), X2.ravel()])
        Z = Z.reshape(X1.shape)
        return X1, X2, Z

    def clear_data(self):
        self.model.data = []
        self.fitted = False
        self.model.changed("clear")

    def add_example(self, x, y, label):
        self.model.data.append((x, y, label))
        self.model.changed("example_added")
        self.refit()

    def refit(self):
        if self.fitted:
            self.fit()
```
