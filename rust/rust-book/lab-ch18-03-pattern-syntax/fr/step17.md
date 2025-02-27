# @ Liaisons

L'opérateur **au** `@` nous permet de créer une variable qui stocke une valeur en même temps que nous testons cette valeur pour une correspondance de motif. Dans la Liste 18-29, nous voulons tester qu'un champ `id` de type `Message::Hello` est dans la plage `3..=7`. Nous voulons également lier la valeur à la variable `id_variable` afin que nous puissions l'utiliser dans le code associé au bras. Nous pourrions nommer cette variable `id`, comme le champ, mais pour cet exemple, nous utiliserons un nom différent.

Nom de fichier : `src/main.rs`

```rust
enum Message {
    Hello { id: i32 },
}

let msg = Message::Hello { id: 5 };

match msg {
    Message::Hello {
        id: id_variable @ 3..=7,
    } => println!("Found an id in range: {id_variable}"),
    Message::Hello { id: 10..=12 } => {
        println!("Found an id in another range")
    }
    Message::Hello { id } => println!("Some other id: {id}"),
}
```

Liste 18-29 : Utilisation de `@` pour lier une valeur dans un motif tout en la testant

Cet exemple imprimera `Found an id in range: 5`. En spécifiant `id_variable @` avant la plage `3..=7`, nous capturons la valeur qui a correspondu à la plage tout en testant que la valeur correspondait au motif de plage.

Dans le second bras, où nous n'avons spécifié que la plage dans le motif, le code associé au bras n'a pas de variable qui contient la valeur réelle du champ `id`. La valeur du champ `id` aurait pu être 10, 11 ou 12, mais le code associé à ce motif ne sait pas laquelle. Le code du motif n'est pas capable d'utiliser la valeur du champ `id` car nous n'avons pas enregistré la valeur de `id` dans une variable.

Dans le dernier bras, où nous avons spécifié une variable sans plage, nous avons bien la valeur disponible pour l'utiliser dans le code du bras dans une variable nommée `id`. La raison est que nous avons utilisé la syntaxe raccourcie de champ de structure. Mais nous n'avons pas appliqué de test à la valeur dans le champ `id` dans ce bras, comme nous l'avons fait avec les deux premiers bras : n'importe quelle valeur correspondrait à ce motif.

L'utilisation de `@` nous permet de tester une valeur et de la sauvegarder dans une variable à l'intérieur d'un seul motif.
