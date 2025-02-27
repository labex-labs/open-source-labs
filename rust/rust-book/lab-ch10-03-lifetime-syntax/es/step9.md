# Elisión de lifetimes

Has aprendido que cada referencia tiene un lifetime y que necesitas especificar parámetros de lifetime para funciones o structs que usan referencias. Sin embargo, tuvimos una función en la Lista 4-9, que se muestra nuevamente en la Lista 10-25, que se compiló sin anotaciones de lifetime.

Nombre de archivo: `src/lib.rs`

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Lista 10-25: Una función que definimos en la Lista 4-9 que se compiló sin anotaciones de lifetime, aunque el parámetro y el tipo de retorno son referencias

La razón por la que esta función se compila sin anotaciones de lifetime es histórica: en versiones tempranas (antes de la 1.0) de Rust, este código no se habría compilado porque cada referencia necesitaba un lifetime explícito. En aquel momento, la firma de la función se habría escrito así:

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Después de escribir mucho código de Rust, el equipo de Rust descubrió que los programadores de Rust estaban ingresando las mismas anotaciones de lifetime una y otra vez en situaciones particulares. Estas situaciones eran predecibles y seguían unos patrones deterministas. Los desarrolladores programaron estos patrones en el código del compilador para que el verificador de préstamos pudiera inferir los lifetimes en estas situaciones y no necesitara anotaciones explícitas.

Esta parte de la historia de Rust es relevante porque es posible que emerjan más patrones deterministas y se agreguen al compilador. En el futuro, se requerirán aún menos anotaciones de lifetime.

Los patrones programados en el análisis de referencias de Rust se llaman _reglas de elisión de lifetimes_. Estas no son reglas para que los programadores las sigan; son un conjunto de casos particulares que el compilador considerará, y si su código se ajusta a estos casos, no necesitas escribir los lifetimes explícitamente.

Las reglas de elisión no proporcionan una inferencia completa. Si Rust aplica determinísticamente las reglas pero todavía hay ambigüedad sobre qué lifetimes tienen las referencias, el compilador no adivinará cuál debería ser el lifetime de las referencias restantes. En lugar de adivinar, el compilador te dará un error que puedes resolver agregando las anotaciones de lifetime.

Los lifetimes en los parámetros de función o método se llaman _lifetimes de entrada_, y los lifetimes en los valores de retorno se llaman _lifetimes de salida_.

El compilador utiliza tres reglas para determinar los lifetimes de las referencias cuando no hay anotaciones explícitas. La primera regla se aplica a los lifetimes de entrada, y las segundas y terceras reglas se aplican a los lifetimes de salida. Si el compilador llega al final de las tres reglas y todavía hay referencias para las que no puede determinar los lifetimes, el compilador se detendrá con un error. Estas reglas se aplican a las definiciones de `fn` así como a los bloques `impl`.

La primera regla es que el compilador asigna un parámetro de lifetime a cada parámetro que es una referencia. En otras palabras, una función con un parámetro obtiene un parámetro de lifetime: `fn foo<'a>(x: &'a i32)`; una función con dos parámetros obtiene dos parámetros de lifetime separados: `fn foo<'a, 'b>(x: &'a i32, y: &'b i32)`; y así sucesivamente.

La segunda regla es que, si hay exactamente un parámetro de lifetime de entrada, ese lifetime se asigna a todos los parámetros de lifetime de salida: `fn foo<'a>(x: &'a i32) -> &'a i32`.

La tercera regla es que, si hay múltiples parámetros de lifetime de entrada, pero uno de ellos es `&self` o `&mut self` porque se trata de un método, el lifetime de `self` se asigna a todos los parámetros de lifetime de salida. Esta tercera regla hace que los métodos sean mucho más fáciles de leer y escribir porque se necesitan menos símbolos.

Vamos a pretender que somos el compilador. Aplicaremos estas reglas para determinar los lifetimes de las referencias en la firma de la función `first_word` de la Lista 10-25. La firma comienza sin ningún lifetime asociado a las referencias:

```rust
fn first_word(s: &str) -> &str {
```

Luego el compilador aplica la primera regla, que especifica que cada parámetro obtiene su propio lifetime. Lo llamaremos `'a` como de costumbre, así que ahora la firma es esta:

```rust
fn first_word<'a>(s: &'a str) -> &str {
```

La segunda regla se aplica porque hay exactamente un lifetime de entrada. La segunda regla especifica que el lifetime del único parámetro de entrada se asigna al lifetime de salida, así que ahora la firma es esta:

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Ahora todas las referencias en esta firma de función tienen lifetimes, y el compilador puede continuar su análisis sin necesidad de que el programador anote los lifetimes en esta firma de función.

Veamos otro ejemplo, esta vez usando la función `longest` que no tenía parámetros de lifetime cuando comenzamos a trabajar con ella en la Lista 10-20:

```rust
fn longest(x: &str, y: &str) -> &str {
```

Aplicemos la primera regla: cada parámetro obtiene su propio lifetime. Esta vez tenemos dos parámetros en lugar de uno, así que tenemos dos lifetimes:

```rust
fn longest<'a, 'b>(x: &'a str, y: &'b str) -> &str {
```

Puedes ver que la segunda regla no se aplica porque hay más de un lifetime de entrada. La tercera regla tampoco se aplica, porque `longest` es una función en lugar de un método, por lo que ninguno de los parámetros es `self`. Después de trabajar a través de las tres reglas, todavía no hemos determinado cuál es el lifetime del tipo de retorno. Esta es la razón por la que obtuvimos un error al intentar compilar el código de la Lista 10-20: el compilador trabajó a través de las reglas de elisión de lifetimes pero todavía no pudo determinar todos los lifetimes de las referencias en la firma.

Debido a que la tercera regla realmente solo se aplica en firmas de métodos, veremos los lifetimes en ese contexto a continuación para ver por qué la tercera regla significa que no tenemos que anotar los lifetimes en las firmas de métodos muy a menudo.
