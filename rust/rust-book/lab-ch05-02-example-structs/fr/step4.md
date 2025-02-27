# Ajout de fonctionnalités utiles avec des traits dérivés

Il serait utile de pouvoir afficher une instance de `Rectangle` pendant le débogage de notre programme et de voir les valeurs de tous ses champs. La liste 5-11 essaie d'utiliser la macro `println!` comme nous l'avons fait dans les chapitres précédents. Cela ne fonctionnera pas, cependant.

Nom de fichier : `src/main.rs`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {}", rect1);
}
```

Liste 5-11 : Tentative d'affichage d'une instance de `Rectangle`

Lorsque nous compilons ce code, nous obtenons une erreur avec ce message central :

```bash
error[E0277]: `Rectangle` n'implémente pas `std::fmt::Display`
```

La macro `println!` peut effectuer de nombreux types de formatage, et par défaut, les accolades indiquent à `println!` d'utiliser un formatage appelé `Display` : une sortie destinée à une consommation directe par l'utilisateur final. Les types primitifs que nous avons vus jusqu'à présent implémentent `Display` par défaut car il n'y a qu'un seul moyen de montrer un `1` ou tout autre type primitif à un utilisateur. Mais avec les structs, la manière dont `println!` devrait formater la sortie est moins claire car il y a plus de possibilités d'affichage : voulez-vous des virgules ou non? Voulez-vous afficher les accolades? Tous les champs devraient-ils être affichés? En raison de cette ambiguïté, Rust ne tente pas de deviner ce que nous voulons, et les structs n'ont pas de mise en œuvre fournie de `Display` à utiliser avec `println!` et le placeholder `{}`.

Si nous continuons à lire les erreurs, nous trouverons cette note utile :

    = help: le trait `std::fmt::Display` n'est pas implémenté pour `Rectangle`
    = note: dans les chaînes de formatage, vous pouvez peut-être utiliser `{:?}` (ou {:#?} pour
    l'affichage joli) à la place

Essayons-le! L'appel de macro `println!` ressemblera maintenant à `println!("rect1 is {:?}", rect1);`. En plaçant le spécificateur `:?` à l'intérieur des accolades, nous indiquons à `println!` que nous voulons utiliser un format de sortie appelé `Debug`. Le trait `Debug` nous permet d'afficher notre struct d'une manière utile pour les développeurs afin que nous puissions voir sa valeur pendant le débogage de notre code.

Compilez le code avec ce changement. Zut! Nous obtenons toujours une erreur :

```bash
error[E0277]: `Rectangle` n'implémente pas `Debug`
```

Mais encore une fois, le compilateur nous donne une note utile :

```rust
= help: le trait `Debug` n'est pas implémenté pour `Rectangle`
= note: ajoutez `#[derive(Debug)]` ou implémentez manuellement `Debug`
```

Rust _inclut_ effectivement une fonctionnalité pour afficher des informations de débogage, mais nous devons explicitement choisir de rendre cette fonctionnalité disponible pour notre struct. Pour ce faire, nous ajoutons l'attribut externe `#[derive(Debug)]` juste avant la définition du struct, comme montré dans la liste 5-12.

Nom de fichier : `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
}
```

Liste 5-12 : Ajout de l'attribut pour dériver le trait `Debug` et affichage de l'instance de `Rectangle` en utilisant le format de débogage

Maintenant, lorsque nous exécutons le programme, nous n'obtenons pas d'erreurs, et nous voyons la sortie suivante :

```rust
rect1 is Rectangle { width: 30, height: 50 }
```

Très bien! Ce n'est pas la sortie la plus jolie, mais elle montre les valeurs de tous les champs pour cette instance, ce qui serait certainement utile pendant le débogage. Lorsque nous avons des structs plus grands, il est utile d'avoir une sortie un peu plus facile à lire ; dans ces cas, nous pouvons utiliser `{:#?}` à la place de `{:?}` dans la chaîne `println!`. Dans cet exemple, en utilisant le style `{:#?}`, la sortie sera la suivante :

    rect1 is Rectangle {
        width: 30,
        height: 50,
    }

Une autre manière d'afficher une valeur au format `Debug` est d'utiliser la macro `dbg!`, qui prend la propriété d'une expression (contrairement à `println!`, qui prend une référence), affiche le nom du fichier et le numéro de ligne où cet appel de macro `dbg!` se produit dans votre code ainsi que la valeur résultante de cette expression, et renvoie la propriété de la valeur.

> Note : Appeler la macro `dbg!` imprime dans le flux de console d'erreur standard (`stderr`), contrairement à `println!`, qui imprime dans le flux de console de sortie standard (`stdout`). Nous en parlerons plus en détail dans "Écriture de messages d'erreur sur la sortie d'erreur standard au lieu de la sortie standard".

Voici un exemple où nous sommes intéressés par la valeur qui est assignée au champ `width`, ainsi que la valeur du struct entier dans `rect1` :

Nom de fichier : `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
      1 width: dbg!(30 * scale),
        height: 50,
    };

  2 dbg!(&rect1);
}
```

Nous pouvons placer `dbg!` autour de l'expression `30 * scale` \[1\] et, puisque `dbg!` renvoie la propriété de la valeur de l'expression, le champ `width` aura la même valeur que si nous n'avions pas le call `dbg!` là. Nous ne voulons pas que `dbg!` prenne la propriété de `rect1`, donc nous utilisons une référence à `rect1` dans l'appel suivant \[2\]. Voici à quoi ressemble la sortie de cet exemple :

    [src/main.rs:10] 30 * scale = 60
    [src/main.rs:14] &rect1 = Rectangle {
        width: 60,
        height: 50,
    }

Nous pouvons voir que le premier morceau de sortie provient de \[1\] où nous débuggeons l'expression `30 * scale`, et sa valeur résultante est `60` (le formatage `Debug` implémenté pour les entiers est de n'afficher que leur valeur). L'appel `dbg!` à \[2\] affiche la valeur de `&rect1`, qui est le struct `Rectangle`. Cette sortie utilise le formatage `Debug` joli du type `Rectangle`. La macro `dbg!` peut être vraiment utile lorsque vous essayez de comprendre ce que fait votre code!

En plus du trait `Debug`, Rust a fourni un certain nombre de traits pour que nous puissions les utiliser avec l'attribut `derive` qui peuvent ajouter un comportement utile à nos types personnalisés. Ces traits et leurs comportements sont listés dans l'annexe C. Nous aborderons la manière d'implémenter ces traits avec un comportement personnalisé ainsi que la manière de créer vos propres traits au chapitre 10. Il existe également de nombreux attributs autres que `derive` ; pour plus d'informations, consultez la section "Attributs" de la référence Rust à *https://doc.rust-lang.org/reference/attributes.html*.

Notre fonction `area` est très spécifique : elle ne calcule que l'aire de rectangles. Il serait utile de lier ce comportement plus étroitement à notre struct `Rectangle` car elle ne fonctionnera pas avec tout autre type. Voyons comment nous pouvons continuer à refactoriser ce code en transformant la fonction `area` en une _méthode_ `area` définie sur notre type `Rectangle`.
