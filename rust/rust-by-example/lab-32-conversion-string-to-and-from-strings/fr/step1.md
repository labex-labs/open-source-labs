# Conversions entre chaînes de caractères

## Conversion en chaîne de caractères

Convertir n'importe quel type en une `String` est aussi simple qu'en implémentant le trait \[`ToString`\] pour ce type. Plutôt que de le faire directement, vous devriez implémenter le trait `fmt::Display` qui fournit automatiquement \[`ToString`\] et permet également d'afficher le type comme discuté dans la section sur `print!`.

```rust
use std::fmt;

struct Circle {
    radius: i32
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Circle of radius {}", self.radius)
    }
}

fn main() {
    let circle = Circle { radius: 6 };
    println!("{}", circle.to_string());
}
```

## Analyse d'une chaîne de caractères

L'une des conversions les plus courantes est de convertir une chaîne de caractères en un nombre. L'approche habituelle pour ce faire est d'utiliser la fonction \[`parse`\] et de soit permettre l'inférence de type soit de spécifier le type à analyser en utilisant la syntaxe 'turbofish'. Les deux alternatives sont montrées dans l'exemple suivant.

Cela convertira la chaîne de caractères en le type spécifié pourvu que le trait \[`FromStr`\] soit implémenté pour ce type. Ceci est implémenté pour de nombreux types dans la bibliothèque standard. Pour obtenir cette fonctionnalité sur un type défini par l'utilisateur, il suffit d'implémenter le trait \[`FromStr`\] pour ce type.

```rust
fn main() {
    let parsed: i32 = "5".parse().unwrap();
    let turbo_parsed = "10".parse::<i32>().unwrap();

    let sum = parsed + turbo_parsed;
    println!("Sum: {:?}", sum);
}
```
