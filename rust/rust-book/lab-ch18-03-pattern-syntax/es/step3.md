# Coincidencia con variables con nombre

Las variables con nombre son patrones irrefutables que coinciden con cualquier valor, y las hemos utilizado muchas veces en este libro. Sin embargo, hay una complicación cuando se utilizan variables con nombre en expresiones `match`. Debido a que `match` inicia un nuevo ámbito, las variables declaradas como parte de un patrón dentro de la expresión `match` sombrearán a aquellas con el mismo nombre fuera de la construcción `match`, como es el caso de todas las variables. En la Lista 18-11, declaramos una variable llamada `x` con el valor `Some(5)` y una variable `y` con el valor `10`. Luego creamos una expresión `match` en el valor `x`. Observa los patrones en los brazos de la coincidencia y `println!` al final, y trata de adivinar lo que imprimirá el código antes de ejecutarlo o leer más.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
  1 let x = Some(5);
  2 let y = 10;

    match x {
      3 Some(50) => println!("Got 50"),
      4 Some(y) => println!("Matched, y = {y}"),
      5 _ => println!("Default case, x = {:?}", x),
    }

  6 println!("at the end: x = {:?}, y = {y}", x);
}
```

Lista 18-11: Una expresión `match` con un brazo que introduce una variable `y` sombreada

Analicemos lo que sucede cuando se ejecuta la expresión `match`. El patrón en el primer brazo de coincidencia \[3\] no coincide con el valor definido de `x` \[1\], por lo que el código continúa.

El patrón en el segundo brazo de coincidencia \[4\] introduce una nueva variable llamada `y` que coincidirá con cualquier valor dentro de un valor `Some`. Debido a que estamos en un nuevo ámbito dentro de la expresión `match`, esta es una nueva variable `y`, no la `y` que declaramos al principio con el valor `10` \[2\]. Esta nueva vinculación `y` coincidirá con cualquier valor dentro de un `Some`, que es lo que tenemos en `x`. Por lo tanto, esta nueva `y` se vincula al valor interno del `Some` en `x`. Ese valor es `5`, por lo que la expresión de ese brazo se ejecuta e imprime `Matched, y = 5`.

Si `x` hubiera sido un valor `None` en lugar de `Some(5)`, los patrones en los primeros dos brazos no habrían coincidido, por lo que el valor habría coincidido con el subrayado \[5\]. No introdujimos la variable `x` en el patrón del brazo del subrayado, por lo que la `x` en la expresión sigue siendo la `x` externa que no ha sido sombreada. En este caso hipotético, la coincidencia imprimiría `Default case, x = None`.

Cuando la expresión `match` finaliza, su ámbito finaliza, y también lo hace el ámbito de la `y` interna. El último `println!` \[6\] produce `at the end: x = Some(5), y = 10`.

Para crear una expresión `match` que compare los valores de la `x` externa y `y`, en lugar de introducir una variable sombreada, necesitaríamos usar una condición de guardia de coincidencia en su lugar. Hablaremos sobre las guardias de coincidencia en "Condicionales adicionales con guardias de coincidencia".
