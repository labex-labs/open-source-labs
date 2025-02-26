# `unittest` の使用方法

`unittest` にはいくつかの組み込みアサーションがあります。それぞれが異なることをアサートします。

```python
# expr が真であることをアサートする
self.assertTrue(expr)

# x == y であることをアサートする
self.assertEqual(x,y)

# x!= y であることをアサートする
self.assertNotEqual(x,y)

# x が y に近いことをアサートする
self.assertAlmostEqual(x,y,places)

# callable(arg1,arg2,...) が exc を発生させることをアサートする
self.assertRaises(exc, callable, arg1, arg2,...)
```

これは網羅的な一覧ではありません。モジュールには他にもアサーションがあります。
