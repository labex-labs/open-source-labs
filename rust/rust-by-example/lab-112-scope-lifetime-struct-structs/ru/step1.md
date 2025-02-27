# Структуры

Аннотация времени жизни в структурах также похожа на функции:

```rust
// Тип `Borrowed`, который хранит ссылку на
// `i32`. Ссылка на `i32` должна существовать дольше `Borrowed`.
#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

// Аналогично, обе ссылки здесь должны существовать дольше этой структуры.
#[derive(Debug)]
struct NamedBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

// Перечисление, которое может быть либо `i32`, либо ссылкой на него.
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
