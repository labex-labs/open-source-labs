# Structs

L'annotation des durées de vie dans les structures est également similaire aux fonctions :

```rust
// Un type `Borrowed` qui contient une référence à un
// `i32`. La référence à `i32` doit exister plus longtemps que `Borrowed`.
#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

// De même, les deux références ici doivent exister plus longtemps que cette structure.
#[derive(Debug)]
struct NamedBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

// Un enum qui est soit un `i32` soit une référence à un `i32`.
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

    println!("x est emprunté dans {:?}", single);
    println!("x et y sont empruntés dans {:?}", double);
    println!("x est emprunté dans {:?}", reference);
    println!("y n'est *pas* emprunté dans {:?}", number);
}
```
