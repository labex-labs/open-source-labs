# Vérification que le contenu d'un brouillon de publication est vide

Même après avoir appelé `add_text` et ajouté du contenu à notre publication, nous voulons toujours que la méthode `content` renvoie une chaîne de caractères vide car la publication est toujours dans l'état brouillon, comme montré à \[3\] dans le Listing 17-11. Pour l'instant, implémentons la méthode `content` avec la chose la plus simple qui répondra à cette exigence : en renvoyant toujours une chaîne de caractères vide. Nous changerons cela plus tard une fois que nous aurons implémenté la capacité de changer l'état d'une publication pour qu'elle puisse être publiée. Jusqu'à présent, les publications ne peuvent être que dans l'état brouillon, donc le contenu de la publication devrait toujours être vide. Le Listing 17-14 montre cette implémentation provisoire.

Nom de fichier : `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        ""
    }
}
```

Listing 17-14 : Ajout d'une implémentation provisoire pour la méthode `content` sur `Post` qui renvoie toujours une chaîne de caractères vide

Avec cette méthode `content` ajoutée, tout dans le Listing 17-11 jusqu'à la ligne \[3\] fonctionne comme prévu.
