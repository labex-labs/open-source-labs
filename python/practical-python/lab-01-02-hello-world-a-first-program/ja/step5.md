# サンプル プログラム

次の問題を解いてみましょう。

> ある朝、あなたは外出して、シカゴのシアーズタワーの近くの歩道に1ドル札を置きます。その後、毎日、札の数を2倍にして外出します。札の山がタワーの高さを超えるまでにどれくらいの時間がかかりますか？

これは、`/home/labex/project` ディレクトリに `sears.py` ファイルを作成する解決策です。

```python
# sears.py
bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

実行すると、次の出力が得られます。

```bash
$ python3 sears.py
1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672
Number of days 23
Number of bills 4194304
Final height 461.37344
```

このプログラムを参考にして、Python に関する多くの重要なコア コンセプトを学ぶことができます。
