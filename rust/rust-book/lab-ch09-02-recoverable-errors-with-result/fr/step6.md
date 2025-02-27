# A Shortcut for Propagating Errors: The? Operator

La liste 9-7 montre une implémentation de `read_username_from_file` qui a la même fonctionnalité que celle de la liste 9-6, mais cette implémentation utilise l'opérateur `?`.

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

Liste 9-7 : Une fonction qui renvoie des erreurs au code appelant en utilisant l'opérateur `?`

Le `?` placé après une valeur `Result` est défini pour fonctionner de manière presque identique aux expressions `match` que nous avons définies pour gérer les valeurs `Result` dans la liste 9-6. Si la valeur de la `Result` est un `Ok`, la valeur à l'intérieur de l'`Ok` sera renvoyée à partir de cette expression et le programme continuera. Si la valeur est un `Err`, l'`Err` sera renvoyé depuis la fonction entière comme si nous avions utilisé le mot clé `return`, de sorte que la valeur d'erreur soit propagée au code appelant.

Il y a une différence entre ce que fait l'expression `match` de la liste 9-6 et ce que fait l'opérateur `?` : les valeurs d'erreur sur lesquelles l'opérateur `?` est appelé passent par la fonction `from`, définie dans le trait `From` de la bibliothèque standard, qui est utilisée pour convertir des valeurs d'un type en un autre. Lorsque l'opérateur `?` appelle la fonction `from`, le type d'erreur reçu est converti en le type d'erreur défini dans le type de retour de la fonction actuelle. Cela est utile lorsqu'une fonction renvoie un type d'erreur pour représenter toutes les manières dont une fonction peut échouer, même si certaines parties peuvent échouer pour de nombreuses raisons différentes.

Par exemple, nous pourrions modifier la fonction `read_username_from_file` de la liste 9-7 pour renvoyer un type d'erreur personnalisé nommé `OurError` que nous définissons. Si nous définissons également `impl From<io::Error> for OurError` pour construire une instance de `OurError` à partir d'un `io::Error`, alors les appels à l'opérateur `?` dans le corps de `read_username_from_file` appelleront `from` et convertiront les types d'erreur sans avoir besoin d'ajouter plus de code à la fonction.

Dans le contexte de la liste 9-7, le `?` à la fin de l'appel à `File::open` renverra la valeur à l'intérieur d'un `Ok` à la variable `username_file`. Si une erreur se produit, l'opérateur `?` renverra immédiatement la fonction entière et donnera toute valeur `Err` au code appelant. La même chose s'applique au `?` à la fin de l'appel à `read_to_string`.

L'opérateur `?` élimine beaucoup de code répétitif et simplifie l'implémentation de cette fonction. Nous pourrions même raccourcir ce code encore plus en chaînant les appels de méthodes immédiatement après le `?`, comme montré dans la liste 9-8.

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

Liste 9-8 : Chaînement d'appels de méthodes après l'opérateur `?`

Nous avons déplacé la création de la nouvelle `String` dans `username` au début de la fonction ; cette partie n'a pas changé. Au lieu de créer une variable `username_file`, nous avons chaîné l'appel à `read_to_string` directement sur le résultat de `File::open("hello.txt")?`. Nous avons toujours un `?` à la fin de l'appel à `read_to_string`, et nous renvoyons toujours une valeur `Ok` contenant `username` lorsque `File::open` et `read_to_string` réussissent plutôt que renvoyer des erreurs. La fonctionnalité est à nouveau la même que dans les listes 9-6 et 9-7 ; il s'agit juste d'une manière différente et plus ergonomique d'écrire le code.

La liste 9-9 montre une manière de le rendre encore plus court en utilisant `fs::read_to_string`.

Nom du fichier : `src/main.rs`

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

Liste 9-9 : Utilisation de `fs::read_to_string` au lieu d'ouvrir puis lire le fichier

La lecture d'un fichier dans une chaîne est une opération assez courante, donc la bibliothèque standard fournit la fonction pratique `fs::read_to_string` qui ouvre le fichier, crée une nouvelle `String`, lit le contenu du fichier, met le contenu dans cette `String` et la renvoie. Bien sûr, l'utilisation de `fs::read_to_string` ne nous donne pas l'occasion d'expliquer toute la gestion des erreurs, donc nous l'avons fait de la manière plus longue d'abord.
