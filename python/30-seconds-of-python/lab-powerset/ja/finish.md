# まとめ

このチャレンジでは、与えられた反復可能オブジェクトの冪集合を返す Python 関数を作成する方法を学びました。この関数は、すべての部分集合を返すジェネレータを作成するために `range()` と `itertools.combinations()` を使用し、ジェネレータを消費してリストを返すために `itertools.chain.from_iterable()` と `list()` を使用します。
