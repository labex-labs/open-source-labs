# 可视化结果

最后，我们可以将预测值与实际值进行绘图，以直观展示模型对数据的拟合程度。

```python
import matplotlib.pyplot as plt

# 绘制输出
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```
