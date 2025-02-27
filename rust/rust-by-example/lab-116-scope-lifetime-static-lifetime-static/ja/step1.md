# 静的なもの

Rust にはいくつかの予約済みの寿命名があります。その1つが `'static` です。2つの状況で遭遇するかもしれません。

```rust
// 'static寿命を持つ参照:
let s: &'static str = "hello world";

// トレイト境界の一部としての 'static:
fn generic<T>(x: T) where T: 'static {}
```

どちらも関連していますが、微妙に異なり、これはRustを学ぶ際の混乱の一般的な原因です。以下は、それぞれの状況の例です。

## 参照寿命

参照寿命としての `'static` は、参照によって指されるデータが実行中のプログラムの生存期間全体にわたって存在することを示します。それでも、短い寿命に強制変換することができます。

`'static` 寿命を持つ変数を作成する方法は2つあり、どちらもバイナリの読み取り専用メモリに格納されます。

- `static` 宣言で定数を作成する。
- 型が `&'static str` である `string` リテラルを作成する。

各方法の表示については、以下の例を参照してください。

```rust
// 'static寿命を持つ定数を作成する。
static NUM: i32 = 18;

// 入力引数の寿命に 'static寿命を強制変換して、NUMへの参照を返す。
fn coerce_static<'a>(_: &'a i32) -> &'a i32 {
    &NUM
}

fn main() {
    {
        // `string` リテラルを作成して表示する:
        let static_string = "I'm in read-only memory";
        println!("static_string: {}", static_string);

        // `static_string` がスコープ外になると、参照はもはや使用できなくなりますが、データはバイナリに残ります。
    }

    {
        // `coerce_static` に使用する整数を作成する:
        let lifetime_num = 9;

        // `NUM` を `lifetime_num` の寿命に強制変換する:
        let coerced_static = coerce_static(&lifetime_num);

        println!("coerced_static: {}", coerced_static);
    }

    println!("NUM: {} stays accessible!", NUM);
}
```

## トレイト境界

トレイト境界としては、型に非静的な参照が含まれていないことを意味します。たとえば、受信者は好きなだけ型を保持でき、破棄するまで無効になることはありません。

所有されたデータは常に `'static` 寿命境界を通過するが、その所有されたデータへの参照は一般的に通過しないことを理解することが重要です。

```rust
use std::fmt::Debug;

fn print_it( input: impl Debug + 'static ) {
    println!( "'static value passed in is: {:?}", input );
}

fn main() {
    // iは所有されており、参照を含まないため、'staticです:
    let i = 5;
    print_it(i);

    // うーん、&iはmain()のスコープによって定義された寿命のみを持っているため、'staticではありません:
    print_it(&i);
}
```

コンパイラは次のように表示します。

```ignore
error[E0597]: `i` does not live long enough
  --> src/lib.rs:15:15
   |
15 |     print_it(&i);
   |     ---------^^--
   |     |         |
   |     |         borrowed value does not live long enough
   |     argument requires that `i` is borrowed for `'static`
16 | }
   | - `i` dropped here while still borrowed
```
