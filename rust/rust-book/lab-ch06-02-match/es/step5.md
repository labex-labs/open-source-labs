# Patrones Genéricos y el Comodín `_`

Usando `enum`, también podemos tomar acciones especiales para algunos valores particulares, pero para todos los demás valores tomar una acción predeterminada. Imagina que estamos implementando un juego donde, si lanzas un 3 en un lanzamiento de dados, tu jugador no se mueve, sino que obtiene un nuevo sombrero elegante. Si lanzas un 7, tu jugador pierde un sombrero elegante. Para todos los demás valores, tu jugador se mueve esa cantidad de casillas en el tablero de juego. Aquí hay un `match` que implementa esa lógica, con el resultado del lanzamiento de dados codificado en duro en lugar de un valor aleatorio, y toda la otra lógica representada por funciones sin cuerpo porque en realidad implementarlas está fuera del alcance de este ejemplo:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
  1 other => move_player(other),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn move_player(num_spaces: u8) {}
```

Para los primeros dos brazos, los patrones son los valores literales `3` y `7`. Para el último brazo que cubre todos los demás valores posibles, el patrón es la variable que hemos elegido llamar `other` \[1\]. El código que se ejecuta para el brazo `other` utiliza la variable pasándola a la función `move_player`.

Este código se compila, aunque no hayamos enumerado todos los valores posibles que puede tener un `u8`, porque el último patrón coincidirá con todos los valores no específicamente enumerados. Este patrón genérico cumple con la exigencia de que `match` debe ser exhaustivo. Tenga en cuenta que tenemos que poner el brazo genérico al final porque los patrones se evalúan en orden. Si ponemos el brazo genérico antes, los otros brazos nunca se ejecutarán, por lo que Rust nos advertirá si agregamos brazos después de un patrón genérico.

Rust también tiene un patrón que podemos usar cuando queremos un patrón genérico pero no queremos _usar_ el valor en el patrón genérico: `_` es un patrón especial que coincide con cualquier valor y no se enlaza a ese valor. Esto le dice a Rust que no vamos a usar el valor, por lo que Rust no nos advertirá sobre una variable no utilizada.

Cambiemos las reglas del juego: ahora, si lanzas cualquier cosa que no sea un 3 o un 7, debes volver a lanzar. Ya no necesitamos usar el valor genérico, por lo que podemos cambiar nuestro código para usar `_` en lugar de la variable llamada `other`:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => reroll(),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn reroll() {}
```

Este ejemplo también cumple con la exigencia de exhaustividad porque estamos ignorando explícitamente todos los demás valores en el último brazo; no hemos olvidado nada.

Finalmente, cambiaremos las reglas del juego una vez más para que no pase nada más en tu turno si lanzas cualquier cosa que no sea un 3 o un 7. Podemos expresarlo usando el valor unitario (el tipo de tupla vacía que mencionamos en "El Tipo de Tupla") como el código que va con el brazo `_`:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => (),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
```

Aquí, estamos diciendo a Rust explícitamente que no vamos a usar ningún otro valor que no coincida con un patrón en un brazo anterior, y no queremos ejecutar ningún código en este caso.

Hay más sobre patrones y coincidencias que cubriremos en el Capítulo 18. Por ahora, vamos a pasar a la sintaxis `if let`, que puede ser útil en situaciones donde la expresión `match` es un poco verbosa.
