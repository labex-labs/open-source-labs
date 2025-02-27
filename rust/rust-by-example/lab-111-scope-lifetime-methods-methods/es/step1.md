# Métodos

Los métodos se annotan de manera similar a las funciones:

```rust
struct Owner(i32);

impl Owner {
    // Anota los lifetimes como en una función independiente.
    fn add_one<'a>(&'a mut self) { self.0 += 1; }
    fn print<'a>(&'a self) {
        println!("`print`: {}", self.0);
    }
}

fn main() {
    let mut owner = Owner(18);

    owner.add_one();
    owner.print();
}
```
