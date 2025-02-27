# Valeurs de retour et portée

Le retour de valeurs peut également transférer la propriété. La liste 4-4 montre un exemple d'une fonction qui retourne une certaine valeur, avec des annotations similaires à celles de la liste 4-3.

    // src/main.rs
    fn main() {
        let s1 = gives_ownership();         // gives_ownership déplace sa valeur de retour
                                            // dans s1

        let s2 = String::from("hello");     // s2 entre dans la portée

        let s3 = takes_and_gives_back(s2);  // s2 est déplacé dans
                                            // takes_and_gives_back, qui déplace également
                                            // sa valeur de retour dans s3
    } // Ici, s3 sort de portée et est supprimé. s2 a été déplacé, donc rien
      // ne se passe. s1 sort de portée et est supprimé

    fn gives_ownership() -> String {             // gives_ownership déplacera sa
                                                 // valeur de retour dans la fonction
                                                 // qui l'appelle

        let some_string = String::from("yours"); // some_string entre dans la portée

        some_string                              // some_string est retournée et
                                                 // déplacée vers la fonction appelante
    }

    // Cette fonction prend une String et retourne une String
    fn takes_and_gives_back(a_string: String) -> String { // a_string entre dans
                                                          // la portée

        a_string  // a_string est retournée et déplacée vers la fonction appelante
    }

Liste 4-4 : Transfert de propriété des valeurs de retour

La propriété d'une variable suit le même modèle chaque fois : attribuer une valeur à une autre variable la déplace. Lorsqu'une variable qui inclut des données sur le tas sort de portée, la valeur sera nettoyée par `drop` à moins que la propriété des données ait été transférée à une autre variable.

Alors que cela fonctionne, prendre la propriété puis retourner la propriété avec chaque fonction est un peu fastidieux. Et si nous voulons laisser une fonction utiliser une valeur mais ne pas prendre la propriété? Il est assez gênant que tout ce que nous passons également doive être passé en retour si nous voulons l'utiliser à nouveau, en plus de tout les données issues du corps de la fonction que nous voudrions peut-être également retourner.

Rust nous permet effectivement de retourner plusieurs valeurs en utilisant un tuple, comme montré dans la liste 4-5.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{s2}' is {len}.");
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() renvoie la longueur d'une String

    (s, length)
}
```

Liste 4-5 : Retour de la propriété des paramètres

Mais c'est trop de formalités et beaucoup de travail pour un concept qui devrait être courant. Heureusement pour nous, Rust a une fonctionnalité pour utiliser une valeur sans transférer la propriété, appelée _références_.
