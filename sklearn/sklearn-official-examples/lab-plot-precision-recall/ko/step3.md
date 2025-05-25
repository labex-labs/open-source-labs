# 다중 레이블 분류를 위한 정밀도 - 재현율 곡선 플롯

정밀도 - 재현율 곡선은 다중 레이블 설정을 지원하지 않습니다. 그러나 이 경우를 처리하는 방법을 결정할 수 있습니다. 다중 레이블 데이터셋을 생성하고, OneVsRestClassifier 를 사용하여 학습 및 예측한 후 정밀도 - 재현율 곡선을 플롯합니다.

```python
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score

# 다중 레이블 데이터 생성
Y = label_binarize(y, classes=[0, 1, 2])
n_classes = Y.shape[1]
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.5, random_state=random_state
)

# OneVsRestClassifier 를 사용하여 학습 및 예측
classifier = OneVsRestClassifier(
    make_pipeline(StandardScaler(), LinearSVC(random_state=random_state, dual="auto"))
)
classifier.fit(X_train, Y_train)
y_score = classifier.decision_function(X_test)

# 각 클래스에 대한 정밀도와 재현율 계산
precision = dict()
recall = dict()
average_precision = dict()
for i in range(n_classes):
    precision[i], recall[i], _ = precision_recall_curve(Y_test[:, i], y_score[:, i])
    average_precision[i] = average_precision_score(Y_test[:, i], y_score[:, i])

# 마이크로 평균 정밀도와 재현율 계산
precision["micro"], recall["micro"], _ = precision_recall_curve(Y_test.ravel(), y_score.ravel())
average_precision["micro"] = average_precision_score(Y_test, y_score, average="micro")

# 마이크로 평균 정밀도 - 재현율 곡선 플롯
display = PrecisionRecallDisplay(
    recall=recall["micro"],
    precision=precision["micro"],
    average_precision=average_precision["micro"],
    prevalence_pos_label=Counter(Y_test.ravel())[1] / Y_test.size,
)
display.plot(plot_chance_level=True)
_ = display.ax_.set_title("모든 클래스에 대한 마이크로 평균")

# 각 클래스의 정밀도 - 재현율 곡선 및 등-F1 곡선 플롯
colors = cycle(["navy", "turquoise", "darkorange", "cornflowerblue", "teal"])
_, ax = plt.subplots(figsize=(7, 8))
f_scores = np.linspace(0.2, 0.8, num=4)
lines, labels = [], []
for f_score in f_scores:
    x = np.linspace(0.01, 1)
    y = f_score * x / (2 * x - f_score)
    (l,) = plt.plot(x[y >= 0], y[y >= 0], color="gray", alpha=0.2)
    plt.annotate("f1={0:0.1f}".format(f_score), xy=(0.9, y[45] + 0.02))

display = PrecisionRecallDisplay(
    recall=recall["micro"],
    precision=precision["micro"],
    average_precision=average_precision["micro"],
)
display.plot(ax=ax, name="마이크로 평균 정밀도 - 재현율", color="gold")

for i, color in zip(range(n_classes), colors):
    display = PrecisionRecallDisplay(
        recall=recall[i],
        precision=precision[i],
        average_precision=average_precision[i],
    )
    display.plot(ax=ax, name=f"클래스 {i}의 정밀도 - 재현율", color=color)

handles, labels = display.ax_.get_legend_handles_labels()
handles.extend([l])
labels.extend(["등-F1 곡선"])
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.legend(handles=handles, labels=labels, loc="best")
ax.set_title("다중 클래스로 확장된 정밀도 - 재현율 곡선")
plt.show()
```
