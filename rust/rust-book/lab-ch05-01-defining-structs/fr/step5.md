# Structs sans champs, ressemblant à l'unité

Vous pouvez également définir des structs qui n'ont aucun champ! Ce sont appelés _structs ressemblant à l'unité_ car ils se comportent de manière similaire à `()`, le type unité que nous avons mentionné dans "Le type tuple". Les structs ressemblant à l'unité peuvent être utiles lorsque vous devez implémenter un trait sur un certain type mais n'avez pas de données que vous souhaitiez stocker dans le type lui-même. Nous aborderons les traits au Chapitre 10. Voici un exemple de déclaration et d'instanciation d'un struct unité nommé `AlwaysEqual` :

Nom de fichier : `src/main.rs`

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

Pour définir `AlwaysEqual`, nous utilisons le mot clé `struct`, le nom que nous souhaitons, puis un point-virgule. Pas besoin d'accolades ou de parenthèses! Ensuite, nous pouvons obtenir une instance de `AlwaysEqual` dans la variable `subject` de manière similaire : en utilisant le nom que nous avons défini, sans aucune accolade ou parenthèse. Imaginez que plus tard, nous implémentons un comportement pour ce type de sorte que chaque instance de `AlwaysEqual` soit toujours égale à chaque instance de n'importe quel autre type, peut-être pour avoir un résultat connu à des fins de test. Nous n'aurions pas besoin de données pour implémenter ce comportement! Vous verrez au Chapitre 10 comment définir des traits et les implémenter sur n'importe quel type, y compris les structs ressemblant à l'unité.

> **Propriété des données des structs**
>
> Dans la définition du struct `User` dans la Liste 5-1, nous avons utilisé le type `String` propriétaire plutôt que le type de tranche de chaîne `&str`. C'est un choix délibéré car nous voulons que chaque instance de ce struct ait la propriété de toutes ses données et que ces données soient valides aussi longtemps que l'ensemble du struct est valide.
>
> Il est également possible pour les structs de stocker des références à des données appartenant à autre chose, mais pour ce faire, il est nécessaire d'utiliser des _durées de vie_, une fonctionnalité de Rust que nous aborderons au Chapitre 10. Les durées de vie garantissent que les données référencées par un struct sont valides aussi longtemps que le struct est valide. Disons que vous essayez de stocker une référence dans un struct sans spécifier de durées de vie, comme suit dans `src/main.rs` ; cela ne fonctionnera pas :
>
>     struct User {
>         active: bool,
>         username: &str,
>         email: &str,
>         sign_in_count: u64,
>     }
>
>     fn main() {
>         let user1 = User {
>             active: true,
>             username: "someusername123",
>             email: "someone@example.com",
>             sign_in_count: 1,
>         };
>     }
>
> Le compilateur signalera qu'il a besoin de spécificateurs de durée de vie :
>
>     $ `cargo run`
>        Compiling structs v0.1.0 (file:///projects/structs)
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:3:15
>       |
>     3 |     username: &str,
>       |               ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 ~     username: &'a str,
>       |
>
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:4:12
>       |
>     4 |     email: &str,
>       |            ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 |     username: &str,
>     4 ~     email: &'a str,
>       |
>
> Au Chapitre 10, nous aborderons comment corriger ces erreurs pour que vous puissiez stocker des références dans des structs, mais pour l'instant, nous corrigerons des erreurs comme celles-ci en utilisant des types propriétaires comme `String` au lieu de références comme `&str`.
