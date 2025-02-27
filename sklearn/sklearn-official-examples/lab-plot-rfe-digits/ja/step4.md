# 特徴のランキングを可視化する

最後に、Matplotlib ライブラリを使って特徴のランキングをプロットします。`matshow()` 関数を使って、ランキングを画像として表示します。また、カラーバーとタイトルをプロットに追加します。

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
```
