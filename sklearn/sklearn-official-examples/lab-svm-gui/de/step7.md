# Erstellen Sie die Hauptfunktion

Die Hauptfunktion wird verwendet, um das Programm auszuführen.

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
