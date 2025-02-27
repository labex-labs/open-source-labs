# Etiquettes de boucle pour désambiguïser entre plusieurs boucles

Si vous avez des boucles imbriquées, `break` et `continue` s'appliquent à la boucle la plus interne à ce moment-là. Vous pouvez optionnellement spécifier une _étiquette de boucle_ sur une boucle que vous pouvez ensuite utiliser avec `break` ou `continue` pour spécifier que ces mots clés s'appliquent à la boucle étiquetée plutôt qu'à la boucle la plus interne. Les étiquettes de boucle doivent commencer par une simple apostrophe. Voici un exemple avec deux boucles imbriquées :

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

La boucle externe a l'étiquette `'counting_up`, et elle comptera de 0 à 2. La boucle interne sans étiquette compte à rebours de 10 à 9. Le premier `break` qui ne spécifie pas d'étiquette ne sortira que de la boucle interne. L'instruction `break 'counting_up;` sortira de la boucle externe. Ce code affiche :

       Compiling boucles v0.1.0 (file:///projets/boucles)
        Finished dev [unoptimized + debuginfo] target(s) in 0.58s
         Running `target/debug/boucles`
    count = 0
    remaining = 10
    remaining = 9
    count = 1
    remaining = 10
    remaining = 9
    count = 2
    remaining = 10
    End count = 2
