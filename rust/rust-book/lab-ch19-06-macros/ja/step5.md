# カスタム `derive` マクロを書く方法

`hello_macro` という名前のクレートを作成しましょう。このクレートには、`HelloMacro` という名前のトレイトが定義されており、そのトレイトには `hello_macro` という名前の1つの関連付けられた関数があります。ユーザーに対してそれぞれの型に対して `HelloMacro` トレイトを実装させるのではなく、手続き型マクロを提供して、ユーザーが `#[derive(HelloMacro)]` で型を注釈付けすることで、`hello_macro` 関数のデフォルトの実装を取得できるようにします。デフォルトの実装では、`Hello, Macro! My name is` TypeName`!` と出力されます。ここで、TypeNameはこのトレイトが定義されている型の名前です。言い換えると、他のプログラマーが私たちのクレートを使ってリスト19-30のようなコードを書けるように、私たちはクレートを書きます。

ファイル名: `src/main.rs`

```rust
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
```

リスト19-30: 私たちのクレートのユーザーが手続き型マクロを使用した場合に書けるようになるコード

このコードは、完了したときに `Hello, Macro! My name is Pancakes!` と出力します。最初のステップは、新しいライブラリクレートを作成することです。次のようにします。

```bash
cargo new hello_macro --lib
```

次に、`HelloMacro` トレイトとその関連付けられた関数を定義します。

ファイル名: `src/lib.rs`

```rust
pub trait HelloMacro {
    fn hello_macro();
}
```

トレイトとその関数があります。この時点で、私たちのクレートのユーザーは、次のようにトレイトを実装して、望ましい機能を達成することができます。

```rust
use hello_macro::HelloMacro;

struct Pancakes;

impl HelloMacro for Pancakes {
    fn hello_macro() {
        println!("Hello, Macro! My name is Pancakes!");
    }
}

fn main() {
    Pancakes::hello_macro();
}
```

しかし、彼らは `hello_macro` で使用したい各型に対して実装ブロックを書かなければなりません。私たちは彼らにこの作業を強いたくありません。

また、私たちはまだ、トレイトが実装されている型の名前を出力するデフォルトの実装を `hello_macro` 関数に提供することができません。Rustにはリフレクション機能がないため、実行時に型の名前を参照することができません。コンパイル時にコードを生成するために、マクロが必要です。

次のステップは、手続き型マクロを定義することです。この記事を書いている時点で、手続き型マクロは独自のクレートに存在する必要があります。最終的に、この制限は解除されるかもしれません。クレートとマクロクレートを構成する規則は次の通りです。fooという名前のクレートに対して、カスタム `derive` 手続き型マクロクレートは foo`_derive` と呼ばれます。`hello_macro` プロジェクト内に新しい `hello_macro_derive` という名前のクレートを作成しましょう。

```bash
cargo new hello_macro_derive --lib
```

私たちの2つのクレートは密接に関連しているため、`hello_macro` クレートのディレクトリ内に手続き型マクロクレートを作成します。`hello_macro` のトレイト定義を変更すると、`hello_macro_derive` の手続き型マクロの実装も変更する必要があります。2つのクレートは別々に公開する必要があり、これらのクレートを使用するプログラマーは、両方を依存関係として追加し、両方をスコープに持ち込む必要があります。代わりに、`hello_macro` クレートが `hello_macro_derive` を依存関係として使用し、手続き型マクロコードを再エクスポートすることもできます。ただし、私たちがプロジェクトを構成した方法により、プログラマーが `derive` 機能を必要としない場合でも、`hello_macro` を使用できるようになります。

`hello_macro_derive` クレートを手続き型マクロクレートとして宣言する必要があります。また、すぐに見るでしょうが、`syn` と `quote` クレートの機能が必要なので、依存関係として追加する必要があります。`hello_macro_derive` の `Cargo.toml` ファイルに次のように追加します。

ファイル名: `hello_macro_derive/Cargo.toml`

```toml
[lib]
proc-macro = true

[dependencies]
syn = "1.0"
quote = "1.0"
```

手続き型マクロを定義し始めるには、`hello_macro_derive` クレートの `src/lib.rs` ファイルにリスト19-31のコードを配置します。`impl_hello_macro` 関数の定義を追加するまで、このコードはコンパイルされません。

ファイル名: `hello_macro_derive/src/lib.rs`

```rust
use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    // Rustコードを構文木として表現し、操作できるようにする
    let ast = syn::parse(input).unwrap();

    // トレイトの実装を構築する
    impl_hello_macro(&ast)
}
```

リスト19-31: Rustコードを処理するために必要な手続き型マクロクレートのほとんどのコード

`hello_macro_derive` 関数は、`TokenStream` を解析する責任があり、`impl_hello_macro` 関数は、構文木を変換する責任があります。これにより、手続き型マクロを書くのが便利になります。外側の関数（この場合は `hello_macro_derive`）のコードは、見たり作成したりするほとんどの手続き型マクロクレートで同じになります。内側の関数（この場合は `impl_hello_macro`）の本体で指定するコードは、手続き型マクロの目的に応じて異なります。

私たちは3つの新しいクレートを紹介しました。`proc_macro`、`syn`（*https://crates.io/crates/syn* から入手可能）、および `quote`（*https://crates.io/crates/quote* から入手可能）です。`proc_macro` クレートはRustに付属しているため、`Cargo.toml` の依存関係に追加する必要はありませんでした。`proc_macro` クレートは、コンパイラのAPIであり、コードからRustコードを読み取り、操作することができます。

`syn` クレートは、文字列をRustコードに解析して、操作できるデータ構造にします。`quote` クレートは、`syn` データ構造を再びRustコードに変換します。これらのクレートにより、取り扱いたい任意の種類のRustコードを解析するのがはるかに簡単になります。Rustコード用の完全なパーサを書くのは簡単な作業ではありません。

`hello_macro_derive` 関数は、ライブラリのユーザーが型に `#[derive(HelloMacro)]` を指定したときに呼び出されます。これは、ここで `hello_macro_derive` 関数に `proc_macro_derive` アノテーションを付け、トレイト名と一致する `HelloMacro` という名前を指定したからできます。これは、ほとんどの手続き型マクロが従う規則です。

`hello_macro_derive` 関数はまず、`input` を `TokenStream` から、その後で解釈して操作できるデータ構造に変換します。ここが `syn` が登場するところです。`syn` の `parse` 関数は `TokenStream` を取り、解析されたRustコードを表す `DeriveInput` 構造体を返します。リスト19-32は、`struct Pancakes;` 文字列を解析することで得られる `DeriveInput` 構造体の関連部分を示しています。

    DeriveInput {
        --snip--

        ident: Ident {
            ident: "Pancakes",
            span: #0 bytes(95..103)
        },
        data: Struct(
            DataStruct {
                struct_token: Struct,
                fields: Unit,
                semi_token: Some(
                    Semi
                )
            }
        )
    }

リスト19-32: リスト19-30のマクロ属性を持つコードを解析するときに得られる `DeriveInput` インスタンス

この構造体のフィールドは、解析したRustコードが `Pancakes` の `ident`（識別子、つまり名前）を持つユニット構造体であることを示しています。この構造体には、さまざまな種類のRustコードを記述するためのさらに多くのフィールドがあります。詳細については、*https://docs.rs/syn/1.0/syn/struct.DeriveInput.html* の `DeriveInput` の `syn` ドキュメントを参照してください。

すぐに、新しいRustコードを生成する `impl_hello_macro` 関数を定義します。しかし、その前に、`derive` マクロの出力も `TokenStream` であることに注意してください。返された `TokenStream` は、クレートのユーザーが書いたコードに追加されます。したがって、彼らがクレートをコンパイルするとき、修正された `TokenStream` に含まれる追加の機能を得ることができます。

`syn::parse` 関数の呼び出しがここで失敗した場合に、`hello_macro_derive` 関数がパニックするように `unwrap` を呼んでいることに気付いたかもしれません。手続き型マクロがエラーでパニックする必要があるのは、`proc_macro_derive` 関数が手続き型マクロAPIに準拠するために `TokenStream` を返さなければならないからです。この例では `unwrap` を使って簡略化していますが、本番コードでは、`panic!` または `expect` を使って何が問題だったかに関するより具体的なエラーメッセージを提供する必要があります。

ここで、注釈付きのRustコードを `TokenStream` から `DeriveInput` インスタンスに変換するコードがあるので、注釈付きの型に対して `HelloMacro` トレイトを実装するコードを生成しましょう。リスト19-33を参照してください。

ファイル名: `hello_macro_derive/src/lib.rs`

```rust
fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!(
                    "Hello, Macro! My name is {}!",
                    stringify!(#name)
                );
            }
        }
    };
    gen.into()
}
```

リスト19-33: 解析されたRustコードを使用して `HelloMacro` トレイトを実装する

`ast.ident` を使用して、注釈付きの型の名前（識別子）を含む `Ident` 構造体インスタンスを取得します。リスト19-32の構造体は、リスト19-30のコードに対して `impl_hello_macro` 関数を実行したとき、取得する `ident` が `ident` フィールドに `"Pancakes"` の値を持つことを示しています。したがって、リスト19-33の `name` 変数は、`Ident` 構造体インスタンスを含み、これを印刷すると、リスト19-30の構造体の名前である文字列 `"Pancakes"` になります。

`quote!` マクロを使って、返すRustコードを定義します。コンパイラは、`quote!` マクロの実行の直接の結果とは異なるものを期待しているため、`TokenStream` に変換する必要があります。これは、この中間表現を消費して、必要な `TokenStream` 型の値を返す `into` メソッドを呼び出すことで行います。

`quote!` マクロはまた、非常に便利なテンプレート機能も提供します。`#name` を入力すると、`quote!` はそれを `name` 変数の値で置き換えます。通常のマクロと同じように、繰り返し処理もできます。詳細な紹介については、*https://docs.rs/quote* の `quote` クレートのドキュメントを参照してください。

私たちの手続き型マクロは、ユーザーが注釈付けした型に対して `HelloMacro` トレイトの実装を生成したいと思っています。これは、`#name` を使用することで取得できます。トレイトの実装には、1つの関数 `hello_macro` があり、その本体には、私たちが提供したい機能が含まれています。つまり、`Hello, Macro! My name is` と出力して、その後に注釈付きの型の名前を出力します。

ここで使用されている `stringify!` マクロは、Rustに組み込まれています。これは、Rust式（たとえば `1 + 2`）を取り、コンパイル時に式を文字列リテラル（たとえば `"1 + 2"`）に変換します。これは、式を評価してから結果を `String` に変換する `format!` や `println!` マクロとは異なります。`#name` 入力が文字通り出力する式である可能性があるため、`stringify!` を使用します。`stringify!` を使用することで、コンパイル時に `#name` を文字列リテラルに変換することで、割り当てを節約することもできます。

この時点で、`hello_macro` と `hello_macro_derive` の両方で `cargo build` が正常に完了するはずです。この手続き型マクロを実際に使ってみましょう！リスト19-30のコードにこれらのクレートを接続します。`cargo new pancakes` を使って、`project` ディレクトリに新しいバイナリプロジェクトを作成します。`pancakes` クレートの `Cargo.toml` に `hello_macro` と `hello_macro_derive` を依存関係として追加する必要があります。`hello_macro` と `hello_macro_derive` のバージョンを *https://crates.io* に公開する場合は、通常の依存関係になります。そうでない場合は、次のように `path` 依存関係として指定できます。

    [dependencies]
    hello_macro = { path = "../hello_macro" }
    hello_macro_derive = { path = "../hello_macro/hello_macro_derive" }

リスト19-30のコードを `src/main.rs` に入れ、`cargo run` を実行します。`Hello, Macro! My name is Pancakes!` と出力されるはずです。手続き型マクロによる `HelloMacro` トレイトの実装が、`pancakes` クレートが実装する必要なく含まれました。`#[derive(HelloMacro)]` により、トレイトの実装が追加されました。

次に、他の種類の手続き型マクロがカスタム `derive` マクロとどのように異なるかを調べましょう。
