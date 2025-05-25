# _Traits_ (Traços)

A anotação de _lifetimes_ (tempo de vida) em métodos de _trait_ (traço) é basicamente semelhante às funções. Note que `impl` também pode ter anotações de _lifetimes_.

```rust
// Uma struct com anotação de lifetimes.
#[derive(Debug)]
struct Borrowed<'a> {
    x: &'a i32,
}

// Anotar lifetimes para impl.
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
