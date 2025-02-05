# 归一化数据

为了创建曼德勃罗集的阴影和功率归一化渲染图，我们需要对数据进行归一化。我们将使用以下公式来完成此操作：

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```
