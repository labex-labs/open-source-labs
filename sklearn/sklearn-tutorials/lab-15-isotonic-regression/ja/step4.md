# モデルを使って予測する

モデルをフィットさせた後、新しいデータに対する予測を行うことができます。新しい配列`X_new`を作成し、対応するターゲット値を予測しましょう。

```python
# Create new data for prediction
X_new = np.linspace(0, 1, 100)
y_pred = ir.predict(X_new)
```
