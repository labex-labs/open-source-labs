# Expresiones `if let` Condicionales

En el Capítulo 6, discutimos cómo usar las expresiones `if let` principalmente como una forma más corta de escribir lo equivalente a un `match` que solo coincide con un caso. Opcionalmente, `if let` puede tener un `else` correspondiente que contiene el código a ejecutar si el patrón en `if let` no coincide.

El Listado 18-1 muestra que también es posible combinar y mezclar expresiones `if let`, `else if` y `else if let`. Hacer esto nos da más flexibilidad que una expresión `match` en la que solo podemos expresar un solo valor para comparar con los patrones. Además, Rust no requiere que las condiciones en una serie de brazos `if let`, `else if` y `else if let` estén relacionadas entre sí.

El código en el Listado 18-1 determina qué color usar para el fondo basado en una serie de comprobaciones para varias condiciones. Para este ejemplo, hemos creado variables con valores codificados en duro que un programa real podría recibir a partir de la entrada del usuario.

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

  1 if let Some(color) = favorite_color {
      2 println!(
            "Using your favorite, {color}, as the background"
        );
  3 } else if is_tuesday {
      4 println!("Tuesday is green day!");
  5 } else if let Ok(age) = age {
      6 if age > 30 {
          7 println!("Using purple as the background color");
        } else {
          8 println!("Using orange as the background color");
        }
  9 } else {
     10 println!("Using blue as the background color");
    }
}
```

Listado 18-1: Combinando `if let`, `else if`, `else if let` y `else`

Si el usuario especifica un color favorito \[1\], ese color se usa como fondo \[2\]. Si no se especifica un color favorito y hoy es martes \[3\], el color de fondo es verde \[4\]. De lo contrario, si el usuario especifica su edad como una cadena y podemos analizarla correctamente como un número \[5\], el color es o violeta \[7\] o naranja \[8\] dependiendo del valor del número \[6\]. Si ninguna de estas condiciones se aplica \[9\], el color de fondo es azul \[10\].

Esta estructura condicional nos permite soportar requisitos complejos. Con los valores codificados en duro que tenemos aquí, este ejemplo imprimirá `Using purple as the background color`.

Puedes ver que `if let` también puede introducir variables sombreadas de la misma manera que los brazos de `match` pueden: la línea `if let Ok(age) = age` \[5\] introduce una nueva variable `age` sombreada que contiene el valor dentro de la variante `Ok`. Esto significa que necesitamos colocar la condición `if age > 30` \[6\] dentro de ese bloque: no podemos combinar estas dos condiciones en `if let Ok(age) = age && age > 30`. La variable `age` sombreada que queremos comparar con 30 no es válida hasta que el nuevo ámbito comienza con la llave.

La desventaja de usar expresiones `if let` es que el compilador no comprueba la exhaustividad, mientras que con las expresiones `match` sí lo hace. Si omitimos el último bloque `else` \[9\] y, por lo tanto, perdemos el manejo de algunos casos, el compilador no nos alertará sobre el posible error de lógica.
