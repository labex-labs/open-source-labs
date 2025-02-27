# Structs

Die Angabe von Lebensdauern in Strukturen ähnelt auch der von Funktionen:

```rust
// Ein Typ `Borrowed`, der eine Referenz auf ein
// `i32` enthält. Die Referenz auf `i32` muss die Lebensdauer von `Borrowed` überdauern.
#[derive(Debug)]
struct Borrowed<'a>(&'a i32);

// Ebenso müssen hier beide Referenzen die Lebensdauer dieser Struktur überdauern.
#[derive(Debug)]
struct NamedBorrowed<'a> {
    x: &'a i32,
    y: &'a i32,
}

// Eine Enumeration, die entweder ein `i32` oder eine Referenz auf eines ist.
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

    println!("x wird in {:?} entliehen", single);
    println!("x und y werden in {:?} entliehen", double);
    println!("x wird in {:?} entliehen", reference);
    println!("y wird *nicht* in {:?} entliehen", number);
}
```
