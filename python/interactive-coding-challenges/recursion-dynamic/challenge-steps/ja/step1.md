# Python チャレンジ：階段

## 問題

n 段の階段の一番下に立っていると想像してください。1 回に 1 段、2 段、または 3 段を歩くことができます。問題は、n 段目まで上る方法が何通りあるかを見つけることです。

たとえば、3 段の階段がある場合、次のようにして階段を上ることができます。

- 1-1-1
- 1-2
- 2-1
- 3

したがって、3 段目まで上る方法は 4 通りあります。

## 要件

この問題を解くには、次の要件を念頭に置く必要があります。

- n == 0 の場合、結果は 1 でなければなりません。ただし、この問題にはさまざまなアプローチがあり、議論することができます。
- 入力が妥当であることを前提としてはいけません。
- 問題がメモリに収まることを前提としてよいです。

## 例の使い方

この問題を Python を使って解く方法のいくつかの例を次に示します。

- 入力がないか負の場合 -> 例外
- n == 0 -> 1
- n == 1 -> 1
- n == 2 -> 2
- n == 3 -> 4
- n == 4 -> 7
- n == 10 -> 274
