# Opérations non sécurisées

Comme introduction à cette section, pour citer les docs officielles, "on devrait essayer de minimiser la quantité de code non sécurisé dans une base de code". Ayant cela à l'esprit, commençons! Les annotations non sécurisées en Rust sont utilisées pour contourner les protections mises en place par le compilateur; plus précisément, il y a quatre choses principales pour lesquelles le mot clé `unsafe` est utilisé :

- déréférencer des pointeurs bruts
- appeler des fonctions ou des méthodes qui sont `unsafe` (y compris appeler une fonction via l'FFI, voir [un chapitre précédent du livre)
- accéder ou modifier des variables statiques mutables
- implémenter des traits non sécurisés

## Pointeurs bruts

Les pointeurs bruts `*` et les références `&T` fonctionnent de manière similaire, mais les références sont toujours sûres car elles sont garanties pointer vers des données valides grâce au borrow checker. La déréférencement d'un pointeur brut ne peut être effectué que dans un bloc `unsafe`.

```rust
fn main() {
    let raw_p: *const u32 = &10;

    unsafe {
        assert!(*raw_p == 10);
    }
}
```

## Appel de fonctions non sécurisées

Certaines fonctions peuvent être déclarées comme `unsafe`, ce qui signifie que c'est à l'auteur du programme de s'assurer de la correction au lieu du compilateur. Un exemple de cela est \[`std::slice::from_raw_parts`\] qui créera une slice à partir d'un pointeur vers le premier élément et d'une longueur donnée.

```rust
use std::slice;

fn main() {
    let some_vector = vec![1, 2, 3, 4];

    let pointer = some_vector.as_ptr();
    let length = some_vector.len();

    unsafe {
        let my_slice: &[u32] = slice::from_raw_parts(pointer, length);

        assert_eq!(some_vector.as_slice(), my_slice);
    }
}
```

Pour `slice::from_raw_parts`, l'une des hypothèses qui _doit_ être respectée est que le pointeur passé en paramètre pointe vers une mémoire valide et que la mémoire pointée est du bon type. Si ces invariants ne sont pas respectés, le comportement du programme est indéfini et on ne sait pas ce qui va se passer.
