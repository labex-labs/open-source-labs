# パターン内で値を無視する

`match` の最後のアームのように、パターン内で値を無視することが役立つ場合があることは見てきました。これは、実際には何もしないが、残りのすべての可能な値を網羅するキャッチオールを実現するためです。パターン内で値全体または値の一部を無視する方法はいくつかあります。すでに見た `_` パターンを使用する方法、他のパターン内で `_` パターンを使用する方法、アンダースコアで始まる名前を使用する方法、または `..` を使用して値の残りの部分を無視する方法です。それでは、これらの各パターンをいつ、なぜ使用するのかを見ていきましょう。
