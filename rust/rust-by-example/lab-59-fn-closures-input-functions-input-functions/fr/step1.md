# Fonctions d'entrée

Puisque les closures peuvent être utilisées comme arguments, vous vous demandez peut-être si c'est également le cas pour les fonctions. Et en effet, c'est possible! Si vous déclarez une fonction qui prend une closure comme paramètre, alors n'importe quelle fonction qui satisfait la contrainte de trait de cette closure peut être passée en tant que paramètre.

```rust
// Définissez une fonction qui prend un argument générique `F`
// limité par `Fn`, et l'appelez
fn call_me<F: Fn()>(f: F) {
    f();
}

// Définissez une fonction wrapper satisfaisant la contrainte `Fn`
fn function() {
    println!("Je suis une fonction!");
}

fn main() {
    // Définissez une closure satisfaisant la contrainte `Fn`
    let closure = || println!("Je suis une closure!");

    call_me(closure);
    call_me(function);
}
```

Pour information supplémentaire, les traits `Fn`, `FnMut` et `FnOnce` déterminent la manière dont une closure capture les variables du scope entourant.
