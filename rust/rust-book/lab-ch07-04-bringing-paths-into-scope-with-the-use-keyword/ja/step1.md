# use キーワードを使ってパスをスコープに持ち込む

関数を呼び出すためのパスを書き出す必要があると、不便で繰り返しに感じることがあります。リスト 7-7 では、`add_to_waitlist` 関数への絶対パスまたは相対パスを選択した場合でも、`add_to_waitlist` を呼び出したいたびに、`front_of_house` と `hosting` も指定する必要がありました。幸いなことに、このプロセスを簡略化する方法があります。`use` キーワードを使ってパスのショートカットを一度作成し、その後、スコープ内の他の場所では短い名前を使用することができます。

リスト 7-11 では、`crate::front_of_house::hosting` モジュールを `eat_at_restaurant` 関数のスコープに持ち込み、`eat_at_restaurant` で `add_to_waitlist` 関数を呼び出すために、`hosting::add_to_waitlist` を指定するだけで済むようにします。

ファイル名：`src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

リスト 7-11: `use` を使ってモジュールをスコープに持ち込む

スコープ内に `use` とパスを追加することは、ファイルシステムにシンボリック リンクを作成するのと似ています。クレート ルートに `use crate::front_of_house::hosting` を追加することで、`hosting` はそのスコープ内で有効な名前になります。`hosting` モジュールがクレート ルートに定義されているかのようです。`use` でスコープに持ち込まれたパスも、他のパスと同様に、プライバシーをチェックします。

`use` は、`use` が発生する特定のスコープに対してのみショートカットを作成することに注意してください。リスト 7-12 では、`eat_at_restaurant` 関数を新しい子モジュール `customer` に移動します。このとき、`customer` は `use` 文とは異なるスコープになるため、関数本体はコンパイルされません。

ファイル名：`src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
    }
}
```

リスト 7-12: `use` 文はそのスコープ内でのみ適用されます。

コンパイラのエラーは、`customer` モジュール内ではショートカットがもはや適用されないことを示しています。

```bash
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
  --> src/lib.rs:11:9
   |
11 |         hosting::add_to_waitlist();
   |         ^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default
```

`use` がそのスコープ内でもはや使用されていないことを示す警告もあることに注意してください。この問題を解決するには、`customer` モジュール内にも `use` を移動するか、子モジュール `customer` 内で親モジュールのショートカットを `super::hosting` で参照します。
