# 对数损失比较

我们比较未校准和校准后的分类器在 1000 个测试样本预测结果上的对数损失。

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("对数损失为")
print(f" * 未校准分类器：{score:.3f}")
print(f" * 校准后分类器：{cal_score:.3f}")
```
