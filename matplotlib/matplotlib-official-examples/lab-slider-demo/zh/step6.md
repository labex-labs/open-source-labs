# 将更新函数与滑块关联

接下来，我们会将更新函数与每个滑块进行关联，这样每次调整滑块时都会调用该函数。

```python
freq_slider.on_changed(update)
amp_slider.on_changed(update)
```
