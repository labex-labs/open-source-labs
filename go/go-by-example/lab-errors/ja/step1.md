# エラー

この実験では、入力引数が 42 の場合にエラーを返す 2 つの関数が用意されています。最初の関数は基本的なエラー値を返し、2 番目の関数はエラーを表すためにカスタム型を使用します。

- `errors` パッケージをインポートする必要があります。
- `f1` 関数は、入力引数が 42 の場合にエラーを返す必要があります。
- `f2` 関数は、入力引数が 42 の場合に `argError` 型のエラーを返す必要があります。
- `argError` 型は、2 つのフィールド `arg` と `prob` を持たなければなりません。
- `argError` 型は `Error()` メソッドを実装する必要があります。
- `main` 関数は、入力引数として 7 と 42 を使って `f1` と `f2` の両方を呼び出す必要があります。
- `main` 関数は、各関数呼び出しの結果と、返されたエラーを表示する必要があります。
- `main` 関数は、カスタムエラーのデータをプログラム的に使用する方法を示す必要があります。

```sh
# エラーハンドリングに関する詳細は、
# Go のブログのこの [素晴らしい記事](https://go.dev/blog/error-handling-and-go) を参照してください。
```

以下が完全なコードです：

```go
// Go 言語では、エラーを明示的な別の戻り値を通じて伝えるのが慣習的です。
// これは、Java や Ruby のような言語で使用される例外や、
// 時々 C 言語で使用されるオーバーロードされた単一の結果/エラー値とは対照的です。
// Go のアプローチにより、どの関数がエラーを返すかを簡単に確認でき、
// 他の非エラータスクと同じ言語構文を使ってエラーを処理できます。

package main

import (
	"errors"
	"fmt"
)

// 慣例として、エラーは最後の戻り値で、
// 型 `error`（組み込みのインターフェイス）を持ちます。
func f1(arg int) (int, error) {
	if arg == 42 {

		// `errors.New` は、与えられたエラーメッセージで基本的な `error` 値を構築します。
		return -1, errors.New("can't work with 42")

	}

	// エラー位置の `nil` 値は、エラーがなかったことを示します。
	return arg + 3, nil
}

// カスタム型を `error` として使用するには、
// それに対して `Error()` メソッドを実装することができます。
// 以下は、上の例のバリエーションで、引数エラーを明示的に表すためにカスタム型を使用しています。
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {

		// この場合、`&argError` 構文を使って新しい構造体を作成し、
		// 2 つのフィールド `arg` と `prob` に値を提供します。
		return -1, &argError{arg, "can't work with it"}
	}
	return arg + 3, nil
}

func main() {

	// 以下の 2 つのループは、エラーを返す各関数をテストします。
	// `if` 行でのインラインエラーチェックの使用は、Go コードの一般的な慣用句です。
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e!= nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e!= nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	// カスタムエラーのデータをプログラム的に使用したい場合は、
	// 型アサーションを通じてエラーをカスタムエラー型のインスタンスとして取得する必要があります。
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}

```
