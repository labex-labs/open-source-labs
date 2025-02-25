# ビット操作

## 問題

Pythonで以下の一般的なビット操作を実装します。

- `get_bit`：数値とインデックスを指定して、指定されたインデックスのビットの値を返します。
- `set_bit`：数値とインデックスを指定して、指定されたインデックスのビットの値を1に設定します。
- `clear_bit`：数値とインデックスを指定して、指定されたインデックスのビットの値を0に設定します。
- `clear_bits_msb_to_index`：数値とインデックスを指定して、最上位ビットから指定されたインデックスまでのすべてのビットを0に設定します。
- `clear_bits_index_to_lsb`：数値とインデックスを指定して、指定されたインデックスから最下位ビットまでのすべてのビットを0に設定します。
- `update_bit`：数値、インデックス、および値を指定して、指定されたインデックスのビットの値を指定された値に更新します。

## 要件

実装は以下の要件を満たす必要があります。

- 入力が有効でない場合があり、実装はそのようなケースを適切に処理する必要があります。
- 実装はメモリに収まる必要があります。

## 使い方の例

実装された関数の使い方の例を以下に示します。

- `get_bit`：
  ```
  number   = 0b10001110
  index = 3
  expected = True
  ```
- `set_bit`：
  ```
  number   = 0b10001110
  index = 4
  expected = 0b10011110
  ```
- `clear_bit`：
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000110
  ```
- `clear_bits_msb_to_index`：
  ```
  number   = 0b10001110
  index = 3
  expected = 0b00000110
  ```
- `clear_bits_index_to_lsb`：
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000000
  ```
- `update_bit`：

  ```
  number   = 0b10001110
  index = 3
  value = 1
  expected = 0b10001110

  number   = 0b10001110
  index = 3
  value = 0
  expected = 0b10000110

  number   = 0b10001110
  index = 0
  value = 1
  expected = 0b10001111
  ```
