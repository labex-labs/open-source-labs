# 文字列とルーン

このチャレンジで解くべき問題は、Go 言語で文字列とルーンを扱う方法を理解することです。具体的には、文字列の長さを取得する方法、文字列のインデックスを指定する方法、文字列内のルーンの数を数える方法、および文字列内のルーンを反復処理する方法をカバーします。

## 要件

このチャレンジを完了するには、以下が必要です。

- Go 言語の構文の基本的な理解
- Go 言語の文字列とルーンの知識
- Go 言語の標準ライブラリ

## 例

```sh
$ go run strings-and-runes.go
Len: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Rune count: 6
U+0E2A 'ส' starts at 0
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15

Using DecodeRuneInString
U+0E2A 'ส' starts at 0
found so sua
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
found so sua
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15
```
