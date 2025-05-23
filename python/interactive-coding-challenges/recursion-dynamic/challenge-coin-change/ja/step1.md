# コインチェンジ

## 問題

異なる額面のコインのセットと、合計金額 n が与えられたとき、n セントの両替を行う一意な方法の総数を求めます。与えられたコインの額面は n セント未満です。

## 要件

この問題を解くには、以下の要件を満たす必要があります。

- コインは正確に n セントに達する必要があります。
- n セントを作るためには無限にコインがあると仮定できます。
- 最小を表すコインの組み合わせは報告する必要はありません。
- コインの額面はソートされた順序で与えられません。
- 解はメモリに収まる必要があります。

## 例の使い方

以下の例は、コインチェンジ問題の使い方を示しています。

- コイン：なし または n: なし -> 例外
- コイン：[] または n: 0 -> 0
- コイン：[1, 2, 3], n: 5 -> 5
