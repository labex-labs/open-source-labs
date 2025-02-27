# Comment écrire une macro personnalisée `derive`

Créons une crate appelée `hello_macro` qui définit un trait nommé `HelloMacro` avec une fonction associée nommée `hello_macro`. Au lieu de demander à nos utilisateurs d'implémenter le trait `HelloMacro` pour chacun de leurs types, nous allons fournir une macro procédurale de sorte que les utilisateurs puissent annoter leur type avec `#[derive(HelloMacro)]` pour obtenir une implémentation par défaut de la fonction `hello_macro`. L'implémentation par défaut imprimera `Hello, Macro! My name is` TypeName`!` où TypeName est le nom du type sur lequel ce trait a été défini. En d'autres termes, nous allons écrire une crate qui permettra à un autre programmeur d'écrire du code comme dans l'annexe 19-30 en utilisant notre crate.

Nom de fichier : `src/main.rs`

```rust
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
```

Annexe 19-30 : Le code que l'utilisateur de notre crate pourra écrire en utilisant notre macro procédurale

Ce code imprimera `Hello, Macro! My name is Pancakes!` une fois que nous aurons terminé. La première étape est de créer une nouvelle crate bibliothèque, comme ceci :

```bash
cargo new hello_macro --lib
```

Ensuite, nous définirons le trait `HelloMacro` et sa fonction associée :

Nom de fichier : `src/lib.rs`

```rust
pub trait HelloMacro {
    fn hello_macro();
}
```

Nous avons un trait et sa fonction. À ce stade, l'utilisateur de notre crate pourrait implémenter le trait pour obtenir la fonctionnalité souhaitée, comme ceci :

```rust
use hello_macro::HelloMacro;

struct Pancakes;

impl HelloMacro for Pancakes {
    fn hello_macro() {
        println!("Hello, Macro! My name is Pancakes!");
    }
}

fn main() {
    Pancakes::hello_macro();
}
```

Cependant, ils devraient écrire le bloc d'implémentation pour chaque type qu'ils souhaitent utiliser avec `hello_macro` ; nous voulons les épargner de cette tâche.

De plus, nous ne pouvons pas encore fournir à la fonction `hello_macro` une implémentation par défaut qui imprimera le nom du type sur lequel le trait est implémenté : Rust n'a pas de capacités de réflexion, donc il ne peut pas rechercher le nom du type à l'exécution. Nous avons besoin d'une macro pour générer du code à la compilation.

L'étape suivante est de définir la macro procédurale. Au moment de l'écriture de ce document, les macros procédurales doivent être dans leur propre crate. Eventuellement, cette restriction pourrait être levée. La convention pour structurer les crates et les crates de macros est la suivante : pour une crate nommée foo, une crate de macro procédurale personnalisée `derive` est appelée foo`_derive`. Commençons une nouvelle crate appelée `hello_macro_derive` dans notre projet `hello_macro` :

```bash
cargo new hello_macro_derive --lib
```

Nos deux crates sont étroitement liées, donc nous créons la crate de macro procédurale dans le répertoire de notre crate `hello_macro`. Si nous modifions la définition du trait dans `hello_macro`, nous devrons également modifier l'implémentation de la macro procédurale dans `hello_macro_derive`. Les deux crates devront être publiées séparément, et les programmeurs utilisant ces crates devront les ajouter toutes les deux comme dépendances et les porter toutes les deux en contexte. Nous pourrions au lieu de cela faire en sorte que la crate `hello_macro` utilise `hello_macro_derive` comme dépendance et réexporte le code de la macro procédurale. Cependant, la manière dont nous avons structuré le projet permet aux programmeurs d'utiliser `hello_macro` même s'ils ne veulent pas la fonctionnalité `derive`.

Nous devons déclarer la crate `hello_macro_derive` comme une crate de macro procédurale. Nous aurons également besoin des fonctionnalités des crates `syn` et `quote`, comme vous le verrez tout de suite, donc nous devons les ajouter comme dépendances. Ajoutez le suivant au fichier `Cargo.toml` pour `hello_macro_derive` :

Nom de fichier : `hello_macro_derive/Cargo.toml`

```toml
[lib]
proc-macro = true

[dependencies]
syn = "1.0"
quote = "1.0"
```

Pour commencer à définir la macro procédurale, placez le code de l'annexe 19-31 dans votre fichier `src/lib.rs` pour la crate `hello_macro_derive`. Notez que ce code ne compilera pas jusqu'à ce que vous ajoutiez une définition pour la fonction `impl_hello_macro`.

Nom de fichier : `hello_macro_derive/src/lib.rs`

```rust
use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    // Construit une représentation du code Rust sous forme d'un arbre de syntaxe
    // que nous pouvons manipuler
    let ast = syn::parse(input).unwrap();

    // Génère l'implémentation du trait
    impl_hello_macro(&ast)
}
```

Annexe 19-31 : Code que la plupart des crates de macros procédurales nécessiteront pour traiter le code Rust

Remarquez que nous avons divisé le code en la fonction `hello_macro_derive`, qui est responsable de l'analyse du `TokenStream`, et la fonction `impl_hello_macro`, qui est responsable de la transformation de l'arbre de syntaxe : cela facilite l'écriture d'une macro procédurale. Le code dans la fonction externe (`hello_macro_derive` dans ce cas) sera le même pour presque toutes les crates de macros procédurales que vous verrez ou créerez. Le code que vous spécifiez dans le corps de la fonction interne (`impl_hello_macro` dans ce cas) sera différent selon le but de votre macro procédurale.

Nous avons introduit trois nouvelles crates : `proc_macro`, `syn` (disponible sur *https://crates.io/crates/syn*), et `quote` (disponible sur *https://crates.io/crates/quote*). La crate `proc_macro` est incluse avec Rust, donc nous n'avons pas eu besoin d'ajouter cela aux dépendances dans `Cargo.toml`. La crate `proc_macro` est l'API du compilateur qui nous permet de lire et de manipuler le code Rust à partir de notre code.

La crate `syn` analyse le code Rust à partir d'une chaîne en une structure de données sur laquelle nous pouvons effectuer des opérations. La crate `quote` convertit les structures de données `syn` en nouveau code Rust. Ces crates simplifient considérablement l'analyse de n'importe quel type de code Rust que nous pourrions vouloir traiter : écrire un analyseur complet pour le code Rust n'est pas une tâche simple.

La fonction `hello_macro_derive` sera appelée lorsqu'un utilisateur de notre bibliothèque spécifiera `#[derive(HelloMacro)]` sur un type. Cela est possible car nous avons annoté la fonction `hello_macro_derive` ici avec `proc_macro_derive` et spécifié le nom `HelloMacro`, qui correspond à notre nom de trait ; c'est la convention la plus suivie par la plupart des macros procédurales.

La fonction `hello_macro_derive` convertit d'abord l'`input` d'un `TokenStream` en une structure de données que nous pouvons ensuite interpréter et sur laquelle effectuer des opérations. C'est là que `syn` intervient. La fonction `parse` dans `syn` prend un `TokenStream` et renvoie une structure `DeriveInput` représentant le code Rust analysé. L'annexe 19-32 montre les parties pertinentes de la structure `DeriveInput` que nous obtenons en analysant la chaîne `struct Pancakes;`.

    DeriveInput {
        --snip--

        ident: Ident {
            ident: "Pancakes",
            span: #0 bytes(95..103)
        },
        data: Struct(
            DataStruct {
                struct_token: Struct,
                fields: Unit,
                semi_token: Some(
                    Semi
                )
            }
        )
    }

Annexe 19-32 : L'instance `DeriveInput` que nous obtenons en analysant le code qui a l'attribut de la macro dans l'annexe 19-30

Les champs de cette structure montrent que le code Rust que nous avons analysé est une structure unitaire avec l'`ident` (_identifiant_, c'est-à-dire le nom) de `Pancakes`. Il y a plus de champs sur cette structure pour décrire tout type de code Rust ; consultez la documentation `syn` pour `DeriveInput` sur *https://docs.rs/syn/1.0/syn/struct.DeriveInput.html* pour plus d'informations.

Bientôt, nous définirons la fonction `impl_hello_macro`, qui est là où nous construireons le nouveau code Rust que nous voulons inclure. Mais avant de le faire, notez que la sortie de notre macro `derive` est également un `TokenStream`. Le `TokenStream` renvoyé est ajouté au code que les utilisateurs de notre crate écrivent, de sorte que lorsqu'ils compilent leur crate, ils obtiendront la fonctionnalité supplémentaire que nous fournissons dans le `TokenStream` modifié.

Vous avez peut-être remarqué que nous appelons `unwrap` pour faire en sorte que la fonction `hello_macro_derive` génère une panique si l'appel à la fonction `syn::parse` échoue ici. Il est nécessaire que notre macro procédurale génère une panique en cas d'erreur car les fonctions `proc_macro_derive` doivent renvoyer un `TokenStream` plutôt qu'un `Result` pour être conformes à l'API de la macro procédurale. Nous avons simplifié cet exemple en utilisant `unwrap` ; dans le code de production, vous devriez fournir des messages d'erreur plus spécifiques sur ce qui s'est mal passé en utilisant `panic!` ou `expect`.

Maintenant que nous avons le code pour convertir le code Rust annoté d'un `TokenStream` en une instance `DeriveInput`, générons le code qui implémente le trait `HelloMacro` sur le type annoté, comme montré dans l'annexe 19-33.

Nom de fichier : `hello_macro_derive/src/lib.rs`

```rust
fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!(
                    "Hello, Macro! My name is {}!",
                    stringify!(#name)
                );
            }
        }
    };
    gen.into()
}
```

Annexe 19-33 : Implémentation du trait `HelloMacro` en utilisant le code Rust analysé

Nous obtenons une instance de la structure `Ident` contenant le nom (identifiant) du type annoté en utilisant `ast.ident`. La structure dans l'annexe 19-32 montre que lorsque nous exécutons la fonction `impl_hello_macro` sur le code dans l'annexe 19-30, l'`ident` que nous obtenons aura le champ `ident` avec une valeur de `"Pancakes"`. Ainsi, la variable `name` dans l'annexe 19-33 contiendra une instance de la structure `Ident` qui, lorsqu'elle est imprimée, sera la chaîne `"Pancakes"`, le nom de la structure dans l'annexe 19-30.

La macro `quote!` nous permet de définir le code Rust que nous voulons renvoyer. Le compilateur attend quelque chose de différent du résultat direct de l'exécution de la macro `quote!`, donc nous devons le convertir en un `TokenStream`. Nous le faisons en appelant la méthode `into`, qui consomme cette représentation intermédiaire et renvoie une valeur du type `TokenStream` requis.

La macro `quote!` fournit également des mécanismes de mise en page très sympas : nous pouvons entrer `#name`, et `quote!` le remplacera par la valeur dans la variable `name`. Vous pouvez même faire une certaine répétition similaire à la manière dont fonctionnent les macros régulières. Consultez la documentation de la crate `quote` sur *https://docs.rs/quote* pour une introduction approfondie.

Nous voulons que notre macro procédurale génère une implémentation de notre trait `HelloMacro` pour le type annoté par l'utilisateur, que nous pouvons obtenir en utilisant `#name`. L'implémentation du trait a la fonction unique `hello_macro`, dont le corps contient la fonctionnalité que nous voulons fournir : imprimer `Hello, Macro! My name is` puis le nom du type annoté.

La macro `stringify!` utilisée ici est intégrée à Rust. Elle prend une expression Rust, telle que `1 + 2`, et à la compilation, elle convertit l'expression en une chaîne littérale, telle que `"1 + 2"`. Cela est différent de `format!` ou `println!`, qui évaluent l'expression puis convertissent le résultat en une `String`. Il y a une possibilité que l'entrée `#name` soit une expression à imprimer littéralement, donc nous utilisons `stringify!`. Utiliser `stringify!` économise également une allocation en convertissant `#name` en une chaîne littérale à la compilation.

À ce stade, `cargo build` devrait réussir dans les deux crates `hello_macro` et `hello_macro_derive`. Essayons de connecter ces crates au code dans l'annexe 19-30 pour voir la macro procédurale en action! Créez un nouveau projet binaire dans votre répertoire `project` en utilisant `cargo new pancakes`. Nous devons ajouter `hello_macro` et `hello_macro_derive` comme dépendances dans le `Cargo.toml` de la crate `pancakes`. Si vous publiez vos versions de `hello_macro` et `hello_macro_derive` sur *https://crates.io*, ce sera des dépendances normales ; sinon, vous pouvez les spécifier comme dépendances `path` comme suit :

    [dependencies]
    hello_macro = { path = "../hello_macro" }
    hello_macro_derive = { path = "../hello_macro/hello_macro_derive" }

Placez le code de l'annexe 19-30 dans `src/main.rs`, et exécutez `cargo run` : il devrait imprimer `Hello, Macro! My name is Pancakes!` L'implémentation du trait `HelloMacro` provenant de la macro procédurale a été incluse sans que la crate `pancakes` ait besoin de l'implémenter ; l'annotation `#[derive(HelloMacro)]` a ajouté l'implémentation du trait.

Ensuite, explorons comment les autres types de macros procédurales diffèrent des macros personnalisées `derive`.
