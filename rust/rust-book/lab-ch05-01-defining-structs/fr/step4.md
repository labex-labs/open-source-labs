# Utiliser des structs tuple sans champs nommés pour créer différents types

Rust prend également en charge des structs qui ressemblent aux tuples, appelés _structs tuple_. Les structs tuple ont la signification supplémentaire que le nom du struct apporte, mais n'ont pas de noms associés à leurs champs ; au lieu de cela, ils ont simplement les types des champs. Les structs tuple sont utiles lorsque vous voulez donner un nom à l'ensemble du tuple et que vous voulez que le tuple soit un type différent des autres tuples, et lorsque nommer chaque champ comme dans un struct classique serait verbeux ou redondant.

Pour définir un struct tuple, commencer par le mot clé `struct` et le nom du struct suivi des types dans le tuple. Par exemple, ici nous définissons et utilisons deux structs tuple nommés `Color` et `Point` :

Nom de fichier : `src/main.rs`

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

Notez que les valeurs `black` et `origin` sont de différents types car elles sont des instances de différents structs tuple. Chaque struct que vous définissez est un type propre, même si les champs à l'intérieur du struct peuvent avoir les mêmes types. Par exemple, une fonction qui prend un paramètre de type `Color` ne peut pas prendre un `Point` en argument, même si les deux types sont composés de trois valeurs `i32`. Sinon, les instances de struct tuple sont similaires aux tuples dans le sens où vous pouvez les décomposer en leurs parties individuelles, et vous pouvez utiliser un `.` suivi de l'index pour accéder à une valeur individuelle.
