# Interfaces variadiques

Une interface _variadique_ prend un nombre arbitraire d'arguments. Par exemple, `println!` peut prendre un nombre arbitraire d'arguments, tel que déterminé par la chaîne de formatage.

Nous pouvons étendre la macro `calculate!` de la section précédente pour qu'elle soit variadique :

```rust
macro_rules! calculate {
    // Le motif pour un seul `eval`
    (eval $e:expr) => {
        {
            let val: usize = $e; // Forcer les types à être des entiers
            println!("{} = {}", stringify!{$e}, val);
        }
    };

    // Découper plusieurs `eval`s de manière récursive
    (eval $e:expr, $(eval $es:expr),+) => {{
        calculate! { eval $e }
        calculate! { $(eval $es),+ }
    }};
}

fn main() {
    calculate! { // Regardez-moi! `calculate!` variadique!
        eval 1 + 2,
        eval 3 + 4,
        eval (2 * 3) + 1
    }
}
```

Sortie :

```txt
1 + 2 = 3
3 + 4 = 7
(2 * 3) + 1 = 7
```
