# 演習 1.6：デバッグ

次のコードフラグメントには、シアーズタワーの問題のコードが含まれています。また、その中にはバグもあります。

```python
# sears.py

bill_thickness = 0.11 * 0.001    # メートル (0.11 mm)
sears_height   = 442             # 高さ (メートル)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

上記のコードを、`sears.py` という新しいプログラムにコピーして貼り付けてください。コードを実行すると、次のようにエラーメッセージが表示され、プログラムがクラッシュします。

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

エラーメッセージの読み取りは、Python コードの重要な部分です。プログラムがクラッシュした場合、トレースバックメッセージの最後の行が、プログラムがクラッシュした実際の理由です。その上には、ソースコードの断片と、識別用のファイル名と行番号が表示されます。

- エラーのある行はどれですか？
- エラー内容は何ですか？
- エラーを修正してください。
- プログラムを正常に実行してください。
