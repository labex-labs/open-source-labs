# 메인 함수 정의

다음으로, `main()` 함수를 정의합니다. 이 함수는 사용자 인터페이스를 생성하고, 그래프를 생성하며, 창을 표시합니다.

```python
def main():
    builder = Gtk.Builder()
    builder.add_objects_from_file(
        str(Path(__file__).parent / "mpl_with_glade3.glade"),
        ("window1", ""))
    builder.connect_signals(Window1Signals())
    window = builder.get_object("window1")
    sw = builder.get_object("scrolledwindow1")

    # Start of Matplotlib specific code
    figure = Figure(figsize=(8, 6), dpi=71)
    axis = figure.add_subplot()
    t = np.arange(0.0, 3.0, 0.01)
    s = np.sin(2*np.pi*t)
    axis.plot(t, s)

    axis.set_xlabel('time [s]')
    axis.set_ylabel('voltage [V]')

    canvas = FigureCanvas(figure)  # a Gtk.DrawingArea
    canvas.set_size_request(800, 600)
    sw.add(canvas)
    # End of Matplotlib specific code

    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
```
