# Preventing Dangling References with Lifetimes

Le principal objectif des durées de vie est de prévenir les _références faussaires_, qui entraînent qu'un programme référence des données autres que celles qu'il est censé référencer. Considérez le programme de la Liste 10-16, qui a une portée externe et une portée interne.

```rust
fn main() {
  1 let r;

    {
      2 let x = 5;
      3 r = &x;
  4 }

  5 println!("r: {r}");
}
```

Liste 10-16: Tentative d'utilisation d'une référence dont la valeur est sortie de portée

> Note: Les exemples des Listes 10-16, 10-17 et 10-23 déclarent des variables sans leur donner de valeur initiale, de sorte que le nom de variable existe dans la portée externe. Au premier abord, cela peut sembler être en conflit avec le fait que Rust n'a pas de valeurs nulles. Cependant, si nous essayons d'utiliser une variable avant de lui donner une valeur, nous obtiendrons une erreur de compilation, ce qui montre que Rust ne permet effectivement pas les valeurs nulles.

La portée externe déclare une variable nommée `r` sans valeur initiale \[1\], et la portée interne déclare une variable nommée `x` avec la valeur initiale de `5` \[2\]. À l'intérieur de la portée interne, nous tentons de définir la valeur de `r` comme une référence à `x` \[3\]. Ensuite, la portée interne se termine \[4\], et nous tentons d'afficher la valeur de `r` \[5\]. Ce code ne compilera pas car la valeur à laquelle `r` fait référence est sortie de portée avant que nous n'essayions de l'utiliser. Voici le message d'erreur :

```bash
error[E0597]: `x` does not live long enough
 --> src/main.rs:6:13
  |
6 |         r = &x;
  |             ^^ borrowed value does not live long enough
7 |     }
  |     - `x` dropped here while still borrowed
8 |
9 |     println!("r: {r}");
  |                   - borrow later used here
```

Le message d'erreur indique que la variable `x` "ne vit pas assez longtemps". La raison est que `x` sera hors de portée lorsque la portée interne se terminera à la ligne 7. Mais `r` est toujours valide pour la portée externe ; parce que sa portée est plus grande, nous disons qu'elle "vit plus longtemps". Si Rust autorisait ce code à fonctionner, `r` ferait référence à une mémoire qui aurait été désallouée lorsque `x` est sorti de portée, et tout ce que nous aurions essayé de faire avec `r` ne fonctionnerait pas correctement. Alors, comment Rust détermine-t-il que ce code est invalide? Il utilise un vérificateur d'emprunt.
