# 메인 함수 생성

메인 함수는 프로그램을 실행하는 데 사용됩니다.

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
