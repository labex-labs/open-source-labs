# Tranches de chaîne

Une _tranche de chaîne_ est une référence à une partie d'une `String`, et elle ressemble à ceci :

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

Plutôt qu'une référence à l'ensemble de la `String`, `hello` est une référence à une partie de la `String`, spécifiée dans le morceau supplémentaire `[0..5]`. Nous créons des tranches en utilisant une plage entre crochets en spécifiant `[index_de_début..index_de_fin]`, où `index_de_début` est la première position dans la tranche et `index_de_fin` est une unité plus grande que la dernière position dans la tranche. Internement, la structure de données de la tranche stocke la position de départ et la longueur de la tranche, qui correspond à `index_de_fin` moins `index_de_début`. Ainsi, dans le cas de `let world = &s[6..11];`, `world` serait une tranche qui contient un pointeur vers le byte à l'index 6 de `s` avec une valeur de longueur de `5`.

La Figure 4-6 montre cela dans un diagramme.

Figure 4-6 : Tranche de chaîne faisant référence à une partie d'une `String`

Avec la syntaxe de plage `..` de Rust, si vous voulez commencer à l'index 0, vous pouvez omettre la valeur avant les deux points. En d'autres termes, ces deux expressions sont équivalentes :

```rust
let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];
```

De même, si votre tranche inclut le dernier byte de la `String`, vous pouvez omettre le nombre final. Cela signifie que ces deux expressions sont équivalentes :

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[3..len];
let slice = &s[3..];
```

Vous pouvez également omettre les deux valeurs pour prendre une tranche de toute la chaîne. Donc, ces deux expressions sont équivalentes :

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[0..len];
let slice = &s[..];
```

> Note : Les indices de plage de tranches de chaîne doivent se trouver aux limites valides des caractères UTF-8. Si vous essayez de créer une tranche de chaîne au milieu d'un caractère multioctet, votre programme se terminera avec une erreur. Dans le but d'introduire les tranches de chaîne, nous supposons ici uniquement des caractères ASCII ; une discussion plus approfondie du traitement UTF-8 se trouve dans "Stockage de texte encodé en UTF-8 avec des chaînes".

Ayant toutes ces informations à l'esprit, réécrivons `first_word` pour renvoyer une tranche. Le type qui signifie "tranche de chaîne" est écrit `&str` :

Nom de fichier : `src/main.rs`

```rust
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Nous obtenons l'index de la fin du mot de la même manière que dans la Liste 4-7, en cherchant la première occurrence d'un espace. Lorsque nous trouvons un espace, nous renvoyons une tranche de chaîne en utilisant le début de la chaîne et l'index de l'espace comme indices de début et de fin.

Maintenant, lorsque nous appelons `first_word`, nous obtenons une seule valeur qui est liée aux données sous-jacentes. La valeur est composée d'une référence au point de départ de la tranche et du nombre d'éléments dans la tranche.

Renvoyer une tranche fonctionnerait également pour une fonction `second_word` :

```rust
fn second_word(s: &String) -> &str {
```

Nous avons maintenant une API simple qui est beaucoup plus difficile à foirer car le compilateur assurera que les références dans la `String` restent valides. Rappelez-vous le bogue dans le programme de la Liste 4-8, lorsque nous avons obtenu l'index de la fin du premier mot mais avons ensuite vidé la chaîne, rendant ainsi notre index invalide? Ce code était logiquement incorrect mais n'a pas montré d'erreurs immédiates. Les problèmes se seraient manifestés plus tard si nous avions continué à utiliser l'index du premier mot avec une chaîne vidée. Les tranches rendent ce bogue impossible et nous permettent de détecter un problème dans notre code bien plus tôt. Utiliser la version avec tranche de `first_word` entraînera une erreur de compilation :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear(); // erreur!

    println!("le premier mot est : {word}");
}
```

Voici l'erreur du compilateur :

```bash
error[E0502]: impossible de prêter mutuellement `s` car il est déjà prêté en lecture seule
  --> src/main.rs:18:5
   |
16 |     let word = first_word(&s);
   |                           -- prêt en lecture seule ici
17 |
18 |     s.clear(); // erreur!
   |     ^^^^^^^^^ prêt mutuel ici
19 |
20 |     println!("le premier mot est : {word}");
   |                                   ---- prêt en lecture seule utilisé plus tard ici
```

Rappelez-vous les règles d'emprunt : si nous avons une référence immuable à quelque chose, nous ne pouvons pas également prendre une référence mutable. Parce que `clear` doit tronquer la `String`, il a besoin d'obtenir une référence mutable. L'instruction `println!` après l'appel à `clear` utilise la référence dans `word`, donc la référence immuable doit encore être active à ce moment-là. Rust interdit la référence mutable dans `clear` et la référence immuable dans `word` d'exister en même temps, et la compilation échoue. Non seulement Rust a rendu notre API plus facile à utiliser, mais il a également éliminé une classe entière d'erreurs au moment de la compilation!
