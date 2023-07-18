# Create a Qt Application Window

The first step is to create a Qt application window with a main widget and a vertical layout using the `QtWidgets` module. Then, we create two `FigureCanvas` objects with different sizes and add them to the layout. Finally, we add `NavigationToolbar` to both `FigureCanvas` objects.

```python
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(NavigationToolbar(static_canvas, self))
        layout.addWidget(static_canvas)

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)
        layout.addWidget(NavigationToolbar(dynamic_canvas, self))
```
