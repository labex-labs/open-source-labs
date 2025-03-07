# n 対の括弧

## 問題

問題は、n 対の括弧のすべての有効な組み合わせを見つけることです。有効な組み合わせとは、各開き括弧に対応する閉じ括弧があり、括弧のペアが適切にネストされている組み合わせのことです。たとえば、3 対の括弧の有効な組み合わせは以下の通りです。

- ((()))
- (()())
- (())()
- ()(())
- ()()()

以下は、3 対の括弧の有効でない組み合わせです。

- )()(
- ((()
- ))((
- ()()()

## 要件

この問題を解くには、以下の質問に答える必要があります。

- 入力は、ペアの数を表す整数ですか？
  - はい、入力はペアの数を表す整数です。
- 入力が有効であると仮定できますか？
  - いいえ、入力が有効であると仮定できません。
- 出力は有効な組み合わせのリストですか？
  - はい、出力は有効な組み合わせのリストです。
- 出力に重複があっても良いですか？
  - いいえ、出力に重複はあってはなりません。
- これがメモリに収まると仮定できますか？
  - はい、これがメモリに収まると仮定できます。

## 例の使用法

以下は、関数の例の使用法です。

- なし -> 例外
- 負の数 -> 例外
- 0 -> []
- 1 -> ['()']
- 2 -> ['(())', '()()']
- 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
