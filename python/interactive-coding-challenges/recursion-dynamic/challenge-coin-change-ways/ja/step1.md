# コイン両替の方法

## 問題

整数 `n` と異なるコインの配列が与えられたとき、配列内のコインを使って `n` の両替方法の数を数える関数を書きなさい。コインは何度でも使え、一意の組み合わせを数えています。

たとえば、`n = 4` で `coins = [1, 2]` の場合、両替方法は 3 通りあります。1+1+1+1、1+2+1、2+2 です。

## 要件

この問題を解くには、以下のことが必要になります。

- 整数 `n` と異なるコインの配列を 2 つの引数として取る関数を書きます。
- 動的計画法を使って、配列内のコインを使って `n` の両替方法の数を数えます。
- 一意の組み合わせの数を返します。

## 例

入力：`n = 4`, `coins = [1, 2]`

出力：3。1+1+1+1、1+2+1、2+2 が両替方法になります。
