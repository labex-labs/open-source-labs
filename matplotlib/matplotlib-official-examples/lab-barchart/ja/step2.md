# データを準備する

次に、チャート用のデータを準備します。ペンギンの種類が 3 つで、属性も 3 つあるので、種ごとの各属性の平均値を持つ辞書を作成します。

```python
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
```
