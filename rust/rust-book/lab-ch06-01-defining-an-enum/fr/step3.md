# L'énumération Option et ses avantages par rapport aux valeurs nulles

Cette section explore une étude de cas de `Option`, qui est une autre énumération définie par la bibliothèque standard. Le type `Option` encode le scénario très courant dans lequel une valeur peut être quelque chose ou ne rien être.

Par exemple, si vous demandez le premier élément d'une liste contenant plusieurs éléments, vous obtiendrez une valeur. Si vous demandez le premier élément d'une liste vide, vous n'obtiendrez rien. Exprimer ce concept au niveau du système de types signifie que le compilateur peut vérifier si vous avez traité tous les cas que vous devriez traiter ; cette fonctionnalité peut empêcher des bugs extrêmement courants dans d'autres langages de programmation.

La conception des langages de programmation est souvent considérée en termes des fonctionnalités que vous incluez, mais les fonctionnalités que vous excluez sont également importantes. Rust n'a pas la fonctionnalité null que de nombreux autres langages ont. _Null_ est une valeur qui signifie qu'il n'y a pas de valeur là. Dans les langages avec null, les variables peuvent toujours être dans l'un des deux états : null ou non-null.

Dans sa présentation de 2009 intitulée "Null References: The Billion Dollar Mistake", Tony Hoare, l'inventeur de null, a ceci à dire :

> Je l'appelle ma grosse erreur de milliards de dollars. À l'époque, je concevais le premier système de types complet pour les références dans un langage orienté objet. Mon objectif était de garantir que toute utilisation des références soit absolument sûre, avec des vérifications effectuées automatiquement par le compilateur. Mais je n'ai pas résisté à la tentation d'ajouter une référence null, simplement parce que c'était si facile à implémenter. Cela a entraîné d'innombrables erreurs, vulnérabilités et plantages de systèmes, qui ont probablement causé des milliards de dollars de problèmes et de dégâts au cours des quarante dernières années. Le problème avec les valeurs nulles est que si vous essayez d'utiliser une valeur null comme une valeur non-nulle, vous obtiendrez une erreur de quelque type. Étant donné que cette propriété null ou non-null est omniprésente, il est extrêmement facile de commettre ce genre d'erreur.

Cependant, le concept que null essaie d'exprimer est toujours un concept utile : un null est une valeur qui est actuellement invalide ou absente pour une certaine raison.

Le problème n'est pas vraiment avec le concept mais avec la mise en œuvre particulière. En conséquence, Rust n'a pas de nulls, mais il a une énumération qui peut encoder le concept d'une valeur étant présente ou absente. Cette énumération est `Option<T>`, et elle est définie par la bibliothèque standard comme suit :

```rust
enum Option<T> {
    None,
    Some(T),
}
```

L'énumération `Option<T>` est si utile qu'elle est même incluse dans le préambule ; vous n'avez pas besoin de l'importer explicitement dans votre portée. Ses variantes sont également incluses dans le préambule : vous pouvez utiliser `Some` et `None` directement sans le préfixe `Option::`. L'énumération `Option<T>` est toujours juste une énumération normale, et `Some(T)` et `None` sont toujours des variantes du type `Option<T>`.

La syntaxe `<T>` est une fonctionnalité de Rust dont nous n'avons pas encore parlé. C'est un paramètre de type générique, et nous aborderons les génériques en détail au chapitre 10. Pour l'instant, tout ce que vous avez besoin de savoir est que `<T>` signifie que la variante `Some` de l'énumération `Option` peut contenir une donnée de n'importe quel type, et que chaque type concret qui est utilisé à la place de `T` rend le type `Option<T>` global un type différent. Voici quelques exemples d'utilisation de valeurs `Option` pour stocker des types numériques et des types de chaînes :

```rust
let some_number = Some(5);
let some_char = Some('e');

let absent_number: Option<i32> = None;
```

Le type de `some_number` est `Option<i32>`. Le type de `some_char` est `Option<char>`, qui est un type différent. Rust peut déduire ces types car nous avons spécifié une valeur à l'intérieur de la variante `Some`. Pour `absent_number`, Rust nous oblige à annoter le type `Option` global : le compilateur ne peut pas déduire le type que la variante `Some` correspondante contiendra en ne regardant que la valeur `None`. Ici, nous disons à Rust que nous voulons que `absent_number` soit de type `Option<i32>`.

Lorsque nous avons une valeur `Some`, nous savons qu'une valeur est présente et que la valeur est contenue dans `Some`. Lorsque nous avons une valeur `None`, en un certain sens, cela signifie la même chose que null : nous n'avons pas de valeur valide. Alors pourquoi avoir `Option<T>` est-il meilleur que d'avoir null?

En résumé, parce que `Option<T>` et `T` (où `T` peut être n'importe quel type) sont des types différents, le compilateur ne nous permettra pas d'utiliser une valeur `Option<T>` comme si elle était définitivement une valeur valide. Par exemple, ce code ne compilera pas, car il essaie d'ajouter un `i8` à un `Option<i8>` :

```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);

let sum = x + y;
```

Si nous exécutons ce code, nous obtenons un message d'erreur comme celui-ci :

```bash
error[E0277]: cannot add `Option<i8>` to `i8`
 --> src/main.rs:5:17
  |
5 |     let sum = x + y;
  |                 ^ no implementation for `i8 + Option<i8>`
  |
  = help: the trait `Add<Option<i8>>` is not implemented for `i8`
```

Intense! En fait, ce message d'erreur signifie que Rust ne sait pas comment ajouter un `i8` et un `Option<i8>`, car ce sont des types différents. Lorsque nous avons une valeur d'un type comme `i8` en Rust, le compilateur veillera à ce que nous ayons toujours une valeur valide. Nous pouvons procéder avec confiance sans avoir à vérifier si la valeur est null avant de l'utiliser. Seule lorsque nous avons une `Option<i8>` (ou n'importe quel type de valeur avec lequel nous travaillons), nous devons nous soucier du fait que nous n'ayons peut-être pas de valeur, et le compilateur veillera à ce que nous traitons ce cas avant d'utiliser la valeur.

En d'autres termes, vous devez convertir une `Option<T>` en un `T` avant de pouvoir effectuer des opérations sur `T` avec elle. Généralement, cela aide à détecter l'un des problèmes les plus courants avec null : supposer que quelque chose n'est pas null lorsqu'il l'est effectivement.

Éliminer le risque d'assumer incorrectement une valeur non-nulle vous aide à être plus confiant dans votre code. Pour avoir une valeur qui peut éventuellement être null, vous devez explicitement choisir de le faire en donnant à ce type de valeur le type `Option<T>`. Ensuite, lorsque vous utilisez cette valeur, vous êtes obligé d'explicitement gérer le cas où la valeur est null. Partout où une valeur a un type qui n'est pas un `Option<T>`, vous _pouvez_ supposer avec confiance que la valeur n'est pas null. Cette décision de conception délibérée de Rust vise à limiter la généralité de null et à augmenter la sécurité du code Rust.

Alors, comment extraire la valeur `T` d'une variante `Some` lorsque vous avez une valeur de type `Option<T>` afin que vous puissiez utiliser cette valeur? L'énumération `Option<T>` a un grand nombre de méthodes qui sont utiles dans diverses situations ; vous pouvez les consulter dans sa documentation. Devenir familier avec les méthodes sur `Option<T>` sera extrêmement utile dans votre parcours avec Rust.

En général, pour utiliser une valeur `Option<T>`, vous voulez avoir du code qui traitera chaque variante. Vous voulez du code qui ne s'exécutera que lorsque vous avez une valeur `Some(T)`, et ce code est autorisé à utiliser le `T` interne. Vous voulez un autre code qui ne s'exécutera que si vous avez une valeur `None`, et ce code n'a pas de valeur `T` disponible. L'expression `match` est une construction de contrôle de flux qui fait exactement cela lorsqu'elle est utilisée avec des enums : elle exécutera du code différent selon la variante de l'énumération qu'elle a, et ce code peut utiliser les données à l'intérieur de la valeur correspondante.
