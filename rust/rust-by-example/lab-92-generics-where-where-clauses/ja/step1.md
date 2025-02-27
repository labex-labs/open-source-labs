# where句

境界は、型の最初の言及の直前ではなく、開き括弧 `{` の直前に `where` 句を使っても表現できます。また、`where` 句は型パラメータに限らず、任意の型に境界を適用することができます。

`where` 句が役に立ついくつかのケース:

- ジェネリック型と境界を別々に指定する方が明確な場合:

```rust
impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

// where句を使って境界を表現する
impl <A, D> MyTrait<A, D> for YourType where
    A: TraitB + TraitC,
    D: TraitE + TraitF {}
```

- `where` 句を使う方が通常の構文を使うよりも表現力がある場合。この例の `impl` は、`where` 句なしでは直接表現できません:

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

// そうでなければ、これを `T: Debug` として表現しなければならないか、
// 別の間接的なアプローチを使う必要があるため、where句が必要になります:
impl<T> PrintInOption for T where
    Option<T>: Debug {
    // 出力されるのは `Option<T>: Debug` なので、これを境界として使います。
    // そうでなければ、誤った境界を使っています。
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];

    vec.print_in_option();
}
```
