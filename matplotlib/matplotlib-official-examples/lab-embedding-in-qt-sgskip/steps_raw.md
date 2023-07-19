# Python Matplotlib Lab

## Introduction

In this lab, you will learn how to embed Matplotlib canvases in a simple Qt application using any Qt binding (PyQt6, PySide6, PyQt5, PySide2). This program will work equally well using any Qt binding and can be selected by setting the `QT_API` environment variable to the binding name or by first importing it.

## Steps

### Step 1: Create a Qt Application Window

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

### Step 2: Plot a Static Graph

In this step, we plot a static graph using `subplots()` method of `FigureCanvas` object. Then, we create a numpy array using `linspace()` method and plot it using `plot()` method of `subplots()` object.

```python
self._static_ax = static_canvas.figure.subplots()
t = np.linspace(0, 10, 501)
self._static_ax.plot(t, np.tan(t), ".")
```

### Step 3: Plot a Dynamic Graph

In this step, we plot a dynamic graph using `subplots()` method of `FigureCanvas` object. Then, we create a numpy array using `linspace()` method and plot it using `plot()` method of `subplots()` object.

```python
self._dynamic_ax = dynamic_canvas.figure.subplots()
t = np.linspace(0, 10, 101)
self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
```

### Step 4: Update the Dynamic Graph

In this step, we update the dynamic graph using a timer. We create a new timer object with a callback function `_update_canvas()`. The callback function updates the data of the graph using `set_data()` method of `Line2D` object and redraws the graph using `draw()` method of `FigureCanvas` object.

```python
self._timer = dynamic_canvas.new_timer(50)
self._timer.add_callback(self._update_canvas)
self._timer.start()

def _update_canvas(self):
    t = np.linspace(0, 10, 101)
    self._line.set_data(t, np.sin(t + time.time()))
    self._line.figure.canvas.draw()
```

### Step 5: Run the Application

In this step, we create a new `QApplication` object and check whether there is already a running `QApplication` (e.g., if running from an IDE). Then, we create a new `ApplicationWindow` object and show it using `show()` method.

```python
if __name__ == "__main__":
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    qapp.exec()
```

## Summary

In this lab, you learned how to embed Matplotlib canvases in a simple Qt application using any Qt binding. You learned how to create a Qt application window with a main widget and a vertical layout, plot static and dynamic graphs using `FigureCanvas` object, and update the dynamic graph using a timer. You also learned how to create a new `QApplication` object and show the `ApplicationWindow` object.
