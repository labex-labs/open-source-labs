# `cfg`

Il est possible de réaliser des vérifications conditionnelles de configuration grâce à deux opérateurs différents :

- l'attribut `cfg` : `#[cfg(...)]` en position d'attribut
- le macro `cfg!` : `cfg!(...)` dans des expressions booléennes

Alors que le premier active la compilation conditionnelle, le second évalue conditionnellement à des littéraux `true` ou `false`, permettant des vérifications au moment de l'exécution. Les deux utilisent la même syntaxe d'arguments.

Contrairement à `#[cfg]`, `cfg!` n'enlève aucun code et n'évalue qu'à `true` ou `false`. Par exemple, tous les blocs dans une expression if/else doivent être valides lorsque `cfg!` est utilisé pour la condition, quelle que soit l'évaluation de `cfg!`.

```rust
// Cette fonction n'est compilée que si le système d'exploitation cible est linux
#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("You are running linux!");
}

// Et cette fonction n'est compilée que si le système d'exploitation cible n'est *pas* linux
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("You are *not* running linux!");
}

fn main() {
    are_you_on_linux();

    println!("Are you sure?");
    if cfg!(target_os = "linux") {
        println!("Yes. It's definitely linux!");
    } else {
        println!("Yes. It's definitely *not* linux!");
    }
}
```
