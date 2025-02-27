# Traits

La anotación de los períodos de vida en los métodos de trato es básicamente similar a las funciones. Tenga en cuenta que `impl` también puede tener una anotación de períodos de vida.

```rust
// Una estructura con anotación de períodos de vida.
#[derive(Debug)]
struct Borrowed<'a> {
    x: &'a i32,
}

// Anota los períodos de vida para impl.
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
