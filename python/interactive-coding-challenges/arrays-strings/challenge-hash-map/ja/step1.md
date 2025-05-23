# ハッシュマップ

## 問題

set、get、および remove メソッドを備えたハッシュテーブルを実装します。ハッシュテーブルは、衝突解消にチェーニングを使用する必要があります。キーは整数のみです。ロードファクタや入力の検証は心配する必要はありません。ハッシュテーブルがメモリに収まると仮定して構いません。

## 要件

- キーは整数のみです。
- 衝突解消にチェーニングを使用します。
- ロードファクタを考慮する必要はありません。
- 入力を検証する必要はありません。
- ハッシュテーブルはメモリに収まります。

## 例の使用法

- `get` メソッド：
  - 一致するキーがない場合、KeyError 例外が発生します。
  - 一致するキーがある場合、対応する値が返されます。
- `set` メソッド：
  - 一致するキーがない場合、新しいキー-値のペアがハッシュテーブルに追加されます。
  - 一致するキーがある場合、対応する値が更新されます。
- `remove` メソッド：
  - 一致するキーがない場合、KeyError 例外が発生します。
  - 一致するキーがある場合、対応するキー-値のペアがハッシュテーブルから削除されます。
