# Variables y datos interactuando con Move

En Rust, múltiples variables pueden interactuar con los mismos datos de diferentes maneras. Echemos un vistazo a un ejemplo que utiliza un entero en la Lista 4-2.

```rust
let x = 5;
let y = x;
```

Lista 4-2: Asignando el valor entero de la variable `x` a `y`

Probablemente podemos adivinar lo que está sucediendo: "asocia el valor `5` con `x`; luego hace una copia del valor en `x` y lo asocia con `y`". Ahora tenemos dos variables, `x` e `y`, y ambas son iguales a `5`. Esto es lo que realmente está sucediendo, porque los enteros son valores simples con un tamaño conocido y fijo, y estos dos valores `5` se empujan a la pila.

Ahora echemos un vistazo a la versión de `String`:

```rust
let s1 = String::from("hello");
let s2 = s1;
```

Esto parece muy similar, por lo que podríamos suponer que la forma en que funciona sería la misma: es decir, la segunda línea haría una copia del valor en `s1` y lo asociaría con `s2`. Pero esto no es exactamente lo que pasa.

Echa un vistazo a la Figura 4-1 para ver lo que está sucediendo con `String` por debajo de los paneles. Un `String` está compuesto por tres partes, mostradas en la izquierda: un puntero a la memoria que contiene el contenido de la cadena, una longitud y una capacidad. Este grupo de datos se almacena en la pila. En la derecha está la memoria en el montón que contiene el contenido.

Figura 4-1: Representación en memoria de un `String` que contiene el valor `"hello"` asociado a `s1`

La longitud es la cantidad de memoria, en bytes, que el contenido del `String` está utilizando actualmente. La capacidad es la cantidad total de memoria, en bytes, que el `String` ha recibido del asignador. La diferencia entre la longitud y la capacidad es importante, pero no en este contexto, por lo que por ahora está bien ignorar la capacidad.

Cuando asignamos `s1` a `s2`, los datos del `String` se copian, lo que significa que copiamos el puntero, la longitud y la capacidad que están en la pila. No copiamos los datos en el montón a los que apunta el puntero. En otras palabras, la representación de los datos en memoria se ve como en la Figura 4-2.

Figura 4-2: Representación en memoria de la variable `s2` que tiene una copia del puntero, la longitud y la capacidad de `s1`

La representación _no_ se ve como en la Figura 4-3, que es cómo se vería la memoria si Rust en lugar de eso copiara también los datos del montón. Si Rust hiciera esto, la operación `s2 = s1` podría ser muy costosa en términos de rendimiento en tiempo de ejecución si los datos en el montón fueran grandes.

Figura 4-3: Otra posibilidad de lo que podría hacer `s2 = s1` si Rust copiara también los datos del montón

Antes, dijimos que cuando una variable sale del ámbito, Rust llama automáticamente a la función `drop` y libera la memoria del montón para esa variable. Pero la Figura 4-2 muestra ambos punteros de datos apuntando a la misma ubicación. Este es un problema: cuando `s2` y `s1` salen del ámbito, ambos intentarán liberar la misma memoria. Esto se conoce como un error de _doble liberación_ y es uno de los errores de seguridad de memoria que mencionamos anteriormente. Liberar la memoria dos veces puede causar una corrupción de memoria, lo que puede conllevar posibles vulnerabilidades de seguridad.

Para garantizar la seguridad de la memoria, después de la línea `let s2 = s1;`, Rust considera que `s1` ya no es válido. Por lo tanto, Rust no necesita liberar nada cuando `s1` sale del ámbito. Echa un vistazo a lo que sucede cuando intentas usar `s1` después de crear `s2`; no funcionará:

```rust
let s1 = String::from("hello");
let s2 = s1;

println!("{s1}, world!");
```

Obtendrás un error como este porque Rust te impide usar la referencia invalidada:

```bash
error[E0382]: borrow of moved value: `s1`
 --> src/main.rs:5:28
  |
2 |     let s1 = String::from("hello");
  |         -- move occurs because `s1` has type `String`, which
 does not implement the `Copy` trait
3 |     let s2 = s1;
  |              -- value moved here
4 |
5 |     println!("{s1}, world!");
  |                ^^ value borrowed here after move
```

Si has escuchado los términos _copia superficial_ y _copia profunda_ mientras trabajabas con otros lenguajes, el concepto de copiar el puntero, la longitud y la capacidad sin copiar los datos probablemente suene como hacer una copia superficial. Pero debido a que Rust también invalida la primera variable, en lugar de ser llamada una copia superficial, se conoce como un _move_. En este ejemplo, diríamos que `s1` fue _movido_ a `s2`. Entonces, lo que realmente sucede se muestra en la Figura 4-4.

Figura 4-4: Representación en memoria después de que `s1` ha sido invalidado

¡Eso resuelve nuestro problema! Con solo `s2` válido, cuando sale del ámbito solo él liberará la memoria, y ya terminamos.

Además, hay una decisión de diseño que se implica con esto: Rust nunca creará automáticamente "copias profundas" de tus datos. Por lo tanto, se puede asumir que cualquier copia _automática_ será barata en términos de rendimiento en tiempo de ejecución.
