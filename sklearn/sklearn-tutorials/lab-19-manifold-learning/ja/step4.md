# 結果を比較する

異なる多様体学習アルゴリズムの結果を比較しましょう。変換後のデータを可視化して、アルゴリズムがデータの基礎となる構造をどのように保持しているかを確認します。

```python
import matplotlib.pyplot as plt

# 変換後のデータの散布図を作成
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('多様体学習')
plt.xlabel('成分1')
plt.ylabel('成分2')
plt.show()
```
