# Inférence et annotation de type pour les closures

Il existe d'autres différences entre les fonctions et les closures. Les closures ne nécessitent généralement pas que vous annotiez les types des paramètres ou de la valeur de retour comme les fonctions `fn` le font. Les annotations de type sont requises pour les fonctions car les types font partie d'une interface explicite exposée à vos utilisateurs. Définir cette interface de manière rigide est important pour s'assurer que tout le monde est d'accord sur les types de valeurs qu'une fonction utilise et renvoie. Les closures, en revanche, ne sont pas utilisées dans une interface exposée de cette manière : elles sont stockées dans des variables et utilisées sans les nommer et sans les exposer aux utilisateurs de notre bibliothèque.

Les closures sont généralement courtes et ne sont pertinentes que dans un contexte restreint plutôt que dans n'importe quel scénario arbitraire. Dans ces contextes limités, le compilateur peut inférer les types des paramètres et le type de retour, de manière similaire à la façon dont il est capable d'inférer les types de la plupart des variables (il existe des cas rares où le compilateur a également besoin d'annotations de type pour les closures).

Comme pour les variables, nous pouvons ajouter des annotations de type si nous voulons augmenter l'explicitude et la clarté au détriment d'une plus grande verbeosité que nécessaire. Annoter les types pour une closure ressemblerait à la définition montrée dans la Liste 13-2. Dans cet exemple, nous définissons une closure et la stockons dans une variable plutôt que de la définir sur place où nous la passons en tant qu'argument, comme nous l'avons fait dans la Liste 13-1.

Nom du fichier : `src/main.rs`

```rust
let expensive_closure = |num: u32| -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

Liste 13-2 : Ajout d'annotations de type optionnelles des types de paramètre et de valeur de retour dans la closure

Avec les annotations de type ajoutées, la syntaxe des closures ressemble plus à la syntaxe des fonctions. Ici, nous définissons une fonction qui ajoute 1 à son paramètre et une closure qui a le même comportement, pour la comparaison. Nous avons ajouté quelques espaces pour aligner les parties pertinentes. Cela illustre comment la syntaxe des closures est similaire à la syntaxe des fonctions, sauf pour l'utilisation des tuyaux et la quantité de syntaxe optionnelle :

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

La première ligne montre une définition de fonction et la deuxième ligne montre une définition de closure entièrement annotée. Dans la troisième ligne, nous supprimons les annotations de type de la définition de closure. Dans la quatrième ligne, nous supprimons les accolades, qui sont optionnelles car le corps de la closure n'a qu'une seule expression. Toutes ces définitions sont valides et produiront le même comportement lorsqu'elles seront appelées. Les lignes `add_one_v3` et `add_one_v4` nécessitent que les closures soient évaluées pour être compilées car les types seront inférés à partir de leur utilisation. Cela est similaire à `let v = Vec::new();` qui nécessite soit des annotations de type soit des valeurs d'un certain type à être insérées dans le `Vec` pour que Rust soit capable d'inférer le type.

Pour les définitions de closures, le compilateur inferera un type concret pour chacun de leurs paramètres et pour leur valeur de retour. Par exemple, la Liste 13-3 montre la définition d'une closure courte qui ne renvoie que la valeur qu'elle reçoit en tant que paramètre. Cette closure n'est pas très utile, sauf dans le cadre de cet exemple. Notez que nous n'avons pas ajouté d'annotations de type à la définition. Du fait qu'il n'y a pas d'annotations de type, nous pouvons appeler la closure avec n'importe quel type, ce que nous avons fait ici avec `String` la première fois. Si nous essayons ensuite d'appeler `example_closure` avec un entier, nous obtiendrons une erreur.

Nom du fichier : `src/main.rs`

```rust
let example_closure = |x| x;

let s = example_closure(String::from("hello"));
let n = example_closure(5);
```

Liste 13-3 : Tentative d'appel d'une closure dont les types sont inférés avec deux types différents

Le compilateur nous donne cette erreur :

```bash
error[E0308]: mismatched types
 --> src/main.rs:5:29
  |
5 |     let n = example_closure(5);
  |                             ^- help: try using a conversion method:
`.to_string()`
  |                             |
  |                             expected struct `String`, found integer
```

La première fois que nous appelons `example_closure` avec la valeur `String`, le compilateur infère le type de `x` et le type de retour de la closure comme étant `String`. Ces types sont ensuite bloqués dans la closure dans `example_closure`, et nous obtenons une erreur de type lorsque nous essayons ensuite d'utiliser un type différent avec la même closure.
