# One-vs-Rest 다중 클래스 ROC

One-vs-the-Rest (OvR) 다중 클래스 전략은 각 `n_classes`에 대해 ROC 곡선을 계산하는 방식입니다. 각 단계에서 특정 클래스를 양성 클래스로 간주하고 나머지 클래스를 대량으로 음성 클래스로 간주합니다. 이 단계에서는 OvR 다중 클래스 전략을 사용하여 ROC 곡선을 계산하는 방법을 보여줍니다.

```python
from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

# OvR 전략을 사용하여 타겟을 이진화
label_binarizer = LabelBinarizer().fit(y_train)
y_onehot_test = label_binarizer.transform(y_test)

# 로지스틱 회귀 모델 학습
classifier = LogisticRegression()
y_score = classifier.fit(X_train, y_train).predict_proba(X_test)

# 각 클래스에 대한 ROC 곡선 및 ROC AUC 점수 계산
fpr, tpr, roc_auc = dict(), dict(), dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_onehot_test[:, i], y_score[:, i])
    roc_auc[i] = roc_auc_score(y_onehot_test[:, i], y_score[:, i])

# 마이크로 평균 ROC 곡선 및 ROC 면적 계산
fpr["micro"], tpr["micro"], _ = roc_curve(y_onehot_test.ravel(), y_score.ravel())
roc_auc["micro"] = roc_auc_score(y_onehot_test, y_score, multi_class="ovr", average="micro")

# 매크로 평균 ROC 곡선 및 ROC 면적 계산
# 각 클래스의 참/거짓 양성률 집계
fpr["macro"], tpr["macro"] = [], []
for i in range(n_classes):
    fpr_averaged, tpr_averaged = [], []
    for j in range(n_classes):
        if i != j:
            fpr_averaged += list(fpr[j])
            tpr_averaged += list(tpr[j])
    fpr_averaged = np.array(fpr_averaged)
    tpr_averaged = np.array(tpr_averaged)
    fpr["macro"].append(fpr_averaged)
    tpr["macro"].append(tpr_averaged)
fpr["macro"] = np.concatenate(fpr["macro"])
tpr["macro"] = np.concatenate(tpr["macro"])
roc_auc["macro"] = roc_auc_score(y_onehot_test, y_score, multi_class="ovr", average="macro")

# 각 클래스 및 마이크로/매크로 평균에 대한 ROC 곡선 플롯
fig, ax = plt.subplots(figsize=(6, 6))
colors = ["aqua", "darkorange", "cornflowerblue"]
for i, color in zip(range(n_classes), colors):
    RocCurveDisplay.from_predictions(
        y_onehot_test[:, i],
        y_score[:, i],
        name=f"ROC curve of class {target_names[i]} (AUC = {roc_auc[i]:.2f})",
        color=color,
        ax=ax,
        plot_micro=False,
        plot_macro=False,
    )

RocCurveDisplay.from_predictions(
    y_onehot_test.ravel(),
    y_score.ravel(),
    name=f"Micro-average ROC curve (AUC = {roc_auc['micro']:.2f})",
    color="deeppink",
    linestyle=":",
    linewidth=4,
    ax=ax,
)

plt.plot(
    fpr["macro"],
    tpr["macro"],
    label=f"Macro-average ROC curve (AUC = {roc_auc['macro']:.2f})",
    color="navy",
    linestyle=":",
    linewidth=4,
)

plt.plot([0, 1], [0, 1], "k--", label="Chance level")
plt.axis("square")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("One-vs-Rest ROC curves")
plt.legend()
plt.show()
```
