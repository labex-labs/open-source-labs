# Structs (Estruturas)

A anotação de _lifetimes_ (tempo de vida) em estruturas também é semelhante às funções:

```rust
// Um tipo `Borrowed` que armazena uma referência a um
// `i32`. A referência a `i32` deve sobreviver a `Borrowed`.
#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

// Similarmente, ambas as referências aqui devem sobreviver a esta estrutura.
#[derive(Debug)]
struct NamedBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

// Um enum que é um `i32` ou uma referência a um.
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
