# Scikit-learn Libsvm GUI Tutorial

## Introduction

In this tutorial, you will learn how to use Scikit-learn Libsvm GUI, which is a simple graphical frontend for Libsvm mainly intended for didactic purposes. You can create data points by point and click and visualize the decision region induced by different kernels and parameter settings.

## Steps

### Step 1: Install Required Packages

Before getting started, make sure you have the following packages installed:

- matplotlib
- numpy
- tkinter
- scikit-learn

You can install these packages using pip.

### Step 2: Import Required Packages

The first step is to import the required packages for the project.

```python
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg as NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.contour import ContourSet
import sys
import numpy as np
import tkinter as Tk
from sklearn import svm
from sklearn.datasets import dump_svmlight_file
```

### Step 3: Create Model Class

In this step, we will create the Model class which holds the data. It implements the observable in the observer pattern and notifies the registered observers on change event.

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

### Step 4: Create Controller Class

The Controller class is used to control the Model class. It contains methods for fitting the model, adding examples, clearing the data, and refitting the model.

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

### Step 5: Create View Class

The View class is used to display the graphical user interface (GUI) and handle the user's interactions.

```python
class View:
    def __init__(self, root, controller):
        f = Figure()
        ax = f.add_subplot(111)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim((x_min, x_max))
        ax.set_ylim((y_min, y_max))
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas.mpl_connect("button_press_event", self.onclick)
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        self.controllbar = ControllBar(root, controller)
        self.f = f
        self.ax = ax
        self.canvas = canvas
        self.controller = controller
        self.contours = []
        self.c_labels = None
        self.plot_kernels()

    def plot_kernels(self):
        self.ax.text(-50, -60, "Linear: $u^T v$")
        self.ax.text(-20, -60, r"RBF: $\exp (-\gamma \| u-v \|^2)$")
        self.ax.text(10, -60, r"Poly: $(\gamma \, u^T v + r)^d$")

    def onclick(self, event):
        if event.xdata and event.ydata:
            if event.button == 1:
                self.controller.add_example(event.xdata, event.ydata, 1)
            elif event.button == 3:
                self.controller.add_example(event.xdata, event.ydata, -1)

    def update_example(self, model, idx):
        x, y, l = model.data[idx]
        if l == 1:
            color = "w"
        elif l == -1:
            color = "k"
        self.ax.plot([x], [y], "%so" % color, scalex=0.0, scaley=0.0)

    def update(self, event, model):
        if event == "examples_loaded":
            for i in range(len(model.data)):
                self.update_example(model, i)

        if event == "example_added":
            self.update_example(model, -1)

        if event == "clear":
            self.ax.clear()
            self.ax.set_xticks([])
            self.ax.set_yticks([])
            self.contours = []
            self.c_labels = None
            self.plot_kernels()

        if event == "surface":
            self.remove_surface()
            self.plot_support_vectors(model.clf.support_vectors_)
            self.plot_decision_surface(model.surface, model.surface_type)

        self.canvas.draw()

    def remove_surface(self):
        if len(self.contours) > 0:
            for contour in self.contours:
                if isinstance(contour, ContourSet):
                    for lineset in contour.collections:
                        lineset.remove()
                else:
                    contour.remove()
            self.contours = []

    def plot_support_vectors(self, support_vectors):
        cs = self.ax.scatter(
            support_vectors[:, 0],
            support_vectors[:, 1],
            s=80,
            edgecolors="k",
            facecolors="none",
        )
        self.contours.append(cs)

    def plot_decision_surface(self, surface, type):
        X1, X2, Z = surface
        if type == 0:
            levels = [-1.0, 0.0, 1.0]
            linestyles = ["dashed", "solid", "dashed"]
            colors = "k"
            self.contours.append(
                self.ax.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
            )
        elif type == 1:
            self.contours.append(
                self.ax.contourf(
                    X1, X2, Z, 10, cmap=matplotlib.cm.bone, origin="lower", alpha=0.85
                )
            )
            self.contours.append(
                self.ax.contour(X1, X2, Z, [0.0], colors="k", linestyles=["solid"])
            )
        else:
            raise ValueError("surface type unknown")
```

### Step 6: Create ControllBar Class

The ControllBar class is used to control the user inputs and display them on the GUI.

```python
class ControllBar:
    def __init__(self, root, controller):
        fm = Tk.Frame(root)
        kernel_group = Tk.Frame(fm)
        Tk.Radiobutton(
            kernel_group,
            text="Linear",
            variable=controller.kernel,
            value=0,
            command=controller.refit,
        ).pack(anchor=Tk.W)
        Tk.Radiobutton(
            kernel_group,
            text="RBF",
            variable=controller.kernel,
            value=1,
            command=controller.refit,
        ).pack(anchor=Tk.W)
        Tk.Radiobutton(
            kernel_group,
            text="Poly",
            variable=controller.kernel,
            value=2,
            command=controller.refit,
        ).pack(anchor=Tk.W)
        kernel_group.pack(side=Tk.LEFT)

        valbox = Tk.Frame(fm)
        controller.complexity = Tk.StringVar()
        controller.complexity.set("1.0")
        c = Tk.Frame(valbox)
        Tk.Label(c, text="C:", anchor="e", width=7).pack(side=Tk.LEFT)
        Tk.Entry(c, width=6, textvariable=controller.complexity).pack(side=Tk.LEFT)
        c.pack()

        controller.gamma = Tk.StringVar()
        controller.gamma.set("0.01")
        g = Tk.Frame(valbox)
        Tk.Label(g, text="gamma:", anchor="e", width=7).pack(side=Tk.LEFT)
        Tk.Entry(g, width=6, textvariable=controller.gamma).pack(side=Tk.LEFT)
        g.pack()

        controller.degree = Tk.StringVar()
        controller.degree.set("3")
        d = Tk.Frame(valbox)
        Tk.Label(d, text="degree:", anchor="e", width=7).pack(side=Tk.LEFT)
        Tk.Entry(d, width=6, textvariable=controller.degree).pack(side=Tk.LEFT)
        d.pack()

        controller.coef0 = Tk.StringVar()
        controller.coef0.set("0")
        r = Tk.Frame(valbox)
        Tk.Label(r, text="coef0:", anchor="e", width=7).pack(side=Tk.LEFT)
        Tk.Entry(r, width=6, textvariable=controller.coef0).pack(side=Tk.LEFT)
        r.pack()
        valbox.pack(side=Tk.LEFT)

        cmap_group = Tk.Frame(fm)
        Tk.Radiobutton(
            cmap_group,
            text="Hyperplanes",
            variable=controller.surface_type,
            value=0,
            command=controller.refit,
        ).pack(anchor=Tk.W)
        Tk.Radiobutton(
            cmap_group,
            text="Surface",
            variable=controller.surface_type,
            value=1,
            command=controller.refit,
        ).pack(anchor=Tk.W)

        cmap_group.pack(side=Tk.LEFT)

        train_button = Tk.Button(fm, text="Fit", width=5, command=controller.fit)
        train_button.pack()
        fm.pack(side=Tk.LEFT)
        Tk.Button(fm, text="Clear", width=5, command=controller.clear_data).pack(
            side=Tk.LEFT
        )
```

### Step 7: Create main Function

The main function is used to run the program.

```python
def main(argv):
    root = Tk.Tk()
    model = Model()
    controller = Controller(model)
    root.wm_title("Scikit-learn Libsvm GUI")
    view = View(root, controller)
    model.add_observer(view)
    Tk.mainloop()
```

### Step 8: Run the Program

Now you can run the program by calling the main function.

```python
if __name__ == "__main__":
    main(sys.argv)
```

## Summary

In this tutorial, you learned how to use Scikit-learn Libsvm GUI to create data points by point and click and visualize the decision region induced by different kernels and parameter settings. You also learned how to create the Model, Controller, View, and ControllBar classes, as well as how to run the program.
