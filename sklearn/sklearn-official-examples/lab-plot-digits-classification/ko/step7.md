# 혼동 행렬로부터 분류 보고서 재구성

분류기 평가 결과가 혼동 행렬 형태로 저장되어 있고 `y_true` 및 `y_pred` 값이 아닌 경우에도 `metrics.classification_report()` 메서드를 사용하여 분류 보고서를 생성할 수 있습니다.

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "혼동 행렬로부터 재구성된 분류 보고서:\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```
