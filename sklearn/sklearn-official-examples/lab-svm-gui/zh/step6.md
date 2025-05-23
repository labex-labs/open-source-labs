# 创建控制栏类

控制栏类用于控制用户输入并在图形用户界面（GUI）上显示这些输入。

```python
class ControllBar:
    def __init__(self, root, controller):
        fm = Tk.Frame(root)
        kernel_group = Tk.Frame(fm)
        Tk.Radiobutton(
            kernel_group,
            text="线性",
            variable=controller.kernel,
            value=0,
            command=controller.refit,
        ).pack(anchor=Tk.W)
        Tk.Radiobutton(
            kernel_group,
            text="径向基函数（RBF）",
            variable=controller.kernel,
            value=1,
            command=controller.refit,
        ).pack(anchor=Tk.W)
        Tk.Radiobutton(
            kernel_group,
            text="多项式",
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
            text="超平面",
            variable=controller.surface_type,
            value=0,
            command=controller.refit,
        ).pack(anchor=Tk.W)
        Tk.Radiobutton(
            cmap_group,
            text="曲面",
            variable=controller.surface_type,
            value=1,
            command=controller.refit,
        ).pack(anchor=Tk.W)

        cmap_group.pack(side=Tk.LEFT)

        train_button = Tk.Button(fm, text="拟合", width=5, command=controller.fit)
        train_button.pack()
        fm.pack(side=Tk.LEFT)
        Tk.Button(fm, text="清除", width=5, command=controller.clear_data).pack(
            side=Tk.LEFT
        )
```
