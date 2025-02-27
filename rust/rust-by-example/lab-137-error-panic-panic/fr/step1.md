# `panic`

Le mécanisme de gestion d'erreurs le plus simple que nous allons voir est `panic`. Il imprime un message d'erreur, commence à dérouler la pile et quitte généralement le programme. Ici, nous appelons explicitement `panic` dans notre condition d'erreur :

```rust
fn drink(beverage: &str) {
    // Vous ne devriez pas boire trop de boissons sucrées.
    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Some refreshing {} is all I need.", beverage);
}

fn main() {
    drink("water");
    drink("lemonade");
}
```
