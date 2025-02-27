# Starting Relative Paths with super

Nous pouvons construire des chemins relatifs qui commencent dans le module parent, plutôt que dans le module actuel ou la racine du crate, en utilisant `super` au début du chemin. C'est comme commencer un chemin de système de fichiers avec la syntaxe `..`. Utiliser `super` nous permet de faire référence à un élément que nous savons se trouver dans le module parent, ce qui peut faciliter le réarrangement de l'arborescence de modules lorsque le module est étroitement lié au parent, mais que le parent pourrait être déplacé ailleurs dans l'arborescence de modules un jour.

Considérez le code de la Liste 7-8 qui modélise la situation dans laquelle un chef corrige une commande incorrecte et l'apporte personnellement au client. La fonction `fix_incorrect_order` définie dans le module `back_of_house` appelle la fonction `deliver_order` définie dans le module parent en spécifiant le chemin vers `deliver_order`, en commençant par `super`.

Nom de fichier : `src/lib.rs`

```rust
fn deliver_order() {}

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        super::deliver_order();
    }

    fn cook_order() {}
}
```

Liste 7-8 : Appel d'une fonction en utilisant un chemin relatif commençant par `super`

La fonction `fix_incorrect_order` est dans le module `back_of_house`, donc nous pouvons utiliser `super` pour aller au module parent de `back_of_house`, qui dans ce cas est `crate`, la racine. À partir de là, nous cherchons `deliver_order` et nous le trouvons. Succès! Nous pensons que le module `back_of_house` et la fonction `deliver_order` sont susceptibles de rester dans la même relation l'une avec l'autre et d'être déplacés ensemble si nous décidons de reorganiser l'arborescence de modules du crate. Par conséquent, nous avons utilisé `super` pour avoir moins de places à mettre à jour le code à l'avenir si ce code est déplacé dans un autre module.
