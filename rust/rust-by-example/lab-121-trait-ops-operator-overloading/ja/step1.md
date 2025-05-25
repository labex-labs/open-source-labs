# 演算子のオーバーロード

Rust では、多くの演算子をトレイトを通じてオーバーロードできます。つまり、一部の演算子は入力引数に基づいて異なるタスクを実行するために使用できます。これは、演算子がメソッド呼び出しのシンタックス・シュガーであるため可能です。たとえば、`a + b`の`+`演算子は`add`メソッドを呼び出します（`a.add(b)`のように）。この`add`メソッドは`Add`トレイトの一部です。したがって、`+`演算子は`Add`トレイトの実装者によって使用できます。

演算子をオーバーロードするトレイト（`Add`など）の一覧は、`core::ops`にあります。

```rust
use std::ops;

struct Foo;
struct Bar;

#[derive(Debug)]
struct FooBar;

#[derive(Debug)]
struct BarFoo;

// `std::ops::Add` トレイトは、`+` の機能を指定するために使用されます。
// ここでは、`Add<Bar>` を作成します。これは、右辺の型が `Bar` の加算用のトレイトです。
// 次のブロックでは、演算子の操作を実装します。Foo + Bar = FooBar
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        println!("> Foo.add(Bar) was called");

        FooBar
    }
}

// 型を逆にすることで、非可換な加算を実装します。
// ここでは、`Add<Foo>` を作成します。これは、右辺の型が `Foo` の加算用のトレイトです。
// このブロックでは、演算子の操作を実装します。Bar + Foo = BarFoo
impl ops::Add<Foo> for Bar {
    type Output = BarFoo;

    fn add(self, _rhs: Foo) -> BarFoo {
        println!("> Bar.add(Foo) was called");

        BarFoo
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
    println!("Bar + Foo = {:?}", Bar + Foo);
}
```
