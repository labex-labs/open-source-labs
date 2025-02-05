# 定义振幅滑块的允许值

在这一步中，你将定义振幅滑块的允许值。振幅滑块将使用这些值来捕捉到最接近的允许值。

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```
