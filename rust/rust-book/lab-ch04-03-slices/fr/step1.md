# Le type Slice

Les _tranches_ vous permettent de référencer une séquence contiguë d'éléments dans une collection plutôt que la collection entière. Une tranche est un type de référence, donc elle n'a pas de propriété.

Voici un petit problème de programmation : écrire une fonction qui prend une chaîne de mots séparés par des espaces et renvoie le premier mot qu'elle trouve dans cette chaîne. Si la fonction ne trouve pas d'espace dans la chaîne, toute la chaîne doit être un mot, donc la chaîne entière devrait être renvoyée.

Examillons comment écrire la signature de cette fonction sans utiliser de tranches, pour comprendre le problème que les tranches résoudront :

```rust
fn first_word(s: &String) ->?
```

La fonction `first_word` a un paramètre `&String`. Nous ne voulons pas la propriété, donc c'est correct. Mais que devrions-nous renvoyer? Nous n'avons pas vraiment de moyen de parler d'_une partie_ d'une chaîne. Cependant, nous pourrions renvoyer l'index de la fin du mot, indiqué par un espace. Essayons cela, comme montré dans la Liste 4-7.

Nom de fichier : `src/main.rs`

```rust
fn first_word(s: &String) -> usize {
  1 let bytes = s.as_bytes();

    for (2 i, &item) in 3 bytes.iter().enumerate() {
      4 if item == b' ' {
            return i;
        }
    }

  5 s.len()
}
```

Liste 4-7 : La fonction `first_word` qui renvoie une valeur d'index de byte dans le paramètre `String`

Comme nous devons parcourir l'élément `String` un par un et vérifier si une valeur est un espace, nous allons convertir notre `String` en un tableau d'octets en utilisant la méthode `as_bytes` \[1\].

Ensuite, nous créons un itérateur sur le tableau d'octets en utilisant la méthode `iter` \[3\]. Nous aborderons les itérateurs en détail au Chapitre 13. Pour l'instant, sachez que `iter` est une méthode qui renvoie chaque élément d'une collection et que `enumerate` enveloppe le résultat de `iter` et renvoie chaque élément sous forme d'un tuple au lieu de cela. Le premier élément du tuple renvoyé par `enumerate` est l'index, et le second élément est une référence à l'élément. Cela est un peu plus pratique que de calculer l'index nous-mêmes.

Comme la méthode `enumerate` renvoie un tuple, nous pouvons utiliser des motifs pour déstructurer ce tuple. Nous aborderons les motifs plus en détail au Chapitre 6. Dans la boucle `for`, nous spécifions un motif qui a `i` pour l'index dans le tuple et `&item` pour le seul octet dans le tuple \[2\]. Comme nous obtenons une référence à l'élément de `.iter().enumerate()`, nous utilisons `&` dans le motif.

À l'intérieur de la boucle `for`, nous cherchons l'octet qui représente l'espace en utilisant la syntaxe littérale d'octet \[4\]. Si nous trouvons un espace, nous renvoyons la position. Sinon, nous renvoyons la longueur de la chaîne en utilisant `s.len()` \[5\].

Nous avons maintenant un moyen de trouver l'index de la fin du premier mot dans la chaîne, mais il y a un problème. Nous renvoyons un `usize` tout seul, mais ce n'est qu'un nombre significatif dans le contexte du `&String`. En d'autres termes, parce que c'est une valeur séparée de la `String`, il n'est pas garanti qu'elle sera toujours valide à l'avenir. Considérez le programme dans la Liste 4-8 qui utilise la fonction `first_word` de la Liste 4-7.

    // src/main.rs
    fn main() {
        let mut s = String::from("hello world");

        let word = first_word(&s); // word aura la valeur 5

        s.clear(); // cela vide la String, la rendant égale à ""

        // word a toujours la valeur 5 ici, mais il n'y a plus de chaîne que
        // nous pourrions utiliser de manière significative avec la valeur 5. word est maintenant totalement invalide!
    }

Liste 4-8 : Stockage du résultat de l'appel de la fonction `first_word` puis modification du contenu de la `String`

Ce programme se compile sans erreur et le ferait également si nous utilisions `word` après avoir appelé `s.clear()`. Parce que `word` n'est pas du tout lié à l'état de `s`, `word` contient toujours la valeur `5`. Nous pourrions utiliser cette valeur `5` avec la variable `s` pour essayer d'extraire le premier mot, mais ce serait un bogue car le contenu de `s` a changé depuis que nous avons enregistré `5` dans `word`.

Devoir vous soucier de l'index dans `word` qui se met hors de synchronisation avec les données dans `s` est fastidieux et propice aux erreurs! Gérer ces indices est encore plus fragile si nous écrivons une fonction `second_word`. Sa signature devrait ressembler à cela :

```rust
fn second_word(s: &String) -> (usize, usize) {
```

Maintenant, nous suivons un index de départ _et_ un index de fin, et nous avons encore plus de valeurs qui ont été calculées à partir des données dans un état particulier mais qui ne sont pas liées à cet état du tout. Nous avons trois variables non liées qui circulent et qui doivent être maintenues en synchronisation.

Heureusement, Rust a une solution à ce problème : les tranches de chaîne.
