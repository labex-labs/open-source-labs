# Retourner des valeurs à partir de boucles

L'une des utilisations d'une boucle `loop` est de réessayer une opération que vous savez peut échouer, comme vérifier si un thread a terminé son travail. Vous pourriez également avoir besoin de passer le résultat de cette opération en dehors de la boucle pour le reste de votre code. Pour ce faire, vous pouvez ajouter la valeur que vous voulez retourner après l'expression `break` que vous utilisez pour arrêter la boucle ; cette valeur sera retournée en dehors de la boucle pour que vous puissiez l'utiliser, comme le montre ici :

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("Le résultat est {result}");
}
```

Avant la boucle, nous déclarons une variable nommée `counter` et l'initialisons à `0`. Ensuite, nous déclarons une variable nommée `result` pour stocker la valeur retournée par la boucle. A chaque itération de la boucle, nous ajoutons `1` à la variable `counter`, puis vérifions si `counter` est égal à `10`. Lorsque c'est le cas, nous utilisons le mot-clé `break` avec la valeur `counter * 2`. Après la boucle, nous utilisons un point-virgule pour terminer l'instruction qui attribue la valeur à `result`. Enfin, nous affichons la valeur de `result`, qui est dans ce cas `20`.
