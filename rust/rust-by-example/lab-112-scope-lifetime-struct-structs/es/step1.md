# Structs

La anotación de lifetimes en estructuras también es similar a las funciones:

```rust
// Un tipo `Borrowed` que contiene una referencia a un
// `i32`. La referencia a `i32` debe sobrevivir a `Borrowed`.
#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

// Del mismo modo, ambas referencias aquí deben sobrevivir a esta estructura.
#[derive(Debug)]
struct NamedBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

// Un enum que puede ser un `i32` o una referencia a uno.
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
