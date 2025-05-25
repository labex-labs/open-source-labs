# Criar a Classe Visualização

A classe Visualização é usada para exibir a interface gráfica do usuário (GUI) e lidar com as interações do usuário.

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
            raise ValueError("tipo de superfície desconhecido")
```
