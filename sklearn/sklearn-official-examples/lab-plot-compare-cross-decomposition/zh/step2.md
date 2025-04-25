# 典型偏最小二乘法

我们使用偏最小二乘典型相关分析（PLS Canonical）算法对数据进行变换。然后，我们创建得分的散点图。

```python
from sklearn.cross_decomposition import PLSCanonical

plsca = PLSCanonical(n_components=2)
plsca.fit(X_train, Y_train)
X_train_r, Y_train_r = plsca.transform(X_train, Y_train)
X_test_r, Y_test_r = plsca.transform(X_test, Y_test)

import matplotlib.pyplot as plt

# 在对角线上绘制每个成分上 X 与 Y 的得分
plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.scatter(X_train_r[:, 0], Y_train_r[:, 0], label="train", marker="o", s=25)
plt.scatter(X_test_r[:, 0], Y_test_r[:, 0], label="test", marker="o", s=25)
plt.xlabel("x 得分")
plt.ylabel("y 得分")
plt.title(
    "成分 1：X 与 Y（测试集相关性 = %.2f）"
    % np.corrcoef(X_test_r[:, 0], Y_test_r[:, 0])[0, 1]
)
plt.xticks(())
plt.yticks(())
plt.legend(loc="最佳位置")

plt.subplot(224)
plt.scatter(X_train_r[:, 1], Y_train_r[:, 1], label="train", marker="o", s=25)
plt.scatter(X_test_r[:, 1], Y_test_r[:, 1], label="test", marker="o", s=25)
plt.xlabel("x 得分")
plt.ylabel("y 得分")
plt.title(
    "成分 2：X 与 Y（测试集相关性 = %.2f）"
    % np.corrcoef(X_test_r[:, 1], Y_test_r[:, 1])[0, 1]
)
plt.xticks(())
plt.yticks(())
plt.legend(loc="最佳位置")

# 在非对角线上绘制 X 和 Y 的成分 1 与成分 2
plt.subplot(222)
plt.scatter(X_train_r[:, 0], X_train_r[:, 1], label="train", marker="*", s=50)
plt.scatter(X_test_r[:, 0], X_test_r[:, 1], label="test", marker="*", s=50)
plt.xlabel("X 成分 1")
plt.ylabel("X 成分 2")
plt.title(
    "X 成分 1 与 X 成分 2（测试集相关性 = %.2f）"
    % np.corrcoef(X_test_r[:, 0], X_test_r[:, 1])[0, 1]
)
plt.legend(loc="最佳位置")
plt.xticks(())
plt.yticks(())

plt.subplot(223)
plt.scatter(Y_train_r[:, 0], Y_train_r[:, 1], label="train", marker="*", s=50)
plt.scatter(Y_test_r[:, 0], Y_test_r[:, 1], label="test", marker="*", s=50)
plt.xlabel("Y 成分 1")
plt.ylabel("Y 成分 2")
plt.title(
    "Y 成分 1 与 Y 成分 2，（测试集相关性 = %.2f）"
    % np.corrcoef(Y_test_r[:, 0], Y_test_r[:, 1])[0, 1]
)
plt.legend(loc="最佳位置")
plt.xticks(())
plt.yticks(())
plt.show()
```
