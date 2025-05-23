# バランスのチェック

## 問題

二分木が与えられたとき、それが平衡しているかどうかを判定する Python 関数を書きます。任意のノードの 2 つの部分木の高さの差が最大 1 である場合、二分木は平衡していると見なされます。この関数は、二分木の根ノードを入力として受け取り、木が平衡している場合は True を返し、そうでない場合は False を返します。入力が None の場合、関数は例外を発生させる必要があります。

## 要件

この問題を解くには、次の要件を満たす必要があります。

- 平衡した木は、任意のノードの 2 つの部分木の高さの差が 1 を超えない木です。
- 入力が None の場合、関数は例外を発生させる必要があります。
- 既に insert メソッドを持つ Node クラスがあると仮定できます。
- プログラムがメモリに収まると仮定できます。

## 例の使用法

この関数がどのように動作するかの例をいくつか示します。

- None -> 例外を発生させる
- 1 -> True
- 5, 3, 8, 1, 4 -> True
- 5, 3, 8, 9, 10 -> False
