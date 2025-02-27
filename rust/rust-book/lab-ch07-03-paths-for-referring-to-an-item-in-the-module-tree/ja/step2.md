# `pub` キーワードを使用したパスの公開

リスト7-4のエラーに戻りましょう。そのエラーは、`hosting` モジュールが非公開であることを伝えていました。親モジュール内の `eat_at_restaurant` 関数が子モジュール内の `add_to_waitlist` 関数にアクセスできるようにするため、`hosting` モジュールを `pub` キーワードでマークします。これは、リスト7-5に示すようになります。

ファイル名: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        fn add_to_waitlist() {}
    }
}

--snip--
```

リスト7-5: `eat_at_restaurant` から使用するために `hosting` モジュールを `pub` として宣言する

残念ながら、リスト7-5のコードは依然としてコンパイラエラーを引き起こします。これは、リスト7-6に示すようになります。

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: function `add_to_waitlist` is private
 --> src/lib.rs:9:37
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                                     ^^^^^^^^^^^^^^^ private function
  |
note: the function `add_to_waitlist` is defined here
 --> src/lib.rs:3:9
  |
3 |         fn add_to_waitlist() {}
  |         ^^^^^^^^^^^^^^^^^^^^

error[E0603]: function `add_to_waitlist` is private
  --> src/lib.rs:12:30
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                              ^^^^^^^^^^^^^^^ private function
   |
note: the function `add_to_waitlist` is defined here
  --> src/lib.rs:3:9
   |
3  |         fn add_to_waitlist() {}
   |         ^^^^^^^^^^^^^^^^^^^^
```

リスト7-6: リスト7-5のコードをビルドしたときのコンパイラエラー

何が起こったのでしょうか？ `mod hosting` の前に `pub` キーワードを追加することで、モジュールが公開されます。この変更により、`front_of_house` にアクセスできる場合、`hosting` にアクセスできるようになります。しかし、`hosting` の **内容** は依然として非公開です。モジュールを公開しても、その内容は公開されません。モジュールの `pub` キーワードは、その祖先モジュール内のコードがそれを参照できるようにするだけで、内部コードにアクセスすることはできません。モジュールはコンテナであるため、モジュールを公開するだけでは何もできません。さらに進んで、モジュール内の1つ以上のアイテムも公開するように選ぶ必要があります。

リスト7-6のエラーは、`add_to_waitlist` 関数が非公開であることを示しています。プライバシールールは、構造体、列挙体、関数、メソッドだけでなく、モジュールにも適用されます。

`add_to_waitlist` 関数の定義の前に `pub` キーワードを追加することで、`add_to_waitlist` 関数も公開しましょう。これは、リスト7-7に示すようになります。

ファイル名: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

--snip--
```

リスト7-7: `mod hosting` と `fn add_to_waitlist` に `pub` キーワードを追加することで、`eat_at_restaurant` から関数を呼び出せるようになります。

今ではコードがコンパイルされます！ `pub` キーワードを追加することで、これらのパスをプライバシールールに関して `add_to_waitlist` で使用できるようになる理由を見てみましょう。絶対パスと相対パスを見てみましょう。

絶対パスでは、クレートのモジュールツリーのルートである `crate` から始まります。`front_of_house` モジュールはクレートのルートに定義されています。`front_of_house` は公開されていませんが、`eat_at_restaurant` 関数は `front_of_house` と同じモジュールに定義されているため（つまり、`eat_at_restaurant` と `front_of_house` は兄弟です）、`eat_at_restaurant` から `front_of_house` を参照できます。次は、`pub` でマークされた `hosting` モジュールです。`hosting` の親モジュールにアクセスできるため、`hosting` にアクセスできます。最後に、`add_to_waitlist` 関数は `pub` でマークされており、その親モジュールにアクセスできるため、この関数呼び出しは機能します！

相対パスでは、最初のステップを除いては絶対パスと同じ論理になります。クレートのルートから始まるのではなく、パスは `front_of_house` から始まります。`front_of_house` モジュールは `eat_at_restaurant` と同じモジュール内に定義されているため、`eat_at_restaurant` が定義されているモジュールから始まる相対パスが機能します。その後、`hosting` と `add_to_waitlist` が `pub` でマークされているため、パスの残りの部分が機能し、この関数呼び出しは有効です！

ライブラリクレートを共有して他のプロジェクトがコードを使用できるようにする予定がある場合、公開APIは、他の人がコードとどのようにやり取りできるかを決定する、クレートのユーザーとの契約になります。公開APIの変更を管理して、人々がクレートに依存しやすくするためには、多くの考慮事項があります。これらの考慮事項は、この本の範囲外です。このトピックに興味がある場合は、*https://rust-lang.github.io/api-guidelines* のRust APIガイドラインを参照してください。

> **バイナリとライブラリを含むパッケージのベストプラクティス**
>
> パッケージには、`src/main.rs` のバイナリクレートルートと `src/lib.rs` のライブラリクレートルートの両方が含まれている場合があり、デフォルトでは両方のクレートにはパッケージ名が付きます。通常、ライブラリとバイナリクレートの両方を含むこのパターンのパッケージは、バイナリクレートには、ライブラリクレートのコードを呼び出す実行可能ファイルを起動するのに十分なコードがあります。これにより、他のプロジェクトがパッケージが提供する最も多くの機能の恩恵を受けることができます。なぜなら、ライブラリクレートのコードを共有できるからです。
>
> モジュールツリーは `src/lib.rs` に定義する必要があります。その後、バイナリクレートでは、パッケージ名から始まるパスを使用して、任意の公開アイテムを使用できます。バイナリクレートは、完全に外部のクレートがライブラリクレートを使用するのと同じように、ライブラリクレートのユーザーになります。それは、公開APIのみを使用できます。これにより、良いAPIを設計するのに役立ちます。自分が作者であるだけでなく、クライアントでもあるからです！
>
> 第12章では、バイナリクレートとライブラリクレートの両方を含むコマンドラインプログラムを使って、この組織的な慣行を示します。
