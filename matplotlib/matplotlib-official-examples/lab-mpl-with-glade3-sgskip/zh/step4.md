# 定义主函数

接下来，定义 `main()` 函数。此函数将创建用户界面、创建图表并显示窗口。

```python
def main():
    builder = Gtk.Builder()
    builder.add_objects_from_file(
        str(Path(__file__).parent / "mpl_with_glade3.glade"),
        ("window1", ""))
    builder.connect_signals(Window1Signals())
    window = builder.get_object("window1")
    sw = builder.get_object("scrolledwindow1")

    # 开始 Matplotlib 特定代码
    figure = Figure(figsize=(8, 6), dpi=71)
    axis = figure.add_subplot()
    t = np.arange(0.0, 3.0, 0.01)
    s = np.sin(2*np.pi*t)
    axis.plot(t, s)

    axis.set_xlabel('time [s]')
    axis.set_ylabel('voltage [V]')

    canvas = FigureCanvas(figure)  # 一个 Gtk.DrawingArea
    canvas.set_size_request(800, 600)
    sw.add(canvas)
    # 结束 Matplotlib 特定代码

    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
```
