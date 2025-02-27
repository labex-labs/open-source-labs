# Fonctions associées

Toutes les fonctions définies à l'intérieur d'un bloc `impl` sont appelées _fonctions associées_ car elles sont associées au type nommé après le `impl`. Nous pouvons définir des fonctions associées qui n'ont pas `self` comme premier paramètre (et donc ne sont pas des méthodes) car elles n'ont pas besoin d'une instance du type pour fonctionner. Nous avons déjà utilisé une fonction de ce type : la fonction `String::from` qui est définie sur le type `String`.

Les fonctions associées qui ne sont pas des méthodes sont souvent utilisées pour les constructeurs qui renvoient une nouvelle instance de la structure. Ces fonctions sont souvent appelées `new`, mais `new` n'est pas un nom spécial et n'est pas intégré à la langue. Par exemple, nous pourrions choisir de fournir une fonction associée nommée `square` qui aurait un paramètre de dimension et utiliserait cela comme largeur et hauteur, ce qui faciliterait la création d'un carré `Rectangle` plutôt que d'avoir à spécifier la même valeur deux fois :

Nom de fichier : `src/main.rs`

```rust
impl Rectangle {
    fn square(size: u32) -> 1 Self  {
      2 Self  {
            width: size,
            height: size,
        }
    }
}
```

Les mots clés `Self` dans le type de retour \[1\] et dans le corps de la fonction \[2\] sont des alias pour le type qui apparaît après le mot clé `impl`, qui dans ce cas est `Rectangle`.

Pour appeler cette fonction associée, nous utilisons la syntaxe `::` avec le nom de la structure ; `let sq = Rectangle::square(3);` est un exemple. Cette fonction est organisée dans l'espace de nom de la structure : la syntaxe `::` est utilisée pour les fonctions associées et les espaces de nom créés par les modules. Nous discuterons des modules au Chapitre 7.
