# `object` 基底クラス

クラスに親がない場合、時には `object` が基底として使用されることがあります。

```python
class Shape(object):
...
```

`object` は Python のすべてのオブジェクトの親です。

\*注：技術的には必要ありませんが、Python 2 での必須の使用からの残りとして指定されるのをよく見ます。省略した場合でも、クラスは依然として暗黙的に `object` から継承します。
