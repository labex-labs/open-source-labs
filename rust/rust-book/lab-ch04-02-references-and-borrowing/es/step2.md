# Referencias Mutables

Podemos corregir el código de la Lista 4-6 para permitirnos modificar un valor prestado con solo unos pequeños ajustes que usan, en cambio, una _referencia mutable_:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

Primero cambiamos `s` a ser `mut`. Luego creamos una referencia mutable con `&mut s` donde llamamos a la función `change`, y actualizamos la firma de la función para aceptar una referencia mutable con `some_string: &mut String`. Esto hace muy claro que la función `change` mutará el valor que presta.

Las referencias mutables tienen una gran restricción: si tienes una referencia mutable a un valor, no puedes tener otras referencias a ese valor. Este código que intenta crear dos referencias mutables a `s` fallará:

Nombre de archivo: `src/main.rs`

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{r1}, {r2}");
```

Aquí está el error:

```bash
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |              ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |              ^^^^^^ second mutable borrow occurs here
6 |
7 |     println!("{r1}, {r2}");
  |                -- first borrow later used here
```

Este error dice que este código es inválido porque no podemos prestar `s` como mutable más de una vez a la vez. El primer préstamo mutable está en `r1` y debe durar hasta que se use en el `println!`, pero entre la creación de esa referencia mutable y su uso, intentamos crear otra referencia mutable en `r2` que presta los mismos datos que `r1`.

La restricción que impide múltiples referencias mutables al mismo dato al mismo tiempo permite la mutación pero de una manera muy controlada. Es algo con lo que los nuevos Rustaceans luchan porque la mayoría de los lenguajes te dejan mutar cuando quieras. El beneficio de tener esta restricción es que Rust puede prevenir las carreras de datos en tiempo de compilación. Una _carrera de datos_ es similar a una condición de carrera y ocurre cuando ocurren estos tres comportamientos:

- Dos o más punteros acceden al mismo dato al mismo tiempo.
- Al menos uno de los punteros se está usando para escribir en los datos.
- No hay ningún mecanismo que se use para sincronizar el acceso a los datos.

Las carreras de datos causan un comportamiento no definido y pueden ser difíciles de diagnosticar y corregir cuando intentas localizarlas en tiempo de ejecución; Rust evita este problema al rechazar la compilación de código con carreras de datos.

Como siempre, podemos usar llaves para crear un nuevo ámbito, lo que permite múltiples referencias mutables, solo no _simultáneas_:

```rust
let mut s = String::from("hello");

{
    let r1 = &mut s;
} // r1 sale del ámbito aquí, por lo que podemos crear una nueva referencia sin problemas

let r2 = &mut s;
```

Rust impone una regla similar para combinar referencias mutables e inmutables. Este código da como resultado un error:

```rust
let mut s = String::from("hello");

let r1 = &s; // no problema
let r2 = &s; // no problema
let r3 = &mut s; // GRAN PROBLEMA

println!("{r1}, {r2}, and {r3}");
```

Aquí está el error:

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:14
  |
4 |     let r1 = &s; // no problem
  |              -- immutable borrow occurs here
5 |     let r2 = &s; // no problem
6 |     let r3 = &mut s; // GRAN PROBLEMA
  |              ^^^^^^ mutable borrow occurs here
7 |
8 |     println!("{r1}, {r2}, and {r3}");
  |                -- immutable borrow later used here
```

¡Uy! Tampoco podemos tener una referencia mutable mientras tenemos una inmutable al mismo valor.

Los usuarios de una referencia inmutable no esperan que el valor cambie repentinamente por debajo de ellos. Sin embargo, se permiten múltiples referencias inmutables porque nadie que solo está leyendo los datos tiene la capacidad de afectar la lectura de los datos de nadie más.

Tenga en cuenta que el ámbito de una referencia comienza desde donde se introduce y continúa hasta la última vez que se usa esa referencia. Por ejemplo, este código se compilará porque el último uso de las referencias inmutables, el `println!`, ocurre antes de que se introduzca la referencia mutable:

```rust
let mut s = String::from("hello");

let r1 = &s; // no problema
let r2 = &s; // no problema
println!("{r1} and {r2}");
// variables r1 y r2 no se usarán después de este punto

let r3 = &mut s; // no problema
println!("{r3}");
```

Los ámbitos de las referencias inmutables `r1` y `r2` terminan después del `println!` donde se usan por última vez, lo que es antes de que se cree la referencia mutable `r3`. Estos ámbitos no se superponen, por lo que este código está permitido: el compilador puede decir que la referencia ya no se está usando en un punto antes del final del ámbito.

Aunque los errores de préstamo pueden ser frustrantes a veces, recuerde que es el compilador de Rust el que señala un posible error temprano (en tiempo de compilación en lugar de en tiempo de ejecución) y le muestra exactamente dónde está el problema. Entonces no tienes que investigar por qué tus datos no son lo que pensabas que eran.
