# ダミー変数を作成する

`get_dummies` メソッドを使用して、文字列データからダミー変数を作成することができます。

```python
# ダミー変数を作成する
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```
