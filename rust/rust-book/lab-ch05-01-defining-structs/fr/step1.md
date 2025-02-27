# Définir et instancier des structs

Les structs sont similaires aux tuples, discutés dans "Le type tuple", en ce sens qu'ils contiennent tous deux plusieurs valeurs liées. Comme les tuples, les éléments d'un struct peuvent être de différents types. Contrairement aux tuples, dans un struct, vous allez nommer chaque élément de données pour qu'il soit clair ce que signifient les valeurs. Ajouter ces noms signifie que les structs sont plus flexibles que les tuples : vous n'avez pas à vous fier à l'ordre des données pour spécifier ou accéder aux valeurs d'une instance.

Pour définir un struct, nous entrons le mot clé `struct` et nommons l'ensemble du struct. Le nom d'un struct devrait décrire l'importance des éléments de données regroupés. Ensuite, à l'intérieur des accolades, nous définissons les noms et les types des éléments de données, que nous appelons _champs_. Par exemple, la Liste 5-1 montre un struct qui stocke des informations sur un compte utilisateur.

Nom de fichier : `src/main.rs`

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

Liste 5-1 : Définition d'un struct `User`

Pour utiliser un struct après l'avoir défini, nous créons une _instance_ de ce struct en spécifiant des valeurs concrètes pour chacun des champs. Nous créons une instance en indiquant le nom du struct et en ajoutant des accolades contenant des paires clé : valeur, où les clés sont les noms des champs et les valeurs sont les données que nous voulons stocker dans ces champs. Nous n'avons pas besoin de spécifier les champs dans le même ordre dans lequel nous les avons déclarés dans le struct. En d'autres termes, la définition du struct est comme un modèle général pour le type, et les instances remplissent ce modèle avec des données particulières pour créer des valeurs du type. Par exemple, nous pouvons déclarer un utilisateur particulier comme indiqué dans la Liste 5-2.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
}
```

Liste 5-2 : Création d'une instance du struct `User`

Pour obtenir une valeur spécifique d'un struct, nous utilisons la notation point. Par exemple, pour accéder à l'adresse e-mail de cet utilisateur, nous utilisons `user1.email`. Si l'instance est mutable, nous pouvons changer une valeur en utilisant la notation point et en assignant à un champ particulier. La Liste 5-3 montre comment changer la valeur dans le champ `email` d'une instance mutable de `User`.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    user1.email = String::from("anotheremail@example.com");
}
```

Liste 5-3 : Changement de la valeur dans le champ `email` d'une instance de `User`

Notez que l'ensemble de l'instance doit être mutable ; Rust ne nous permet pas de marquer seulement certains champs comme mutables. Comme avec toute expression, nous pouvons construire une nouvelle instance du struct comme dernière expression dans le corps de la fonction pour retourner implicitement cette nouvelle instance.

La Liste 5-4 montre une fonction `build_user` qui renvoie une instance de `User` avec l'e-mail et le nom d'utilisateur donnés. Le champ `active` obtient la valeur `true`, et le `sign_in_count` obtient une valeur de `1`.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}
```

Liste 5-4 : Une fonction `build_user` qui prend un e-mail et un nom d'utilisateur et renvoie une instance de `User`

Il est logique de nommer les paramètres de la fonction avec le même nom que les champs du struct, mais devoir répéter les noms de champs `email` et `username` et les variables est un peu fastidieux. Si le struct avait plus de champs, répéter chaque nom serait encore plus ennuyeux. Heureusement, il y a un raccourci pratique!
