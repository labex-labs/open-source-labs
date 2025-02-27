# Méthodes

Les méthodes sont annotées de manière similaire aux fonctions :

```rust
struct Owner(i32);

impl Owner {
    // Annoter les durées de vie comme dans une fonction autonome.
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
