# Fonctions divergentes

Les fonctions divergentes ne retournent jamais. Elles sont marquées avec `!`, qui est un type vide.

```rust
fn foo() ->! {
    panic!("Cette appel ne retourne jamais.");
}
```

Contrairement à tous les autres types, celui-ci ne peut pas être instancié, car l'ensemble de toutes les valeurs possibles que ce type peut avoir est vide. Notez que, il est différent du type `()`, qui a exactement une valeur possible.

Par exemple, cette fonction retourne comme d'habitude, bien qu'il n'y ait aucune information dans la valeur de retour.

```rust
fn some_fn() {
    ()
}

fn main() {
    let _a: () = some_fn();
    println!("Cette fonction retourne et vous pouvez voir cette ligne.");
}
```

Contrairement à cette fonction, qui ne renverra jamais le contrôle à l'appelant.

```rust
#![feature(never_type)]

fn main() {
    let x:! = panic!("Cette appel ne retourne jamais.");
    println!("Vous ne verrez jamais cette ligne!");
}
```

Bien que cela puisse sembler un concept abstrait, il est en fait très utile et souvent pratique. L'avantage principal de ce type est qu'il peut être converti en n'importe quel autre type et donc utilisé à des endroits où un type exact est requis, par exemple dans les branches `match`. Cela nous permet d'écrire du code comme ceci :

```rust
fn main() {
    fn sum_odd_numbers(up_to: u32) -> u32 {
        let mut acc = 0;
        for i in 0..up_to {
            // Remarquez que le type de retour de cette expression match doit être u32
            // en raison du type de la variable "addition".
            let addition: u32 = match i%2 == 1 {
                // La variable "i" est de type u32, ce qui est parfaitement correct.
                true => i,
                // D'un autre côté, l'expression "continue" ne retourne pas
                // u32, mais cela va quand même, car elle ne retourne jamais et donc
                // ne viole pas les exigences de type de l'expression match.
                false => continue,
            };
            acc += addition;
        }
        acc
    }
    println!("Somme des nombres impairs jusqu'à 9 (exclu) : {}", sum_odd_numbers(9));
}
```

C'est également le type de retour des fonctions qui bouclent à l'infini (par exemple `loop {}`) comme les serveurs réseau ou des fonctions qui terminent le processus (par exemple `exit()`).
