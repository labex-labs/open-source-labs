# `itertools` モジュール

`itertools` は、反復子/ジェネレータを助けるために設計されたさまざまな関数を備えたライブラリモジュールです。

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1,... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1,..., sN)
```

すべての関数は、データを反復的に処理します。さまざまな種類の反復パターンを実装しています。

PyCon '08 の [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) チュートリアルで詳細を確認できます。

前のエクササイズでは、ログファイルに書き込まれる行に追従し、それらを行のシーケンスに解析するコードをいくつか書きました。このエクササイズはそれに基づいてさらに構築されます。`stocksim.py` がまだ実行されていることを確認してください。
