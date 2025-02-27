# Alternatives to Using match with Result\<T, E\>

C'est beaucoup de `match`! L'expression `match` est très utile mais également très primitive. Au chapitre 13, vous apprendrez à propos des closures, qui sont utilisées avec de nombreuses des méthodes définies sur `Result<T, E>`. Ces méthodes peuvent être plus concises que l'utilisation de `match` lorsqu'il s'agit de gérer des valeurs `Result<T, E>` dans votre code.

Par exemple, voici une autre façon d'écrire la même logique que celle montrée dans la liste 9-5, cette fois en utilisant des closures et la méthode `unwrap_or_else` :

    // src/main.rs
    use std::fs::File;
    use std::io::ErrorKind;

    fn main() {
        let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
            if error.kind() == ErrorKind::NotFound {
                File::create("hello.txt").unwrap_or_else(|error| {
                    panic!("Problem creating the file: {:?}", error);
                })
            } else {
                panic!("Problem opening the file: {:?}", error);
            }
        });
    }

Bien que ce code ait le même comportement que la liste 9-5, il ne contient pas d'expressions `match` et est plus propre à lire. Revenez à cet exemple après avoir lu le chapitre 13 et consultez la documentation de la bibliothèque standard pour la méthode `unwrap_or_else`. De nombreuses autres de ces méthodes peuvent simplifier les expressions `match` imbriquées lorsqu'il s'agit de gérer les erreurs.
