# Commentaires

Tout programme nécessite des commentaires, et Rust prend en charge plusieurs types différents :

- _Commentaires normaux_ qui sont ignorés par le compilateur :
  - `// Commentaires de ligne qui vont jusqu'à la fin de la ligne.`
  - `/* Commentaires de bloc qui vont jusqu'au délimiteur de fermeture. */`
- _Commentaires de documentation_ qui sont analysés pour générer la documentation de bibliothèque au format HTML :
  - `/// Génère la documentation de bibliothèque pour l'élément suivant.`
  - `//! Génère la documentation de bibliothèque pour l'élément entourant.`

```rust
fn main() {
    // Ceci est un exemple de commentaire de ligne.
    // Il y a deux barres obliques au début de la ligne.
    // Et rien écrit après cela ne sera lu par le compilateur.

    // println!("Bonjour, le monde!");

    // Exécutez-le. Voyez? Maintenant, essayez de supprimer les deux barres obliques, puis exécutez-le à nouveau.

    /*
     * Ceci est un autre type de commentaire, un commentaire de bloc. En général,
     * les commentaires de ligne sont le style de commentaire recommandé. Mais les commentaires de bloc
     * sont extrêmement utiles pour désactiver temporairement des morceaux de code.
     * /* Les commentaires de bloc peuvent être /* imbriqués, */ */ donc il suffit de quelques
     * frappes pour commenter tout le contenu de cette fonction main().
     * /*/*/* Essayez-le vous-même! */*/*/
     */

    /*
    Note : La colonne précédente de `*` était entièrement pour le style. Il n'y a
    pas vraiment besoin de cela.
    */

    // Vous pouvez manipuler les expressions plus facilement avec les commentaires de bloc
    // que avec les commentaires de ligne. Essayez de supprimer les délimiteurs de commentaire
    // pour changer le résultat :
    let x = 5 + /* 90 + */ 5;
    println!("`x` est-il 10 ou 100? x = {}", x);
}
```
