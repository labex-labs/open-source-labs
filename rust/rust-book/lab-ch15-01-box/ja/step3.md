# ボックスを使った再帰型の有効化

「再帰型」の値は、それ自体の一部として同じ型の別の値を持つことができます。再帰型は問題を引き起こします。なぜなら、コンパイル時に Rust は型がどれだけのスペースを占めるかを知る必要があるからです。しかし、再帰型の値のネストは理論的には無限に続く可能性があるため、Rust は値がどれだけのスペースを必要とするかを知ることができません。ボックスは既知のサイズを持っているので、再帰型の定義にボックスを挿入することで再帰型を有効にすることができます。

再帰型の例として、「コンズリスト」を見てみましょう。これは関数型言語で一般的に見られるデータ型です。ここで定義するコンズリスト型は、再帰を除けば簡単です。したがって、この例で扱う概念は、再帰型に関するより複雑な状況に遭遇したときに役立ちます。
