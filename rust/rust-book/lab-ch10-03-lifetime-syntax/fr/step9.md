# Lifetime Elision

Vous avez appris que chaque référence a une durée de vie et que vous devez spécifier des paramètres de durée de vie pour les fonctions ou les structs qui utilisent des références. Cependant, nous avons eu une fonction dans la Liste 4-9, montrée à nouveau dans la Liste 10-25, qui a compilé sans annotations de durée de vie.

Nom de fichier : `src/lib.rs`

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Liste 10-25: Une fonction que nous avons définie dans la Liste 4-9 qui a compilé sans annotations de durée de vie, même si le type de paramètre et de retour est une référence

La raison pour laquelle cette fonction compile sans annotations de durée de vie est historique : dans les premières versions (avant 1.0) de Rust, ce code n'aurait pas compilé car chaque référence avait besoin d'une durée de vie explicite. À l'époque, la signature de la fonction aurait été écrite comme ceci :

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Après avoir écrit beaucoup de code Rust, l'équipe Rust a constaté que les programmeurs Rust entrait les mêmes annotations de durée de vie à répétition dans des situations particulières. Ces situations étaient prévisibles et suivaient quelques modèles déterministes. Les développeurs ont programmé ces modèles dans le code du compilateur de sorte que le vérificateur d'emprunt puisse inférer les durées de vie dans ces situations et n'ait pas besoin d'annotations explicites.

Cette partie de l'histoire de Rust est pertinente car il est possible que de nouveaux modèles déterministes apparaissent et soient ajoutés au compilateur. Dans l'avenir, peut-être que même moins d'annotations de durée de vie seront requises.

Les modèles programmés dans l'analyse de références de Rust sont appelés les _règles d'élision de durée de vie_. Ce ne sont pas des règles pour les programmeurs à suivre ; ce sont un ensemble de cas particuliers que le compilateur considérera, et si votre code correspond à ces cas, vous n'avez pas besoin d'écrire explicitement les durées de vie.

Les règles d'élision ne fournissent pas une inférence complète. Si Rust applique de manière déterministe les règles mais qu'il reste une ambiguïté quant aux durées de vie des références, le compilateur ne devinera pas quelle devrait être la durée de vie des références restantes. Au lieu de deviner, le compilateur vous donnera une erreur que vous pouvez résoudre en ajoutant les annotations de durée de vie.

Les durées de vie sur les paramètres de fonction ou de méthode sont appelées _durées de vie d'entrée_, et les durées de vie sur les valeurs de retour sont appelées _durées de vie de sortie_.

Le compilateur utilise trois règles pour déterminer les durées de vie des références lorsqu'il n'y a pas d'annotations explicites. La première règle s'applique aux durées de vie d'entrée, et les deuxième et troisième règles s'appliquent aux durées de vie de sortie. Si le compilateur arrive à la fin des trois règles et qu'il reste encore des références pour lesquelles il ne peut pas déterminer les durées de vie, le compilateur s'arrêtera avec une erreur. Ces règles s'appliquent aux définitions de `fn` ainsi qu'aux blocs `impl`.

La première règle est que le compilateur attribue un paramètre de durée de vie à chaque paramètre qui est une référence. En d'autres termes, une fonction avec un paramètre obtient un paramètre de durée de vie : `fn foo<'a>(x: &'a i32)` ; une fonction avec deux paramètres obtient deux paramètres de durée de vie séparés : `fn foo<'a, 'b>(x: &'a i32, y: &'b i32)` ; et ainsi de suite.

La deuxième règle est que, s'il y a exactement un paramètre de durée de vie d'entrée, cette durée de vie est attribuée à tous les paramètres de durée de vie de sortie : `fn foo<'a>(x: &'a i32) -> &'a i32`.

La troisième règle est que, s'il y a plusieurs paramètres de durée de vie d'entrée, mais que l'un d'entre eux est `&self` ou `&mut self` car il s'agit d'une méthode, la durée de vie de `self` est attribuée à tous les paramètres de durée de vie de sortie. Cette troisième règle rend les méthodes beaucoup plus agréables à lire et à écrire car il est nécessaire de moins de symboles.

Pretendons que nous soyons le compilateur. Nous allons appliquer ces règles pour déterminer les durées de vie des références dans la signature de la fonction `first_word` de la Liste 10-25. La signature commence sans aucune durée de vie associée aux références :

```rust
fn first_word(s: &str) -> &str {
```

Ensuite, le compilateur applique la première règle, qui spécifie que chaque paramètre obtient sa propre durée de vie. Nous l'appellerons `'a` comme d'habitude, donc maintenant la signature est la suivante :

```rust
fn first_word<'a>(s: &'a str) -> &str {
```

La deuxième règle s'applique car il y a exactement un paramètre de durée de vie d'entrée. La deuxième règle spécifie que la durée de vie du paramètre d'entrée unique est attribuée à la durée de vie de sortie, donc la signature est maintenant la suivante :

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Maintenant, toutes les références dans cette signature de fonction ont des durées de vie, et le compilateur peut continuer son analyse sans que le programmeur ait besoin d'annoter les durées de vie dans cette signature de fonction.

Regardons un autre exemple, cette fois en utilisant la fonction `longest` qui n'avait pas de paramètres de durée de vie lorsque nous l'avons commencé à utiliser dans la Liste 10-20 :

```rust
fn longest(x: &str, y: &str) -> &str {
```

Appliquons la première règle : chaque paramètre obtient sa propre durée de vie. Cette fois, nous avons deux paramètres au lieu d'un, donc nous avons deux durées de vie :

```rust
fn longest<'a, 'b>(x: &'a str, y: &'b str) -> &str {
```

Vous pouvez voir que la deuxième règle ne s'applique pas car il y a plus d'un paramètre de durée de vie d'entrée. La troisième règle ne s'applique pas non plus, car `longest` est une fonction plutôt qu'une méthode, donc aucun des paramètres n'est `self`. Après avoir parcouru les trois règles, nous n'avons toujours pas déterminé quelle est la durée de vie du type de retour. C'est pourquoi nous avons eu une erreur en essayant de compiler le code de la Liste 10-20 : le compilateur a parcouru les règles d'élision de durée de vie mais n'a toujours pas pu déterminer toutes les durées de vie des références dans la signature.

Parce que la troisième règle ne s'applique vraiment que dans les signatures de méthodes, nous allons examiner les durées de vie dans ce contexte ensuite pour voir pourquoi la troisième règle signifie que nous n'avons pas besoin d'annoter les durées de vie dans les signatures de méthodes très souvent.
