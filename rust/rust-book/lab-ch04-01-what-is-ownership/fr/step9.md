# Propriété et fonctions

Les mécanismes de passage d'une valeur à une fonction sont similaires à ceux de l'attribution d'une valeur à une variable. Passer une variable à une fonction entraînera un déplacement ou une copie, tout comme l'affectation. La liste 4-3 a un exemple avec quelques annotations montrant où les variables entrent et sortent de portée.

    // src/main.rs
    fn main() {
        let s = String::from("hello");  // s entre dans la portée

        takes_ownership(s);             // La valeur de s est déplacée dans la fonction...
                                        //... et n'est donc plus valide ici

        let x = 5;                      // x entre dans la portée

        makes_copy(x);                  // x serait déplacé dans la fonction,
                                        // mais i32 est Copy, donc il est possible
                                        // d'utiliser x après

    } // Ici, x sort de portée, puis s. Cependant, puisque la valeur de s a été déplacée,
      // rien de spécial ne se passe

    fn takes_ownership(some_string: String) { // some_string entre dans la portée
        println!("{some_string}");
    } // Ici, some_string sort de portée et `drop` est appelé. La mémoire sous-jacente
      // est libérée

    fn makes_copy(some_integer: i32) { // some_integer entre dans la portée
        println!("{some_integer}");
    } // Ici, some_integer sort de portée. Rien de spécial ne se passe

Liste 4-3 : Fonctions avec propriété et portée annotées

Si nous essayions d'utiliser `s` après l'appel à `takes_ownership`, Rust générerait une erreur de compilation. Ces vérifications statiques nous protègent contre les erreurs. Essayez d'ajouter du code à `main` qui utilise `s` et `x` pour voir où vous pouvez les utiliser et où les règles de propriété vous empêchent de le faire.
