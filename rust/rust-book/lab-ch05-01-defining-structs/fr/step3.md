# Création d'instances à partir d'autres instances avec la syntaxe de mise à jour de struct

Il est souvent utile de créer une nouvelle instance d'un struct qui inclut la plupart des valeurs d'une autre instance, mais en modifie quelques-unes. Vous pouvez le faire en utilisant la _syntaxe de mise à jour de struct_.

Tout d'abord, dans la Liste 5-6, nous montrons comment créer une nouvelle instance de `User` dans `user2` de manière classique, sans la syntaxe de mise à jour. Nous définissons une nouvelle valeur pour `email`, mais sinon, nous utilisons les mêmes valeurs que celles de `user1` que nous avons créées dans la Liste 5-2.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    --snip--

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };
}
```

Liste 5-6 : Création d'une nouvelle instance de `User` en utilisant l'une des valeurs de `user1`

En utilisant la syntaxe de mise à jour de struct, nous pouvons obtenir le même effet avec moins de code, comme indiqué dans la Liste 5-7. La syntaxe `..` spécifie que les autres champs non explicitement définis doivent avoir la même valeur que les champs de l'instance donnée.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    --snip--


    let user2 = User {
        email: String::from("another@example.com"),
      ..user1
    };
}
```

Liste 5-7 : Utilisation de la syntaxe de mise à jour de struct pour définir une nouvelle valeur pour `email` dans une instance de `User`, mais pour utiliser les autres valeurs de `user1`

Le code de la Liste 5-7 crée également une instance dans `user2` qui a une valeur différente pour `email`, mais qui a les mêmes valeurs pour les champs `username`, `active` et `sign_in_count` de `user1`. Le `..user1` doit être placé en dernier pour spécifier que tous les autres champs doivent prendre leurs valeurs à partir des champs correspondants de `user1`, mais nous pouvons choisir de spécifier des valeurs pour autant de champs que nous le souhaitons dans n'importe quel ordre, indépendamment de l'ordre des champs dans la définition du struct.

Notez que la syntaxe de mise à jour de struct utilise `=` comme une affectation ; c'est parce qu'elle déplace les données, tout comme nous l'avons vu dans "Variables et données interagissant avec Move". Dans cet exemple, nous ne pouvons plus utiliser `user1` après avoir créé `user2` car la `String` dans le champ `username` de `user1` a été déplacée dans `user2`. Si nous avions donné de nouvelles valeurs de `String` pour `email` et `username` dans `user2`, et donc seulement utilisé les valeurs `active` et `sign_in_count` de `user1`, alors `user1` serait toujours valide après la création de `user2`. Tant `active` que `sign_in_count` sont des types qui implémentent le trait `Copy`, donc le comportement que nous avons discuté dans "Données uniquement sur la pile : Copy" s'appliquerait.
