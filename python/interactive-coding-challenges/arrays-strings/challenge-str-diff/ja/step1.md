# 文字列の差分

## 問題

2 つの文字列が与えられたとき、それらの間の 1 つだけの異なる文字を見つける必要があります。文字列は ASCII で、小文字であると仮定されます。入力が有効であることを前提とすることはできないので、None をチェックする必要があります。入力が有効な場合、2 つの文字列の間にはただ 1 つの異なる文字があると仮定できます。また、解がメモリに収まることを確認する必要があります。

## 要件

この問題を解くには、以下の要件を考慮する必要があります。

- 文字列は ASCII です。
- 文字列は小文字です。
- 入力が None であることをチェックする必要があります。
- 2 つの文字列の間にはただ 1 つの異なる文字があります。
- 解はメモリに収まる必要があります。

## 例

ここに、関数を使用する方法のいくつかの例を示します。

- 入力が None -> TypeError
- 'ab', 'aab' -> 'a'
- 'aab', 'ab' -> 'a'
- 'abcd', 'abcde' -> 'e'
- 'aaabbcdd', 'abdbacade' -> 'e'
