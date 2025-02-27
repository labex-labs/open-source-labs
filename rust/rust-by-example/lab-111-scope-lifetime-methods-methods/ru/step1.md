# Методы

Методы аннотируются подобно функциям:

```rust
struct Owner(i32);

impl Owner {
    // Аннотируйте время жизни так, как это делается в отдельной функции.
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
