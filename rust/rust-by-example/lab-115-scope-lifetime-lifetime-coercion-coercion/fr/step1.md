# Coercition

Une durée de vie plus longue peut être coercée en une durée de vie plus courte de manière à ce qu'elle fonctionne dans une portée dans laquelle elle ne fonctionnerait normalement pas. Cela se présente sous la forme d'une coercition inférée par le compilateur Rust, mais également sous la forme de la déclaration d'une différence de durée de vie :

```rust
// Ici, Rust infère une durée de vie aussi courte que possible.
// Les deux références sont ensuite coercées vers cette durée de vie.
fn multiply<'a>(first: &'a i32, second: &'a i32) -> i32 {
    first * second
}

// `< 'a: 'b, 'b>` s'interprète comme la durée de vie `'a` est au moins aussi longue que `'b`.
// Ici, nous prenons un `&'a i32` et retournons un `&'b i32` suite à la coercition.
fn choose_first<'a: 'b, 'b>(first: &'a i32, _: &'b i32) -> &'b i32 {
    first
}

fn main() {
    let first = 2; // Durée de vie plus longue

    {
        let second = 3; // Durée de vie plus courte

        println!("Le produit est {}", multiply(&first, &second));
        println!("{} est le premier", choose_first(&first, &second));
    };
}
```
