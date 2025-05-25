# 혼동 행렬 시각화

matplotlib 을 사용하여 혼동 행렬을 시각화할 것입니다. 정규화되지 않은 혼동 행렬과 정규화된 혼동 행렬을 모두 플롯할 것입니다.

```python
titles_options = [
    ("정규화되지 않은 혼동 행렬", None),
    ("정규화된 혼동 행렬", "true"),
]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        X_test,
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)
plt.show()
```
