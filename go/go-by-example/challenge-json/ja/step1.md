# JSON

Go言語でJSONデータをエンコードおよびデコードするために提供されたコードを完成させる必要があります。このコードには、基本データ型のエンコードとデコードの例の他、カスタムデータ型も含まれています。

## 要件

- Go言語のプログラミング言語の基本知識
- Go言語でJSONデータをエンコードおよびデコードすることに慣れていること
- 既存のGo言語のコードを読み取り、理解する能力

## 例

```sh
$ go run json.go
true
1
2.34
"gopher"
["apple","peach","pear"]
{"apple":5,"lettuce":7}
{"Page":1,"Fruits":["apple","peach","pear"]}
{"page":1,"fruits":["apple","peach","pear"]}
map[num:6.13 strs:[a b]]
6.13
a
{1 [apple peach]}
apple
{"apple":5,"lettuce":7}


# ここではGoにおけるJSONの基本を扱いましたが、
# 詳細については[JSON and Go](https://go.dev/blog/json)
# のブログ記事と[JSONパッケージドキュメント](https://pkg.go.dev/encoding/json)
# を参照してください。

```
