# 显示图像

使用以下代码显示最终图像：

```python
ax1.imshow([[0, 1, 2], [1, 2, 3]], cmap=plt.cm.gist_gray_r,
               interpolation="bilinear", aspect="auto")
plt.show()
```
