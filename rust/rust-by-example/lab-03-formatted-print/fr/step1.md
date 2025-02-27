# Impression formatée

L'impression est gérée par une série de `macros` définies dans `std::fmt` dont certaines sont les suivantes :

- `format!` : écrit du texte formaté dans une `String`.
- `print!` : identique à `format!` mais le texte est imprimé sur la console (`io::stdout`).
- `println!` : identique à `print!` mais un retour à la ligne est ajouté.
- `eprint!` : identique à `print!` mais le texte est imprimé sur la sortie d'erreur standard (`io::stderr`).
- `eprintln!` : identique à `eprint!` mais un retour à la ligne est ajouté.

Toutes analysent le texte de la même manière. De plus, Rust vérifie la correction du formatage à la compilation.

```rust
fn main() {
    // En général, `{}` sera automatiquement remplacé par n'importe quel
    // argument. Ces arguments seront convertis en chaîne de caractères.
    println!("{} jours", 31);

    // On peut utiliser des arguments positionnels. Spécifier un entier à
    // l'intérieur de `{}` détermine quel argument supplémentaire sera remplacé.
    // Les arguments commencent à 0 immédiatement après la chaîne de formatage.
    println!("{0}, c'est {1}. {1}, c'est {0}", "Alice", "Bob");

    // On peut également utiliser des arguments nommés.
    println!("{sujet} {verbe} {objet}",
             objet="le chien paresseux",
             sujet="le renard brun rapide",
             verbe="saute par-dessus");

    // On peut invoquer différents formats en spécifiant le caractère de format
    // après un `:`.
    println!("Base 10 :               {}",   69420); // 69420
    println!("Base 2 (binaire) :       {:b}", 69420); // 10000111100101100
    println!("Base 8 (octale) :        {:o}", 69420); // 207454
    println!("Base 16 (hexadécimale) : {:x}", 69420); // 10f2c
    println!("Base 16 (hexadécimale) : {:X}", 69420); // 10F2C

    // On peut justifier le texte à droite avec une largeur spécifiée. Cela
    // produira "    1". (Quatre espaces blancs et un "1", pour une largeur totale de 5.)
    println!("{nombre:>5}", nombre=1);

    // On peut remplir les nombres avec des zéros supplémentaires,
    println!("{nombre:0>5}", nombre=1); // 00001
    // et ajuster à gauche en inversant le signe. Cela produira "10000".
    println!("{nombre:0<5}", nombre=1); // 10000

    // On peut utiliser des arguments nommés dans le spécificateur de format en
    // ajoutant un `$`.
    println!("{nombre:0>largeur$}", nombre=1, largeur=5);

    // Rust vérifie même pour s'assurer qu'on utilise le bon nombre d'arguments.
    println!("Mon nom est {0}, {1} {0}", "Bond");
    // FIXME ^ Ajoutez l'argument manquant : "James"

    // Seuls les types qui implémentent fmt::Display peuvent être formatés avec `{}`.
    // Les types définis par l'utilisateur n'implémentent pas fmt::Display par défaut.

    #[allow(dead_code)] // désactive `dead_code` qui avertit contre les modules inutilisés
    struct Structure(i32);

    // Cela ne compilera pas car `Structure` n'implémente pas
    // fmt::Display.
    // println!("Cette structure `{}` ne s'imprimera pas...", Structure(3));
    // TODO ^ Essayez de décommenter cette ligne

    // Pour Rust 1.58 et supérieur, vous pouvez directement capturer l'argument
    // à partir d'une variable environnante. Comme ci-dessus, cela produira
    // "    1", 4 espaces blancs et un "1".
    let nombre: f64 = 1.0;
    let largeur: usize = 5;
    println!("{nombre:>largeur$}");
}
```

`std::fmt` contient de nombreux `traits` qui gèrent l'affichage du texte. Les formes de base de deux d'entre eux importants sont listées ci-dessous :

- `fmt::Debug` : utilise le marqueur `{:?}`. Formate le texte à des fins de débogage.
- `fmt::Display` : utilise le marqueur `{}`. Formate le texte d'une manière plus élégante et conviviale pour l'utilisateur.

Ici, nous avons utilisé `fmt::Display` car la bibliothèque standard fournit des implémentations pour ces types. Pour imprimer du texte pour des types personnalisés, des étapes supplémentaires sont nécessaires.

L'implémentation du trait `fmt::Display` implémente automatiquement le trait `ToString` qui nous permet de convertir le type en `String`.

À la _ligne 43_, `#[allow(dead_code)]` est un \[attribut\] qui ne s'applique qu'au module qui le suit.

## Activités

- Corrigez le problème dans le code ci-dessus (voir FIXME) pour qu'il s'exécute sans erreur.
- Essayez de décommenter la ligne qui tente de formater la structure `Structure` (voir TODO)
- Ajoutez un appel à la macro `println!` qui imprime : `Pi est environ 3,142` en contrôlant le nombre de décimales affichées. Pour cet exercice, utilisez `let pi = 3,141592` comme estimation de pi. (Indice : vous devrez peut-être consulter la documentation de `std::fmt` pour définir le nombre de décimales à afficher)
