# 绘制单变量特征得分

我们可以绘制每个特征的单变量得分，以查看哪些特征是显著的。

```python
import matplotlib.pyplot as plt

X_indices = np.arange(X.shape[-1])
plt.figure(1)
plt.clf()
plt.bar(X_indices - 0.05, scores, width=0.2)
plt.title("特征单变量得分")
plt.xlabel("特征编号")
plt.ylabel(r"单变量得分（$-Log(p_{值})$）")
plt.show()
```
