# ROC 曲線を描画する

次に、`RocCurveDisplay.from_estimator`関数を使って ROC 曲線を描画します。この関数は、学習済みの分類器、テスト用データセット、および真のラベルを入力として受け取り、ROC 曲線を描画するために使用できるオブジェクトを返します。その後、`show()`メソッドを呼び出してプロットを表示します。

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```
