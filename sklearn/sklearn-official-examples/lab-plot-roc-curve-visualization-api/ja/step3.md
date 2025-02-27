# ランダムフォレストを学習してROC曲線を描画する

このステップでは、ランダムフォレスト分類器を学習し、そのROC曲線をSVCのROC曲線と並べて描画します。これを行うには、新しい`RandomForestClassifier`オブジェクトを作成し、学習データに適合させ、その後この分類器を使用して新しい`RocCurveDisplay`オブジェクトを作成します。また、この関数に`ax`パラメータを渡して、同じ軸上に曲線を描画します。最後に、SVCのROC曲線を描画するために`svc_disp`オブジェクトの`plot()`メソッドを呼び出します。

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
