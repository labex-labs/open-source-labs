# Macros déclaratives avec macro_rules! pour la métaprogrammation générale

La forme la plus largement utilisée de macros en Rust est la macro _déclarative_. On les appelle parfois également "macros par exemple", "macros `macro_rules!`", ou simplement "macros". Au cœur, les macros déclaratives vous permettent d'écrire quelque chose de similaire à une expression `match` en Rust. Comme discuté au chapitre 6, les expressions `match` sont des structures de contrôle qui prennent une expression, comparent la valeur résultante de l'expression à des motifs, puis exécutent le code associé au motif correspondant. Les macros comparent également une valeur à des motifs associés à du code particulier : dans cette situation, la valeur est le code source littéral Rust passé à la macro ; les motifs sont comparés avec la structure de ce code source ; et le code associé à chaque motif, lorsqu'il correspond, remplace le code passé à la macro. Tout cela se produit pendant la compilation.

Pour définir une macro, vous utilisez la construction `macro_rules!`. Explorerons comment utiliser `macro_rules!` en examinant la définition de la macro `vec!`. Le chapitre 8 a traité de la manière dont nous pouvons utiliser la macro `vec!` pour créer un nouveau vecteur avec des valeurs particulières. Par exemple, la macro suivante crée un nouveau vecteur contenant trois entiers :

```rust
let v: Vec<u32> = vec![1, 2, 3];
```

Nous pourrions également utiliser la macro `vec!` pour créer un vecteur de deux entiers ou un vecteur de cinq fragments de chaîne de caractères. Nous ne pourrions pas utiliser une fonction pour faire la même chose car nous ne saurions pas à l'avance le nombre ou le type de valeurs.

L'annexe 19-28 montre une définition légèrement simplifiée de la macro `vec!`.

Nom de fichier : `src/lib.rs`

```rust
1 #[macro_export]
2 macro_rules! vec {
  3 ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
          4 $(
              5 temp_vec.push(6 $x);
            )*
          7 temp_vec
        }
    };
}
```

Annexe 19-28 : Version simplifiée de la définition de la macro `vec!`

> Note : La définition réelle de la macro `vec!` dans la bibliothèque standard inclut du code pour allouer à l'avance la quantité correcte de mémoire. Ce code est une optimisation que nous n'incluons pas ici pour simplifier l'exemple.

L'annotation `#[macro_export]` \[1\] indique que cette macro devrait être disponible chaque fois que le crate dans lequel la macro est définie est mis en contexte. Sans cette annotation, la macro ne peut pas être mise en contexte.

Nous commençons ensuite la définition de la macro avec `macro_rules!` et le nom de la macro que nous définissons _sans_ le point d'exclamation \[2\]. Le nom, dans ce cas `vec`, est suivi de parenthèses accolades dénotant le corps de la définition de la macro.

La structure dans le corps de `vec!` est similaire à la structure d'une expression `match`. Ici, nous avons un bras avec le motif `( $( $x:expr ),* )`, suivi de `=>` et du bloc de code associé à ce motif \[3\]. Si le motif correspond, le bloc de code associé sera émis. Étant donné que c'est le seul motif dans cette macro, il n'y a qu'un seul moyen valide de correspondre ; tout autre motif entraînera une erreur. Les macros plus complexes auront plus d'un bras.

La syntaxe de motif valide dans les définitions de macros est différente de la syntaxe de motif présentée au chapitre 18 car les motifs de macros sont comparés avec la structure du code Rust plutôt que avec des valeurs. Examillons ce que signifient les parties de motif dans l'annexe 19-28 ; pour la syntaxe complète des motifs de macros, consultez la Rust Reference à *https://doc.rust-lang.org/reference/macros-by-example.html*.

Tout d'abord, nous utilisons une paire de parenthèses pour envelopper le motif complet. Nous utilisons un signe dollar (`$`) pour déclarer une variable dans le système de macros qui contiendra le code Rust correspondant au motif. Le signe dollar indique clairement qu'il s'agit d'une variable de macro contrairement à une variable normale en Rust. Ensuite vient une paire de parenthèses qui capture les valeurs qui correspondent au motif à l'intérieur des parenthèses pour être utilisées dans le code de remplacement. Dans `$()`, il y a `$x:expr`, qui correspond à n'importe quelle expression Rust et donne à l'expression le nom `$x`.

La virgule qui suit `$()` indique qu'un caractère séparateur de virgule littéral pourrait éventuellement apparaître après le code qui correspond au code dans `$()`. Le `*` spécifie que le motif correspond à zéro ou plusieurs fois ce qui précède le `*`.

Lorsque nous appelons cette macro avec `vec![1, 2, 3];`, le motif `$x` correspond trois fois aux trois expressions `1`, `2` et `3`.

Maintenant, regardons le motif dans le corps du code associé à ce bras : `temp_vec.push()` \[5\] à l'intérieur de `$()* à [4] et [7] est généré pour chaque partie qui correspond à`$()` dans le motif zéro ou plusieurs fois selon combien de fois le motif correspond. Le `$x`[6] est remplacé par chaque expression correspondante. Lorsque nous appelons cette macro avec`vec\[1, 2, 3\];\`, le code généré qui remplace cet appel de macro sera le suivant :

    {
        let mut temp_vec = Vec::new();
        temp_vec.push(1);
        temp_vec.push(2);
        temp_vec.push(3);
        temp_vec
    }

Nous avons défini une macro qui peut prendre un nombre quelconque d'arguments de n'importe quel type et peut générer du code pour créer un vecteur contenant les éléments spécifiés.

Pour en savoir plus sur la manière d'écrire des macros, consultez la documentation en ligne ou d'autres ressources, telles que "The Little Book of Rust Macros" à *https://veykril.github.io/tlborm* initié par Daniel Keep et poursuivi par Lukas Wirth.
