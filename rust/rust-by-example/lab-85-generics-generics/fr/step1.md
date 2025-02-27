# Génériques

_Generics_ est le sujet de la généralisation des types et des fonctionnalités à des cas plus larges. Cela est extrêmement utile pour réduire la duplication de code de nombreuses manières, mais peut nécessiter une syntaxe assez complexe. Plus précisément, être générique nécessite de prendre soin de spécifier sur quels types un type générique est effectivement considéré valide. Le plus simple et le plus courant usage des génériques est pour les paramètres de type.

Un paramètre de type est spécifié comme générique en utilisant des crochets et des majuscules
typiquement représenté par `<T>`. En Rust, "générique" décrit également tout ce qui accepte un ou plusieurs paramètres de type générique `<T>`. Tout type spécifié comme paramètre de type générique est générique, et tout le reste est concret (non générique).

Par exemple, en définissant une _fonction générique_ nommée `foo` qui prend un argument `T` de n'importe quel type :

```rust
fn foo<T>(arg: T) {... }
```

Comme `T` a été spécifié comme paramètre de type générique en utilisant `<T>`, il est considéré générique lorsqu'il est utilisé ici comme `(arg: T)`. C'est le cas même si `T` a été précédemment défini comme un `struct`.

Cet exemple montre quelques éléments de syntaxe en action :

```rust
// Un type concret `A`.
struct A;

// En définissant le type `Single`, le premier usage de `A` n'est pas précédé de `<A>`.
// Par conséquent, `Single` est un type concret, et `A` est défini comme ci-dessus.
struct Single(A);
//            ^ Voici le premier usage de `Single` du type `A`.

// Ici, `<T>` précède le premier usage de `T`, donc `SingleGen` est un type générique.
// Étant donné que le paramètre de type `T` est générique, il peut être n'importe quoi, y compris
// le type concret `A` défini en haut.
struct SingleGen<T>(T);

fn main() {
    // `Single` est concret et prend explicitement `A`.
    let _s = Single(A);

    // Crée une variable `_char` de type `SingleGen<char>`
    // et lui donne la valeur `SingleGen('a')`.
    // Ici, `SingleGen` a un paramètre de type spécifié explicitement.
    let _char: SingleGen<char> = SingleGen('a');

    // `SingleGen` peut également avoir un paramètre de type spécifié implicitement :
    let _t    = SingleGen(A); // Utilise `A` défini en haut.
    let _i32  = SingleGen(6); // Utilise `i32`.
    let _char = SingleGen('a'); // Utilise `char`.
}
```
