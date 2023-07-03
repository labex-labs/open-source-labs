# Update the Counter

We will create a method `OnBang` that updates the counter when the "Bang" button is clicked.

```python
    def OnBang(self, event):
        bang_count = xrc.XRCCTRL(self.frame, "bang_count")
        bangs = bang_count.GetValue()
        bangs = int(bangs) + 1
        bang_count.SetValue(str(bangs))
```
