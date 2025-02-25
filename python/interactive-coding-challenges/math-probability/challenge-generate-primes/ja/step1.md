# 素数を生成する

## 問題

Python関数を書いて、素数のリストを生成します。この関数は整数を入力として受け取り、各値がそのインデックスが素数であるかどうかに対応するブール値のリストを返す必要があります。たとえば、入力が20の場合、出力は[False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]でなければなりません。ここで、インデックス2の値はTrueで、2が素数であるためであり、インデックス4の値はFalseで、4が素数でないためです。

## 要件

- 関数は1を素数としては考慮しないこと。
- 関数は無効な入力をエラーを発生させることで処理すること。
- 関数はメモリ内で素数のリストを生成すること。

## 例の使用法

- なし -> 例外
- 整数でない -> 例外
- 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
