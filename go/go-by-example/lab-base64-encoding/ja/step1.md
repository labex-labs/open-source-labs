# Base64 エンコード

与えられた文字列を標準および URL 互換の Base64 エンコードを使用してエンコードおよびデコードする Go 言語のプログラムを書く必要があります。

- プログラムは、デフォルトの`base64`ではなく`b64`という名前で`encoding/base64`パッケージをインポートする必要があります。
- プログラムは、標準および URL 互換の Base64 エンコードを使用して与えられた文字列をエンコードする必要があります。
- プログラムは、標準および URL 互換の Base64 デコードを使用してエンコードされた文字列をデコードする必要があります。
- プログラムは、エンコードおよびデコードされた文字列をコンソールに出力する必要があります。

```sh
# 標準および URL の Base64 エンコーダーでは、文字列を少し異なる値にエンコードします
# （末尾の `+` と `-`）が、どちらも望ましいように元の文字列にデコードされます。
```

以下に完全なコードがあります：

```go
// Go は、[Base64 エンコード/デコード](https://en.wikipedia.org/wiki/Base64) に対する組み込みのサポートを提供しています。

package main

// この構文は、デフォルトの `base64` ではなく `b64` という名前で `encoding/base64` パッケージをインポートします。
// これにより、以下で少しスペースを節約できます。
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// ここにエンコード/デコードする `string` があります。
	data := "abc123!?$*&()'-=@~"

	// Go は、標準および URL 互換の Base64 の両方をサポートしています。
	// ここでは、標準エンコーダーを使用してエンコードする方法を示します。
	// エンコーダーには `[]byte` が必要なので、`string` をその型に変換します。
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// デコードはエラーを返す場合があります。
	// 入力が正しいことを既に知っていない場合は、これを確認できます。
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// これは、URL 互換の Base64 形式を使用してエンコード/デコードします。
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}

```
