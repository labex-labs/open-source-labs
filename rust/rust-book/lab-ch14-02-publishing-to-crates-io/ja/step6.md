# `pub use` を使った便利なパブリック API のエクスポート

クレートを公開する際には、パブリック API の構造が重要な考慮事項です。クレートを使用する人は、あなたほど API の構造に慣れておらず、大きなモジュール階層を持つクレートの場合、使いたい部分を見つけるのに苦労するかもしれません。

第 7 章では、`pub` キーワードを使って項目を公開する方法と、`use` キーワードを使って項目をスコープに持ち込む方法について説明しました。しかし、クレートを開発している最中には分かりやすい構造であっても、ユーザーにとっては必ずしも便利ではない場合があります。たとえば、構造体を多段階の階層に組織化することが考えられますが、その場合、階層の奥に定義された型を使おうとする人は、その型が存在することを知るのに苦労するかもしれません。また、`use` `my_crate::`some_module`::`another_module`::`UsefulType`;` と入力するのが面倒くさく、`use` `my_crate::`UsefulType`;` のように書きたいと思うかもしれません。

幸いなことに、他のライブラリから使いにくい構造の場合、内部組織を再配置する必要はありません。代わりに、`pub use` を使って項目を再エクスポートして、内部構造とは異なるパブリック構造を作成することができます。_再エクスポート_ は、ある場所のパブリック項目を取り出して、別の場所で公開するもので、その項目が別の場所に定義されているかのように見えます。

たとえば、アート的な概念をモデリングするための `art` という名前のライブラリを作ったとします。このライブラリには 2 つのモジュールがあります。`kinds` モジュールには `PrimaryColor` と `SecondaryColor` という 2 つの列挙型が含まれ、`utils` モジュールには `mix` という名前の関数が含まれています。リスト 14-3 を参照してください。

ファイル名：`src/lib.rs`

```rust
//! # Art
//!
//! A library for modeling artistic concepts.

pub mod kinds {
    /// The primary colors according to the RYB color model.
    pub enum PrimaryColor {
        Red,
        Yellow,
        Blue,
    }

    /// The secondary colors according to the RYB color model.
    pub enum SecondaryColor {
        Orange,
        Green,
        Purple,
    }
}

pub mod utils {
    use crate::kinds::*;

    /// Combines two primary colors in equal amounts to create
    /// a secondary color.
    pub fn mix(
        c1: PrimaryColor,
        c2: PrimaryColor,
    ) -> SecondaryColor {
        --snip--
    }
}
```

リスト 14-3: `kinds` と `utils` モジュールに項目を組織化した `art` ライブラリ

図 14-3 は、`cargo doc` によって生成されるこのクレートのドキュメントの最初のページの様子を示しています。

図 14-3: `kinds` と `utils` モジュールをリストする `art` のドキュメントの最初のページ

`PrimaryColor` と `SecondaryColor` 型は最初のページに表示されず、`mix` 関数も表示されません。それらを見るには、`kinds` と `utils` をクリックする必要があります。

このライブラリに依存する別のクレートでは、`art` からの項目をスコープに持ち込むための `use` 文が必要で、現在定義されているモジュール構造を指定する必要があります。リスト 14-4 は、`art` クレートの `PrimaryColor` と `mix` 項目を使うクレートの例を示しています。

ファイル名：`src/main.rs`

```rust
use art::kinds::PrimaryColor;
use art::utils::mix;

fn main() {
    let red = PrimaryColor::Red;
    let yellow = PrimaryColor::Yellow;
    mix(red, yellow);
}
```

リスト 14-4: 内部構造をエクスポートした `art` クレートの項目を使うクレート

リスト 14-4 のコードの作者は、`PrimaryColor` が `kinds` モジュールにあり、`mix` が `utils` モジュールにあることを把握する必要がありました。`art` クレートのモジュール構造は、`art` クレートを開発する開発者にとってはより関連性が高いものの、それを使用する人にとっては有用な情報を含んでいません。むしろ混乱を招きます。なぜなら、使用する開発者はどこを見るべきかを判断しなければならず、`use` 文でモジュール名を指定する必要があるからです。

パブリック API から内部組織を取り除くには、リスト 14-3 の `art` クレートのコードを変更して、`pub use` 文を追加して項目をトップレベルで再エクスポートします。リスト 14-5 を参照してください。

ファイル名：`src/lib.rs`

```rust
//! # Art
//!
//! A library for modeling artistic concepts.

pub use self::kinds::PrimaryColor;
pub use self::kinds::SecondaryColor;
pub use self::utils::mix;

pub mod kinds {
    --snip--
}

pub mod utils {
    --snip--
}
```

リスト 14-5: 項目を再エクスポートするための `pub use` 文の追加

このクレートに対して `cargo doc` が生成する API ドキュメントは、現在、最初のページに再エクスポートをリストしてリンク付けします。図 14-4 を参照してください。これにより、`PrimaryColor` と `SecondaryColor` 型および `mix` 関数を見つけやすくなります。

図 14-4: 再エクスポートをリストする `art` のドキュメントの最初のページ

`art` クレートのユーザーは、リスト 14-4 に示すように、リスト 14-3 の内部構造を依然として見ることができ、使用することもできます。または、リスト 14-6 に示すように、リスト 14-5 のより便利な構造を使用することもできます。

ファイル名：`src/main.rs`

```rust
use art::mix;
use art::PrimaryColor;

fn main() {
    --snip--
}
```

リスト 14-6: `art` クレートから再エクスポートされた項目を使用するプログラム

多くのネストされたモジュールがある場合、`pub use` を使ってトップレベルで型を再エクスポートすることは、クレートを使用する人の経験に大きな違いをもたらすことができます。`pub use` のもう 1 つの一般的な使い方は、現在のクレートにおける依存関係の定義を再エクスポートして、そのクレートの定義を自分のクレートのパブリック API の一部にすることです。

便利なパブリック API 構造を作成することは、科学よりも芸術に近いものであり、ユーザーに最適な API を見つけるために反復することができます。`pub use` を選択することで、クレートの内部構造をどのように構築するかに柔軟性が与えられ、その内部構造とユーザーに提示するものを切り離すことができます。インストールしたクレートのコードを見て、その内部構造とパブリック API が異なるかどうかを確認してみてください。
