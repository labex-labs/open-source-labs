# 名前から苗字を抽出する

次に、乗客の苗字を含む新しい列`Surname`を作成しましょう。これは、`Name`列のカンマの前の部分を抽出することで達成されます。

```python
# 'Name'列をカンマで分割し、最初の部分を抽出する
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
```
