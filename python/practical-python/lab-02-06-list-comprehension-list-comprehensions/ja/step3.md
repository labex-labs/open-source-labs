# ユースケース

リスト内包表記は非常に便利です。たとえば、特定の辞書フィールドの値を収集することができます。

```python
stocknames = [s['name'] for s in stocks]
```

シーケンスに対してデータベースのようなクエリを実行することができます。

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

また、リスト内包表記とシーケンスの集約を組み合わせることもできます。

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```
