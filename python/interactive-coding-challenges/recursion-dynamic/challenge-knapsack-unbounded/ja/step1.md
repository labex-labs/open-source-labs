# ナップサック無制限

## 問題

総重量容量のあるナップサックと、重量 w(i) と価値 v(i) のアイテムのリストが与えられたとき、運ぶことができる最大の総価値を求めます。アイテムは複数回選択できます。

## 要件

ナップサック無制限問題を解くには、次の要件を満たす必要があります。

- アイテムはナップサックに入れた後に交換できます。
- アイテムは分割できません。
- 入力されたアイテムの重量または価値が 0 であってはなりません。
- 最大の総価値を構成するアイテムではなく、総価値のみを返す必要があります。
- 入力が有効でない場合があるため、検証が必要です。
- 入力は val/weight でソートされています。
- メモリ制約は問題になりません。

## 例の使い方

ナップサック無制限問題は、資源割り当てや金融ポートフォリオ最適化など、さまざまなシナリオで使用できます。以下に、その使い方の例をいくつか示します。

- 総重量またはアイテムが None の場合、例外を発生させる必要があります。
- 総重量またはアイテムが 0 の場合、結果は 0 にする必要があります。
- 一般的な場合を考えます。総重量が 8 で、アイテムは次のとおりです。

  | v   | w   |
  | --- | --- |
  | 0   | 0   |
  | 1   | 1   |
  | 3   | 2   |
  | 7   | 4   |

  運ぶことができる最大の価値は 14 です。
