# Base64エンコード

与えられた文字列を標準およびURL互換のBase64エンコードを使用してエンコードおよびデコードするGo言語のプログラムを書く必要があります。

- プログラムは、デフォルトの`base64`ではなく`b64`という名前で`encoding/base64`パッケージをインポートする必要があります。
- プログラムは、標準およびURL互換のBase64エンコードを使用して与えられた文字列をエンコードする必要があります。
- プログラムは、標準およびURL互換のBase64デコードを使用してエンコードされた文字列をデコードする必要があります。
- プログラムは、エンコードおよびデコードされた文字列をコンソールに出力する必要があります。

```sh
# 標準およびURLのBase64エンコーダーでは、文字列を少し異なる値にエンコードします
# （末尾の`+`と`-`）が、どちらも望ましいように元の文字列にデコードされます。
$ go run base64-encoding.go
YWJjMTIzIT8kKiYoKSctPUB+
abc123!?$*&()'-=@~

YWJjMTIzIT8kKiYoKSctPUB-
abc123!?$*&()'-=@~

```

以下に完全なコードがあります：

```go
// Goは、[Base64エンコード/デコード](https://en.wikipedia.org/wiki/Base64)に対する組み込みのサポートを提供しています。

package main

// この構文は、デフォルトの`base64`ではなく`b64`という名前で`encoding/base64`パッケージをインポートします。
// これにより、以下で少しスペースを節約できます。
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// ここにエンコード/デコードする`string`があります。
	data := "abc123!?$*&()'-=@~"

	// Goは、標準およびURL互換のBase64の両方をサポートしています。
	// ここでは、標準エンコーダーを使用してエンコードする方法を示します。
	// エンコーダーには`[]byte`が必要なので、`string`をその型に変換します。
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// デコードはエラーを返す場合があります。
	// 入力が正しいことを既に知っていない場合は、これを確認できます。
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// これは、URL互換のBase64形式を使用してエンコード/デコードします。
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}

```
