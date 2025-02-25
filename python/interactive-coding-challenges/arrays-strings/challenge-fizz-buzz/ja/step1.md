# Fizz Buzz

## 問題

Python を使って Fizz Buzz を実装します。あなたの関数は整数 n を入力として受け取り、1 から n までの数を表す文字列のリストを返す必要がありますが、次の変更があります。

- 3 の倍数は文字列 "Fizz" に置き換える
- 5 の倍数は文字列 "Buzz" に置き換える
- 3 と 5 の両方の倍数は文字列 "FizzBuzz" に置き換える

あなたの関数はまた、次のケースに対応する必要があります。

- 入力が 1 未満の場合、例外を発生させる
- 入力が有効な整数でない場合、例外を発生させる

## 要件

Python で Fizz Buzz を実装するには、次の要件を満たす必要があります。

- 整数 n を入力として受け取る関数を定義する
- 入力が有効な整数であるかどうかを確認し、そうでない場合は例外を発生させる
- 入力が 1 未満であるかどうかを確認し、そうであれば例外を発生させる
- 上記の変更を加えて、1 から n までの数を表す文字列のリストを作成する
- リストを返す

## 例の使用方法

```python
assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```

```python
try:
    fizz_buzz(0)
except ValueError:
    print("Invalid input")
```

```python
try:
    fizz_buzz("hello")
except ValueError:
    print("Invalid input")
```

```python
try:
    fizz_buzz(-5)
except ValueError:
    print("Invalid input")
```
