# Declaraciones `let`

Antes de este capítulo, solo habíamos discutido explícitamente el uso de patrones con `match` e `if let`, pero de hecho, también los hemos usado en otros lugares, incluyendo en declaraciones `let`. Por ejemplo, considere esta asignación de variable directa con `let`:

```rust
let x = 5;
```

Cada vez que ha usado una declaración `let` como esta, ha estado usando patrones, aunque puede que no lo haya notado. Más formalmente, una declaración `let` se ve así:

```rust
let PATRÓN = EXPRESIÓN;
```

En declaraciones como `let x = 5;` con un nombre de variable en el slot del patrón, el nombre de variable es solo una forma particularmente simple de un patrón. Rust compara la expresión con el patrón y asigna cualquier nombre que encuentre. Entonces, en el ejemplo `let x = 5;`, `x` es un patrón que significa "asigna lo que coincide aquí a la variable `x`". Debido a que el nombre `x` es todo el patrón, este patrón efectivamente significa "asigna todo a la variable `x`, cualquiera que sea el valor".

Para ver más claramente el aspecto de coincidencia de patrones de `let`, considere el Listado 18-4, que usa un patrón con `let` para desestructurar una tupla.

```rust
let (x, y, z) = (1, 2, 3);
```

Listado 18-4: Usando un patrón para desestructurar una tupla y crear tres variables a la vez

Aquí, hacemos coincidir una tupla con un patrón. Rust compara el valor `(1, 2, 3)` con el patrón `(x, y, z)` y ve que el valor coincide con el patrón, en el sentido de que ve que el número de elementos es el mismo en ambos, por lo que Rust asigna `1` a `x`, `2` a `y` y `3` a `z`. Puede pensar en este patrón de tupla como anidar tres patrones de variable individuales dentro de él.

Si el número de elementos en el patrón no coincide con el número de elementos en la tupla, el tipo general no coincidirá y obtendremos un error del compilador. Por ejemplo, el Listado 18-5 muestra un intento de desestructurar una tupla con tres elementos en dos variables, lo que no funcionará.

```rust
let (x, y) = (1, 2, 3);
```

Listado 18-5: Construyendo incorrectamente un patrón cuyas variables no coinciden con el número de elementos en la tupla

Intentar compilar este código da como resultado este error de tipo:

```bash
error[E0308]: mismatched types
 --> src/main.rs:2:9
  |
2 |     let (x, y) = (1, 2, 3);
  |         ^^^^^^   --------- this expression has type `({integer}, {integer},
{integer})`
  |         |
  |         expected a tuple with 3 elements, found one with 2 elements
  |
  = note: expected tuple `({integer}, {integer}, {integer})`
             found tuple `(_, _)`
```

Para corregir el error, podríamos ignorar uno o más de los valores en la tupla usando `_` o `..`, como verá en "Ignorando valores en un patrón". Si el problema es que tenemos demasiadas variables en el patrón, la solución es hacer que los tipos coincidan eliminando variables para que el número de variables sea igual al número de elementos en la tupla.
