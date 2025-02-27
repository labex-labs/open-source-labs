# Utiliser des fonctions `extern` pour appeler du code externe

Parfois, votre code Rust peut avoir besoin d'interagir avec du code écrit dans un autre langage. Pour cela, Rust dispose du mot clé `extern` qui facilite la création et l'utilisation d'une _Foreign Function Interface_ _(FFI)_, qui est un moyen pour un langage de programmation de définir des fonctions et permettre à un autre (étranger) langage de programmation d'appeler ces fonctions.

Le Listing 19-8 montre comment configurer une intégration avec la fonction `abs` de la bibliothèque standard C. Les fonctions déclarées à l'intérieur de blocs `extern` sont toujours non sécurisées à appeler à partir du code Rust. La raison en est que les autres langages ne respectent pas les règles et les garanties de Rust, et Rust ne peut pas les vérifier, donc la responsabilité incombe au programmeur pour assurer la sécurité.

Nom du fichier : `src/main.rs`

```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!(
            "Absolute value of -3 according to C: {}",
            abs(-3)
        );
    }
}
```

Listing 19-8 : Déclaration et appel d'une fonction `extern` définie dans un autre langage

Dans le bloc `extern "C"`, nous listons les noms et les signatures des fonctions externes d'un autre langage que nous souhaitons appeler. La partie `"C"` définit quelle _application binary interface_ _(ABI)_ utilise la fonction externe : l'ABI définit comment appeler la fonction au niveau de l'assemblage. L'ABI `"C"` est la plus commune et suit l'ABI du langage de programmation C.

> **Appeler des fonctions Rust à partir d'autres langages**
>
> Nous pouvons également utiliser `extern` pour créer une interface qui permet à d'autres langages d'appeler des fonctions Rust. Au lieu de créer un bloc `extern` complet, nous ajoutons le mot clé `extern` et spécifions l'ABI à utiliser juste avant le mot clé `fn` pour la fonction concernée. Nous devons également ajouter une annotation `#[no_mangle]` pour dire au compilateur Rust de ne pas modifier le nom de cette fonction. _Mangling_ est le fait qu'un compilateur change le nom que nous avons donné à une fonction en un nom différent qui contient plus d'informations pour d'autres parties du processus de compilation à consommer, mais est moins lisible pour l'homme. Chaque compilateur de langage de programmation modifie les noms légèrement différemment, donc pour qu'une fonction Rust soit nommable par d'autres langages, nous devons désactiver le mangling de noms du compilateur Rust.
>
> Dans l'exemple suivant, nous rendons la fonction `call_from_c` accessible à partir du code C, après qu'elle ait été compilée en une bibliothèque partagée et liée à partir de C :
>
>     #[no_mangle]
>     pub extern "C" fn call_from_c() {
>         println!("Just called a Rust function from C!");
>     }
>
> Cette utilisation de `extern` ne nécessite pas `unsafe`.
