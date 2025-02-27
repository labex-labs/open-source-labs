# En tant que paramètres de sortie

Il est possible d'utiliser des closures comme paramètres d'entrée, donc il devrait également être possible de renvoyer des closures comme paramètres de sortie. Cependant, les types de closures anonymes sont, par définition, inconnus, donc nous devons utiliser `impl Trait` pour les renvoyer.

Les traits valides pour renvoyer une closure sont :

- `Fn`
- `FnMut`
- `FnOnce`

En outre, le mot clé `move` doit être utilisé, ce qui indique que toutes les captures se produisent par valeur. Cela est nécessaire car toute capture par référence serait supprimée dès que la fonction se termine, laissant des références invalides dans la closure.

```rust
fn create_fn() -> impl Fn() {
    let text = "Fn".to_owned();

    move || println!("This is a: {}", text)
}

fn create_fnmut() -> impl FnMut() {
    let text = "FnMut".to_owned();

    move || println!("This is a: {}", text)
}

fn create_fnonce() -> impl FnOnce() {
    let text = "FnOnce".to_owned();

    move || println!("This is a: {}", text)
}

fn main() {
    let fn_plain = create_fn();
    let mut fn_mut = create_fnmut();
    let fn_once = create_fnonce();

    fn_plain();
    fn_mut();
    fn_once();
}
```
