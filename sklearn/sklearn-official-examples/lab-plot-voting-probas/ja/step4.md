# データセットの最初のサンプルに対するクラス確率の取得

データセットの最初のサンプルに対するクラス確率を取得し、class1_1 と class2_1 に格納します。

```python
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]
```
