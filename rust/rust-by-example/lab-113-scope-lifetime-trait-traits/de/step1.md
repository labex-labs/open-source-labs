# Traits

Die Angabe von Lebensdauern in Trait-Methoden ist im Grunde ähnlich wie bei Funktionen. Beachten Sie, dass `impl` ebenfalls eine Angabe von Lebensdauern haben kann.

```rust
// Eine Struktur mit Angabe von Lebensdauern.
#[derive(Debug)]
struct Borrowed<'a> {
    x: &'a i32,
}

// Lebensdauern für impl angeben.
impl<'a> Default for Borrowed<'a> {
    fn default() -> Self {
        Self {
            x: &10,
        }
    }
}

fn main() {
    let b: Borrowed = Default::default();
    println!("b ist {:?}", b);
}
```
