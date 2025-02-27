# Conditional if let Expressions

Au chapitre 6, nous avons discuté de la manière d'utiliser les expressions `if let` principalement comme un moyen plus court d'écrire l'équivalent d'un `match` qui ne correspond qu'à un seul cas. Facultativement, `if let` peut avoir un `else` correspondant contenant le code à exécuter si le motif dans `if let` ne correspond pas.

Le listing 18-1 montre qu'il est également possible de mélanger et d'associer des expressions `if let`, `else if` et `else if let`. Cela nous donne plus de flexibilité qu'une expression `match` dans laquelle nous ne pouvons exprimer qu'une seule valeur à comparer avec les motifs. De plus, Rust n'exige pas que les conditions dans une série de bras `if let`, `else if` et `else if let` soient liées les unes aux autres.

Le code du listing 18-1 détermine quelle couleur utiliser pour votre fond d'écran en fonction d'une série de vérifications pour plusieurs conditions. Pour cet exemple, nous avons créé des variables avec des valeurs codées en dur que pourrait recevoir un programme réel à partir d'une entrée utilisateur.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

  1 if let Some(color) = favorite_color {
      2 println!(
            "Using your favorite, {color}, as the background"
        );
  3 } else if is_tuesday {
      4 println!("Tuesday is green day!");
  5 } else if let Ok(age) = age {
      6 if age > 30 {
          7 println!("Using purple as the background color");
        } else {
          8 println!("Using orange as the background color");
        }
  9 } else {
     10 println!("Using blue as the background color");
    }
}
```

Listing 18-1: Mixing `if let`, `else if`, `else if let`, and `else`

Si l'utilisateur spécifie une couleur favorite \[1\], cette couleur est utilisée comme fond d'écran \[2\]. Si aucune couleur favorite n'est spécifiée et que aujourd'hui est mardi \[3\], la couleur de fond est verte \[4\]. Sinon, si l'utilisateur spécifie son âge sous forme de chaîne de caractères et que nous pouvons le parser en tant que nombre avec succès \[5\], la couleur est soit violette \[7\] soit orange \[8\] selon la valeur du nombre \[6\]. Si aucune de ces conditions n'est applicable \[9\], la couleur de fond est bleue \[10\].

Cette structure conditionnelle nous permet de prendre en charge des exigences complexes. Avec les valeurs codées en dur que nous avons ici, cet exemple affichera `Using purple as the background color`.

Vous pouvez voir que `if let` peut également introduire des variables masquées de la même manière que les bras de `match` le peuvent : la ligne `if let Ok(age) = age` \[5\] introduit une nouvelle variable `age` masquée qui contient la valeur à l'intérieur de la variante `Ok`. Cela signifie que nous devons placer la condition `if age > 30` \[6\] à l'intérieur de ce bloc : nous ne pouvons pas combiner ces deux conditions en `if let Ok(age) = age && age > 30`. L'`age` masqué que nous voulons comparer à 30 n'est pas valide jusqu'au début du nouveau scope avec les accolades.

Le inconvénient d'utiliser des expressions `if let` est que le compilateur ne vérifie pas l'exhaustivité, tandis qu'avec les expressions `match` il le fait. Si nous omettions le dernier bloc `else` \[9\] et donc manquions de traiter certains cas, le compilateur ne nous alerterait pas sur le possible bogue logique.
