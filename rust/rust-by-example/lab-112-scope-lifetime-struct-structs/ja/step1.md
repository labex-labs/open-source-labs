# 構造体

構造体における寿命の注釈も関数と同様です。

```rust
// `i32` 型への参照を保持する型 `Borrowed`。
// `i32` 型への参照は、`Borrowed` よりも長い寿命を持たなければなりません。
#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

// 同様に、ここにある両方の参照は、この構造体よりも長い寿命を持たなければなりません。
#[derive(Debug)]
struct NamedBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

// `i32` 型またはそれへの参照のいずれかである列挙型。
#[derive(Debug)]
enum Either<'a> {
    Num(i32),
    Ref(&'a i32),
}

fn main() {
    let x = 18;
    let y = 15;

    let single = Borrowed(&x);
    let double = NamedBorrowed { x: &x, y: &y };
    let reference = Either::Ref(&x);
    let number    = Either::Num(y);

    println!("x is borrowed in {:?}", single);
    println!("x and y are borrowed in {:?}", double);
    println!("x is borrowed in {:?}", reference);
    println!("y is *not* borrowed in {:?}", number);
}
```
