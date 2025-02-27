# Écrire des commentaires de documentation utiles

Documenter précisément vos packages aidera les autres utilisateurs à savoir comment et quand les utiliser, il est donc worthwhile de prendre le temps d'écrire de la documentation. Au chapitre 3, nous avons discuté de la manière de commenter le code Rust en utilisant deux barres obliques, `//`. Rust dispose également d'un type particulier de commentaire pour la documentation, connu commode ment sous le nom de _commentaire de documentation_, qui générera une documentation HTML. Le HTML affiche le contenu des commentaires de documentation pour les éléments de l'API publique destinés aux programmeurs intéressés par la manière d'_utiliser_ votre boîte à outils (crate) plutôt que par la manière dont votre boîte à outils est _implémentée_.

Les commentaires de documentation utilisent trois barres obliques, `///`, au lieu de deux et prennent en charge la notation Markdown pour formater le texte. Placez les commentaires de documentation juste avant l'élément qu'ils documentent. La liste 14-1 montre des commentaires de documentation pour une fonction `add_one` dans une boîte à outils (crate) nommée `my_crate`.

Nom du fichier : `src/lib.rs`

````rust
/// Ajoute un à un nombre donné.
///
/// # Exemples
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
````

Liste 14-1 : Un commentaire de documentation pour une fonction

Ici, nous donnons une description de ce que fait la fonction `add_one`, commençons une section avec le titre `Exemples`, puis fournissons du code qui démontre comment utiliser la fonction `add_one`. Nous pouvons générer la documentation HTML à partir de ce commentaire de documentation en exécutant `cargo doc`. Cette commande exécute l'outil `rustdoc` distribué avec Rust et place la documentation HTML générée dans le répertoire `target/doc`.

Pour plus de commodité, exécuter `cargo doc --open` construira le HTML pour la documentation de votre boîte à outils (crate) actuelle (ainsi que la documentation pour toutes les dépendances de votre boîte à outils) et ouvrira le résultat dans un navigateur web. Accédez à la fonction `add_one` et vous verrez comment le texte dans les commentaires de documentation est affiché, comme montré dans la figure 14-1.

Figure 14-1 : Documentation HTML pour la fonction `add_one`
