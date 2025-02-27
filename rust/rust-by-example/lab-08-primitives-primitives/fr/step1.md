# Primitives

Rust fournit un accès à une grande variété de `primitives`. Voici un exemple :

## Types scalaires

- Entiers signés : `i8`, `i16`, `i32`, `i64`, `i128` et `isize` (taille de pointeur)
- Entiers non signés : `u8`, `u16`, `u32`, `u64`, `u128` et `usize` (taille de pointeur)
- Nombres à virgule flottante : `f32`, `f64`
- Valeurs scalaires Unicode `char` telles que `'a'`, `'α'` et `'∞'` (4 octets chacune)
- `bool` soit `true` soit `false`
- Le type unité `()`, dont la seule valeur possible est un tuple vide : `()`

Malgré la valeur d'un type unité étant un tuple, il n'est pas considéré comme un type composé car il ne contient pas plusieurs valeurs.

## Types composites

- Tableaux comme `[1, 2, 3]`
- Tuples comme `(1, true)`

Les variables peuvent toujours être _annotées avec leur type_. Les nombres peuvent également être annotés via un _suffixe_ ou _par défaut_. Les entiers ont comme valeur par défaut `i32` et les flottants `f64`. Notez que Rust peut également inférer les types à partir du contexte.

```rust
fn main() {
    // Les variables peuvent être annotées avec leur type.
    let logique: bool = true;

    let un_flottant: f64 = 1.0;  // Annotation classique
    let un_entier   = 5i32; // Annotation avec suffixe

    // Ou une valeur par défaut sera utilisée.
    let flottant_par_defaut   = 3.0; // `f64`
    let entier_par_defaut = 7;   // `i32`

    // Un type peut également être inferé à partir du contexte.
    let mut type_inferé = 12; // Le type i64 est inferé à partir d'une autre ligne.
    type_inferé = 4294967296i64;

    // La valeur d'une variable mutable peut être changée.
    let mut mutable = 12; // `i32` mutable
    mutable = 21;

    // Erreur! Le type d'une variable ne peut pas être changé.
    mutable = true;

    // Les variables peuvent être écrasées par ombre.
    let mutable = true;
}
```
