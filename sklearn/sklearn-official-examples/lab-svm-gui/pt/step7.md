# Criar a Função Principal

A função principal é usada para executar o programa.

```python
def main(argv):
    root = Tk.Tk()
    model = Model()
    controller = Controller(model)
    root.wm_title("GUI Libsvm do Scikit-learn")
    view = View(root, controller)
    model.add_observer(view)
    Tk.mainloop()
```
