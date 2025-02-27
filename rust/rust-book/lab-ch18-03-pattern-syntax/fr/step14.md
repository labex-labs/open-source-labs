# Une variable inutilisée en commençant son nom par \_

Si vous créez une variable mais ne l'utilisez nulle part, Rust vous affichera généralement un avertissement car une variable inutilisée peut être un bogue. Cependant, parfois il est utile de pouvoir créer une variable que vous n'utiliserez pas encore, par exemple lorsque vous protégeez ou que vous commencez un projet. Dans cette situation, vous pouvez dire à Rust de ne pas vous avertir concernant la variable inutilisée en commençant le nom de la variable par un underscore. Dans la Liste 18-20, nous créons deux variables inutilisées, mais lorsque nous compilons ce code, nous devrions seulement recevoir un avertissement concernant l'une d'entre elles.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let _x = 5;
    let y = 10;
}
```

Liste 18-20 : Commencer le nom d'une variable par un underscore pour éviter les avertissements concernant les variables inutilisées

Ici, nous recevons un avertissement concernant l'utilisation de la variable `y`, mais nous ne recevons pas d'avertissement concernant l'utilisation de `_x`.

Notez qu'il existe une différence subtile entre l'utilisation uniquement de `_` et l'utilisation d'un nom commençant par un underscore. La syntaxe `_x` lie toujours la valeur à la variable, tandis que `_` ne lie pas du tout. Pour montrer un cas où cette distinction est importante, la Liste 18-21 nous donnera une erreur.

Nom de fichier : `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_s) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Liste 18-21 : Une variable inutilisée commençant par un underscore lie toujours la valeur, ce qui peut prendre la propriété de la valeur.

Nous recevrons une erreur car la valeur `s` sera toujours déplacée dans `_s`, ce qui nous empêche d'utiliser `s` à nouveau. Cependant, l'utilisation du underscore seul ne lie jamais à la valeur. La Liste 18-22 se compilera sans erreurs car `s` n'est pas déplacé dans `_`.

Nom de fichier : `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Liste 18-22 : L'utilisation d'un underscore ne lie pas la valeur.

Ce code fonctionne parfaitement car nous ne liions jamais `s` à rien ; elle n'est pas déplacée.
