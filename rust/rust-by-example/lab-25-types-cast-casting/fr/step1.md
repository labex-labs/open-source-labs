# Typage explicite

Rust ne fournit pas de conversion implicite de type (coercition) entre les types primitifs. Cependant, une conversion de type explicite (typage) peut être effectuée en utilisant le mot clé `as`.

Les règles de conversion entre les types entiers suivent généralement les conventions C, sauf dans les cas où C présente un comportement indéfini. Le comportement de tous les typages entre les types entiers est bien défini en Rust.

```rust
// Supprime tous les avertissements provenant de typages qui entraînent un dépassement de capacité.
#![allow(overflowing_literals)]

fn main() {
    let decimal = 65.4321_f32;

    // Erreur! Aucune conversion implicite
    let integer: u8 = decimal;
    // FIXME ^ Commenter cette ligne

    // Conversion explicite
    let integer = decimal as u8;
    let character = integer as char;

    // Erreur! Il y a des limites dans les règles de conversion.
    // Un nombre à virgule flottante ne peut pas être directement converti en un caractère.
    let character = decimal as char;
    // FIXME ^ Commenter cette ligne

    println!("Typage : {} -> {} -> {}", decimal, integer, character);

    // Lors du typage de n'importe quelle valeur en un type non signé, T,
    // T::MAX + 1 est ajouté ou soustrait jusqu'à ce que la valeur
    // rentre dans le nouveau type

    // 1000 rentre déjà dans un u16
    println!("1000 en tant que u16 est : {}", 1000 as u16);

    // 1000 - 256 - 256 - 256 = 232
    // Sous le capot, les 8 premiers bits les moins significatifs (LSB) sont conservés,
    // tandis que le reste vers le bit le plus significatif (MSB) est tronqué.
    println!("1000 en tant que u8 est : {}", 1000 as u8);
    // -1 + 256 = 255
    println!("  -1 en tant que u8 est : {}", (-1i8) as u8);

    // Pour les nombres positifs, c'est la même chose que le modulo
    println!("1000 modulo 256 est : {}", 1000 % 256);

    // Lors du typage en un type signé, le résultat (au niveau du bit) est le même que
    // d'abord typage en le type non signé correspondant. Si le bit le plus significatif
    // de cette valeur est 1, alors la valeur est négative.

    // Sauf bien sûr si elle rentre déjà.
    println!(" 128 en tant que i16 est : {}", 128 as i16);

    // Dans le cas limite, la valeur 128 en représentation à complément à deux sur 8 bits est -128
    println!(" 128 en tant que i8 est : {}", 128 as i8);

    // Répétition de l'exemple ci-dessus
    // 1000 en tant que u8 -> 232
    println!("1000 en tant que u8 est : {}", 1000 as u8);
    // et la valeur de 232 en représentation à complément à deux sur 8 bits est -24
    println!(" 232 en tant que i8 est : {}", 232 as i8);

    // Depuis Rust 1.45, le mot clé `as` effectue un *typage saturant*
    // lors du typage d'un nombre à virgule flottante en un entier. Si la valeur flottante dépasse
    // la borne supérieure ou est inférieure à la borne inférieure, la valeur renvoyée
    // sera égale à la borne dépassée.

    // 300.0 en tant que u8 est 255
    println!(" 300.0 en tant que u8 est : {}", 300.0_f32 as u8);
    // -100.0 en tant que u8 est 0
    println!("-100.0 en tant que u8 est : {}", -100.0_f32 as u8);
    // nan en tant que u8 est 0
    println!("   nan en tant que u8 est : {}", f32::NAN as u8);

    // Ce comportement entraîne un coût de runtime légèrement plus élevé et peut être évité
    // avec des méthodes non sûres, cependant les résultats peuvent déborder et
    // renvoyer des **valeurs non valides**. Utilisez ces méthodes avec prudence :
    unsafe {
        // 300.0 en tant que u8 est 44
        println!(" 300.0 en tant que u8 est : {}", 300.0_f32.to_int_unchecked::<u8>());
        // -100.0 en tant que u8 est 156
        println!("-100.0 en tant que u8 est : {}", (-100.0_f32).to_int_unchecked::<u8>());
        // nan en tant que u8 est 0
        println!("   nan en tant que u8 est : {}", f32::NAN.to_int_unchecked::<u8>());
    }
}
```
