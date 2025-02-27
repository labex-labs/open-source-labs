# En tant que paramètres d'entrée

Alors que Rust choisit généralement comment capturer les variables dynamiquement sans annotation de type, cette ambiguïté n'est pas autorisée lorsqu'on écrit des fonctions. Lorsqu'on prend une closure en tant que paramètre d'entrée, le type complet de la closure doit être annoté à l'aide d'un des `traits`, et ils sont déterminés par ce que la closure fait avec la valeur capturée. Dans l'ordre décroissant de restriction, ils sont :

- `Fn` : la closure utilise la valeur capturée par référence (`&T`)
- `FnMut` : la closure utilise la valeur capturée par référence mutable (`&mut T`)
- `FnOnce` : la closure utilise la valeur capturée par valeur (`T`)

Sur une base variable par variable, le compilateur capturera les variables de la manière la moins restrictive possible.

Par exemple, considérez un paramètre annoté comme `FnOnce`. Cela spécifie que la closure _peut_ capturer par `&T`, `&mut T` ou `T`, mais le compilateur choisira finalement en fonction de la manière dont les variables capturées sont utilisées dans la closure.

Cela est dû au fait que si un déplacement est possible, alors n'importe quel type d'emprunt devrait également être possible. Notez que l'inverse n'est pas vrai. Si le paramètre est annoté comme `Fn`, alors la capture de variables par `&mut T` ou `T` n'est pas autorisée. Cependant, `&T` est autorisée.

Dans l'exemple suivant, essayez d'échanger l'utilisation de `Fn`, `FnMut` et `FnOnce` pour voir ce qui se passe :

```rust
// Une fonction qui prend une closure en argument et l'appelle.
// <F> indique que F est un "paramètre de type générique"
fn apply<F>(f: F) where
    // La closure prend aucune entrée et ne renvoie rien.
    F: FnOnce() {
    // ^ TODO: Essayez de changer ceci en `Fn` ou `FnMut`.

    f();
}

// Une fonction qui prend une closure et renvoie un `i32`.
fn apply_to_3<F>(f: F) -> i32 where
    // La closure prend un `i32` et renvoie un `i32`.
    F: Fn(i32) -> i32 {

    f(3)
}

fn main() {
    use std::mem;

    let greeting = "hello";
    // Un type non copiable.
    // `to_owned` crée des données propriétaires à partir d'un emprunt
    let mut farewell = "goodbye".to_owned();

    // Capture 2 variables : `greeting` par référence et
    // `farewell` par valeur.
    let diary = || {
        // `greeting` est par référence : nécessite `Fn`.
        println!("I said {}.", greeting);

        // La mutation force `farewell` à être capturé par
        // référence mutable. Maintenant nécessite `FnMut`.
        farewell.push_str("!!!");
        println!("Then I screamed {}.", farewell);
        println!("Now I can sleep. zzzzz");

        // Appel manuel de drop force `farewell` à
        // être capturé par valeur. Maintenant nécessite `FnOnce`.
        mem::drop(farewell);
    };

    // Appelez la fonction qui applique la closure.
    apply(diary);

    // `double` satisfait la contrainte de trait de `apply_to_3`
    let double = |x| 2 * x;

    println!("3 doubled: {}", apply_to_3(double));
}
```
