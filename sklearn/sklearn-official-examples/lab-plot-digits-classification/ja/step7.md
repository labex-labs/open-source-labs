# 混同行列から分類レポートを再構築する

分類器の評価結果が混同行列の形式で保存されており、`y_true` と `y_pred` の形式ではない場合でも、`metrics.classification_report()` メソッドを使用して以下のように分類レポートを作成することができます。

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "Classification report rebuilt from confusion matrix:\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```
