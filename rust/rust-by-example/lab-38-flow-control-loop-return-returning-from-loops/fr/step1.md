# Retour de boucles

L'une des utilisations d'une boucle `loop` est de réessayer une opération jusqu'à ce qu'elle réussisse. Cependant, si l'opération renvoie une valeur, vous devrez peut-être la passer au reste du code : placez-la après le `break`, et elle sera renvoyée par l'expression `loop`.

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    assert_eq!(result, 20);
}
```
