# 素数を生成する

## 問題

Python 関数を書いて、素数のリストを生成します。この関数は整数を入力として受け取り、各値がそのインデックスが素数であるかどうかに対応するブール値のリストを返す必要があります。たとえば、入力が 20 の場合、出力は[False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]でなければなりません。ここで、インデックス 2 の値は True で、2 が素数であるためであり、インデックス 4 の値は False で、4 が素数でないためです。

## 要件

- 関数は 1 を素数としては考慮しないこと。
- 関数は無効な入力をエラーを発生させることで処理すること。
- 関数はメモリ内で素数のリストを生成すること。

## 例の使用法

- なし -> 例外
- 整数でない -> 例外
- 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
