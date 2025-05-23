# 挿入ソート

## 問題

Python で挿入ソートを実装する問題です。要素の並び替えが済んでいないリストが与えられた場合、このアルゴリズムはそのリストを昇順にソートする必要があります。このアルゴリズムは、リストを反復して、各要素をリストのソート済み部分における正しい位置に挿入することで動作します。

このアルゴリズムは、リストの最初の要素が既にソート済みであると仮定して始まります。その後、リストの残りの要素を反復し、各要素をリストのソート済み部分の要素と比較します。要素がリストのソート済み部分の現在の要素より小さい場合、その要素はその要素の前に挿入されます。要素がリストのソート済み部分のすべての要素より大きい場合、その要素はリストのソート済み部分の末尾に挿入されます。

## 要件

Python で挿入ソートを実装するには、次の要件を満たす必要があります。

- 単純な解決策で十分です。
- 重複は許可されます。
- 入力が必ずしも有効でない場合があるため、アルゴリズムは無効な入力に対処できるようにする必要があります。
- アルゴリズムはメモリに収まる必要があります。

## 例の使用方法

挿入ソートアルゴリズムの使用方法の例を以下に示します。

- None -> 例外：入力が None の場合、例外を発生させる必要があります。
- 空の入力 -> []: 入力が空のリストの場合、出力も空のリストでなければなりません。
- 1 つの要素 -> [要素]: 入力が 1 つの要素のみを持つリストの場合、出力は同じリストでなければなりません。
- 2 つ以上の要素：入力が 2 つ以上の要素を持つリストの場合、出力は昇順にソートされたリストでなければなりません。
