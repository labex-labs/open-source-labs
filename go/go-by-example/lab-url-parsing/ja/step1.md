# URL解析

この実験では、スキーム、認証情報、ホスト、ポート、パス、クエリパラメータ、およびクエリフラグメントを含むサンプルURLを解析する必要があります。解析されたURLを使用して、URLの個々のコンポーネントを抽出する必要があります。

- `url` パッケージと `net` パッケージをインポートする必要があります。
- サンプルURLを解析し、エラーを確認する必要があります。
- 解析されたURLから、スキーム、認証情報、ホスト、ポート、パス、クエリパラメータ、およびクエリフラグメントを抽出する必要があります。
- `SplitHostPort` 関数を使用して、`Host` フィールドからホスト名とポートを抽出する必要があります。
- `ParseQuery` 関数を使用して、クエリパラメータをマップに解析する必要があります。

```sh
# 私たちのURL解析プログラムを実行すると、抽出したすべての異なる部分が表示されます。
$ go run url-parsing.go
postgres
user:pass
user
pass
host.com:5432
host.com
5432
/path
f
k=v
map[k:[v]]
v

```

以下に完全なコードがあります。

```go
// URLは、[リソースを検索するための一貫した方法](https://adam.herokuapp.com/past/2010/3/30/urls_are_the_uniform_way_to_locate_resources/)を提供します。
// ここでは、Go言語でURLを解析する方法を示します。

package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {

	// このサンプルURLを解析します。このURLには、
	// スキーム、認証情報、ホスト、ポート、パス、
	// クエリパラメータ、およびクエリフラグメントが含まれています。
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	// URLを解析し、エラーがないことを確認します。
	u, err := url.Parse(s)
	if err!= nil {
		panic(err)
	}

	// スキームにアクセスするのは簡単です。
	fmt.Println(u.Scheme)

	// `User` にはすべての認証情報が含まれています。
	// 個々の値を取得するには、この関数に `Username` と `Password` を呼び出します。
	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	// `Host` には、ホスト名とポートが含まれています。
	// ポートが存在する場合は、`SplitHostPort` を使用して抽出します。
	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println(host)
	fmt.Println(port)

	// ここでは、`path` と `#` の後のフラグメントを抽出します。
	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	// `k=v` 形式の文字列を取得するには、`RawQuery` を使用します。
	// また、クエリパラメータをマップに解析することもできます。
	// 解析されたクエリパラメータのマップは、文字列から文字列のスライスへのマップです。
	// 最初の値のみを取得する場合は、`[0]` を指定してインデックスを指定します。
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}

```
