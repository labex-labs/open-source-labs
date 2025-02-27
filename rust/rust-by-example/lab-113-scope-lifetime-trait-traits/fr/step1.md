# Traits

L'annotation des durées de vie dans les méthodes de traits est globalement similaire aux fonctions. Notez que le bloc `impl` peut également avoir une annotation de durée de vie.

```rust
// Une structure avec annotation de durée de vie.
#[derive(Debug)]
struct Borrowed<'a> {
    x: &'a i32,
}

// Annoter les durées de vie pour impl.
impl<'a> Default for Borrowed<'a> {
    fn default() -> Self {
        Self {
            x: &10,
        }
    }
}

fn main() {
    let b: Borrowed = Default::default();
    println!("b is {:?}", b);
}
```
