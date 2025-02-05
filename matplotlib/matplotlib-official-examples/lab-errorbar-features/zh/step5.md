# 绘制变量及不对称误差线

接下来，我们将绘制带有可变不对称误差线的数据。同样使用`ax.errorbar()`函数，但这次使用`xerr`参数来指定不对称误差值。

```python
# 绘制变量及不对称误差线
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
