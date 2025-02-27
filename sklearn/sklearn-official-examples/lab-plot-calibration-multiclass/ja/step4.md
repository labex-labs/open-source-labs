# ログ損失の比較

1000 個のテスト サンプルの予測に対する、補正前と補正済みの分類器のログ損失を比較します。

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("Log-loss of")
print(f" * uncalibrated classifier: {score:.3f}")
print(f" * calibrated classifier: {cal_score:.3f}")
```
