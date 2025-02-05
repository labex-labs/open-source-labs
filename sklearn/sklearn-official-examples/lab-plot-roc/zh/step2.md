# 一对多多类ROC

一对其余（One-vs-the-Rest，OvR）多类策略包括为每个 `n_classes` 计算一条ROC曲线。在每一步中，将给定的类视为正类，其余类作为一个整体视为负类。在这一步中，我们展示如何使用OvR多类策略计算ROC曲线。

```python
from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

# 使用OvR策略对目标进行二值化
label_binarizer = LabelBinarizer().fit(y_train)
y_onehot_test = label_binarizer.transform(y_test)

# 训练逻辑回归模型
classifier = LogisticRegression()
y_score = classifier.fit(X_train, y_train).predict_proba(X_test)

# 计算每个类别的ROC曲线和ROC AUC分数
fpr, tpr, roc_auc = dict(), dict(), dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_onehot_test[:, i], y_score[:, i])
    roc_auc[i] = roc_auc_score(y_onehot_test[:, i], y_score[:, i])

# 计算微平均ROC曲线和ROC面积
fpr["micro"], tpr["micro"], _ = roc_curve(y_onehot_test.ravel(), y_score.ravel())
roc_auc["micro"] = roc_auc_score(y_onehot_test, y_score, multi_class="ovr", average="micro")

# 计算宏平均ROC曲线和ROC面积
# 汇总每个类别的真/假阳性率
fpr["macro"], tpr["macro"] = [], []
for i in range(n_classes):
    fpr_averaged, tpr_averaged = [], []
    for j in range(n_classes):
        if i!= j:
            fpr_averaged += list(fpr[j])
            tpr_averaged += list(tpr[j])
    fpr_averaged = np.array(fpr_averaged)
    tpr_averaged = np.array(tpr_averaged)
    fpr["macro"].append(fpr_averaged)
    tpr["macro"].append(tpr_averaged)
fpr["macro"] = np.concatenate(fpr["macro"])
tpr["macro"] = np.concatenate(tpr["macro"])
roc_auc["macro"] = roc_auc_score(y_onehot_test, y_score, multi_class="ovr", average="macro")

# 绘制每个类别的ROC曲线以及微/宏平均值
fig, ax = plt.subplots(figsize=(6, 6))
colors = ["aqua", "darkorange", "cornflowerblue"]
for i, color in zip(range(n_classes), colors):
    RocCurveDisplay.from_predictions(
        y_onehot_test[:, i],
        y_score[:, i],
        name=f"ROC曲线 of class {target_names[i]} (AUC = {roc_auc[i]:.2f})",
        color=color,
        ax=ax,
        plot_micro=False,
        plot_macro=False,
    )

RocCurveDisplay.from_predictions(
    y_onehot_test.ravel(),
    y_score.ravel(),
    name=f"微平均ROC曲线 (AUC = {roc_auc['micro']:.2f})",
    color="deeppink",
    linestyle=":",
    linewidth=4,
    ax=ax,
)

plt.plot(
    fpr["macro"],
    tpr["macro"],
    label=f"宏平均ROC曲线 (AUC = {roc_auc['macro']:.2f})",
    color="navy",
    linestyle=":",
    linewidth=4,
)

plt.plot([0, 1], [0, 1], "k--", label="随机水平")
plt.axis("square")
plt.xlabel("假阳性率")
plt.ylabel("真阳性率")
plt.title("一对多ROC曲线")
plt.legend()
plt.show()
```
