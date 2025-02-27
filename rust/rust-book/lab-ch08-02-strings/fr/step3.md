# Creating a New String

De nombreuses opérations disponibles avec `Vec<T>` sont également disponibles avec `String` car `String` est en fait implémentée comme un wrapper autour d'un vecteur d'octets avec quelques garanties supplémentaires, restrictions et capacités. Un exemple d'une fonction qui fonctionne de la même manière avec `Vec<T>` et `String` est la fonction `new` pour créer une instance, comme montré dans la Liste 8-11.

```rust
let mut s = String::new();
```

Liste 8-11: Création d'une `String` vide et nouvelle

Cette ligne crée une nouvelle chaîne de caractères vide appelée `s`, dans laquelle nous pouvons ensuite charger des données. Souvent, nous aurons des données initiales avec lesquelles nous voulons commencer la chaîne de caractères. Pour cela, nous utilisons la méthode `to_string`, qui est disponible pour tout type qui implémente le trait `Display`, comme les littéraux de chaîne de caractères. La Liste 8-12 montre deux exemples.

```rust
let data = "initial contents";

let s = data.to_string();

// la méthode fonctionne également directement sur un littéral :
let s = "initial contents".to_string();
```

Liste 8-12: Utilisation de la méthode `to_string` pour créer une `String` à partir d'un littéral de chaîne de caractères

Ce code crée une chaîne de caractères contenant `initial contents`.

Nous pouvons également utiliser la fonction `String::from` pour créer une `String` à partir d'un littéral de chaîne de caractères. Le code de la Liste 8-13 est équivalent au code de la Liste 8-12 qui utilise `to_string`.

```rust
let s = String::from("initial contents");
```

Liste 8-13: Utilisation de la fonction `String::from` pour créer une `String` à partir d'un littéral de chaîne de caractères

Parce que les chaînes de caractères sont utilisées pour de nombreuses choses, nous pouvons utiliser de nombreuses API génériques différentes pour les chaînes de caractères, nous offrant ainsi un grand nombre d'options. Certaines d'entre elles peuvent sembler redondantes, mais elles ont toutes leur place! Dans ce cas, `String::from` et `to_string` font la même chose, donc laquelle choisir est une question de style et de lisibilité.

Rappelez-vous que les chaînes de caractères sont encodées en UTF-8, donc nous pouvons y inclure toute donnée correctement encodée, comme montré dans la Liste 8-14.

```rust
let hello = String::from("السلام عليكم");
let hello = String::from("Dobrý den");
let hello = String::from("Hello");
let hello = String::from("שָׁלוֹם");
let hello = String::from("नमस्ते");
let hello = String::from("こんにちは");
let hello = String::from("안녕하세요");
let hello = String::from("你好");
let hello = String::from("Olá");
let hello = String::from("Здравствуйте");
let hello = String::from("Hola");
```

Liste 8-14: Stockage de salutations dans différentes langues dans des chaînes de caractères

Toutes ces valeurs sont des `String` valides.
