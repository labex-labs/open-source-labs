# 保存绘图

你可以使用 `savefig` 方法将绘图保存为图像文件。以下代码将绘图保存为PNG图像：

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.savefig('simple_plot.png')
```
