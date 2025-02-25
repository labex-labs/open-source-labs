# 折れ線グラフ

折れ線グラフは、カテゴリ変数が時間の経過とともにどのように変化するかを示すために使用できます。この例では、さまざまな活動中の猫と犬の幸せ度に関するデータを使用します。

```python
cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]
plt.plot(activity, dog, label="dog")
plt.plot(activity, cat, label="cat")
plt.title('Happiness Levels')
plt.xlabel('Activity')
plt.ylabel('Happiness')
plt.legend()
plt.show()
```
