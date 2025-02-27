# Utiliser la syntaxe raccourcie d'initialisation de champ

Dans la Liste 5-4, les noms des paramètres et des champs du struct étant exactement les mêmes, nous pouvons utiliser la syntaxe _raccourcie d'initialisation de champ_ pour réécrire `build_user` de manière à ce qu'elle se comporte exactement de la même manière mais sans répéter `username` et `email`, comme indiqué dans la Liste 5-5.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

Liste 5-5 : Une fonction `build_user` qui utilise la syntaxe raccourcie d'initialisation de champ car les paramètres `username` et `email` ont le même nom que les champs du struct

Ici, nous créons une nouvelle instance du struct `User`, qui a un champ nommé `email`. Nous voulons définir la valeur du champ `email` sur la valeur du paramètre `email` de la fonction `build_user`. Comme le champ `email` et le paramètre `email` ont le même nom, nous n'avons qu'à écrire `email` au lieu de `email: email`.
