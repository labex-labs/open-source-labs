# Run the Application

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
