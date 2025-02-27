# Portée des variables

Maintenant que nous avons dépassé la syntaxe de base de Rust, nous n'inclurons pas tout le code `fn main() {` dans les exemples, donc si vous suivez, assurez-vous d'insérer manuellement les exemples suivants dans une fonction `main`. En conséquence, nos exemples seront un peu plus concis, nous permettant de nous concentrer sur les détails réels plutôt que sur le code boilerplate.

En tant que premier exemple de propriété, nous examinerons la _portée_ de certaines variables. Une portée est la plage dans un programme pour laquelle un élément est valide. Considérez la variable suivante :

```rust
let s = "hello";
```

La variable `s` fait référence à une chaîne littérale, où la valeur de la chaîne est codée en dur dans le texte de notre programme. La variable est valide à partir du point où elle est déclarée jusqu'à la fin de la _portée_ actuelle. La liste 4-1 montre un programme avec des commentaires annotant où la variable `s` serait valide.

    {                      // s n'est pas valide ici, car elle n'est pas encore déclarée
        let s = "hello";   // s est valide à partir de ce point
        // faire des choses avec s
    }                      // cette portée est maintenant terminée, et s n'est plus valide

Liste 4-1 : Une variable et la portée dans laquelle elle est valide

En d'autres termes, il y a deux points importants dans le temps ici :

- Lorsque `s` entre _dans_ la portée, elle est valide.
- Elle reste valide jusqu'à ce qu'elle sorte _de_ la portée.

À ce stade, la relation entre les portées et le moment où les variables sont valides est similaire à celle des autres langages de programmation. Maintenant, nous allons construire sur cette compréhension en introduisant le type `String`.
