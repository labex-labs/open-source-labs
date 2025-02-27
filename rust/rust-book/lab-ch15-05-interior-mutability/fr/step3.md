# Mutabilité interne : Un emprunt mutable à une valeur immuable

Une conséquence des règles d'emprunt est que lorsqu'on a une valeur immuable, on ne peut pas l'emprunter mutuellement. Par exemple, ce code ne compilera pas :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = &mut x;
}
```

Si vous essayez de compiler ce code, vous obtiendrez l'erreur suivante :

```bash
error[E0596]: cannot borrow `x` as mutable, as it is not declared
as mutable
 --> src/main.rs:3:13
  |
2 |     let x = 5;
  |         - help: consider changing this to be mutable: `mut x`
3 |     let y = &mut x;
  |             ^^^^^^ cannot borrow as mutable
```

Cependant, il existe des situations dans lesquelles il serait utile qu'une valeur se modifie elle-même dans ses méthodes, mais qu'elle apparaisse immuable pour le reste du code. Le code situé en dehors des méthodes de la valeur ne serait pas en mesure de modifier la valeur. L'utilisation de `RefCell<T>` est un moyen d'obtenir la capacité de mutabilité interne, mais `RefCell<T>` ne contourne pas complètement les règles d'emprunt : l'analyseur d'emprunt du compilateur autorise cette mutabilité interne, et les règles d'emprunt sont vérifiées à l'exécution au lieu de la compilation. Si vous violez les règles, vous obtiendrez une `panic!` au lieu d'une erreur du compilateur.

Examînons un exemple pratique où nous pouvons utiliser `RefCell<T>` pour modifier une valeur immuable et voyons pourquoi cela est utile.
