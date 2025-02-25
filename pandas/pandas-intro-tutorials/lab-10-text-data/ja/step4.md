# 特定の乗客データを抽出する

次に、タイタニック号の船内にいた伯爵夫人たちの乗客データを抽出しましょう。`Name`列に'Countess'という単語が含まれる行を見つけるために、`str.contains()`メソッドを使用します。

```python
# 'Name'に'Countess'が含まれる行を見つける
countesses = titanic[titanic["Name"].str.contains("Countess")]
```
