# Documentation testing

La principale manière de documenter un projet Rust est de commenter le code source. Les commentaires de documentation sont écrits selon la spécification CommonMark Markdown et prennent en charge les blocs de code à l'intérieur. Rust s'occupe de la correction, de sorte que ces blocs de code sont compilés et utilisés comme tests de documentation.

````rust
/// La première ligne est un résumé court décrivant la fonction.
///
/// Les lignes suivantes présentent la documentation détaillée. Les blocs de code commencent par
/// trois apostrophes inversées et ont une `fn main()` implicite à l'intérieur
/// et `extern crate <cratename>`. Supposons que nous testons la crate `doccomments` :
///
/// ```
/// let result = doccomments::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

/// En général, les commentaires de doc peuvent inclure les sections "Exemples", "Panics" et "Échecs".
///
/// La fonction suivante divise deux nombres.
///
/// # Exemples
///
/// ```
/// let result = doccomments::div(10, 2);
/// assert_eq!(result, 5);
/// ```
///
/// # Panics
///
/// La fonction génère une panique si le deuxième argument est égal à zéro.
///
/// ```rust
/// // génère une panique lors de la division par zéro
/// doccomments::div(10, 0);
/// ```
pub fn div(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    }

    a / b
}
````

Les blocs de code dans la documentation sont automatiquement testés lors de l'exécution de la commande `cargo test` normale :

```shell

```

## Motivation derrière les tests de documentation

Le principal but des tests de documentation est de servir d'exemples qui mettent en œuvre la fonctionnalité, ce qui est l'une des directives les plus importantes. Cela permet d'utiliser les exemples de la documentation comme extraits de code complets. Mais utiliser `?` fait échouer la compilation car `main` renvoie `unit`. La possibilité de cacher certaines lignes de code de la documentation vient en aide : on peut écrire `fn try_main() -> Result<(), ErrorType>`, la cacher et l'utiliser avec `unwrap` dans un `main` caché. Cela semble compliqué? Voici un exemple :

````rust
/// Utilisation d'un `try_main` caché dans les tests de doc.
///
/// ```
/// # // les lignes cachées commencent par le symbole `#`, mais elles sont toujours compilables!
/// # fn try_main() -> Result<(), String> { // ligne qui entoure le corps montré dans la doc
/// let res = doccomments::try_div(10, 2)?;
/// # Ok(()) // retour de try_main
/// # }
/// # fn main() { // début de main qui appellera unwrap()
/// #    try_main().unwrap(); // appel de try_main et utilisation de unwrap
/// #                         // de sorte que le test génère une panique en cas d'erreur
/// # }
/// ```
pub fn try_div(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Divide-by-zero"))
    } else {
        Ok(a / b)
    }
}
````
