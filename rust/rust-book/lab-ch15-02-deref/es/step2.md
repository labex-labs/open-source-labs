# Siguiendo el Puntero Hasta el Valor

Una referencia normal es un tipo de puntero, y una forma de pensar en un puntero es como una flecha hacia un valor almacenado en otro lugar. En la Lista 15-6, creamos una referencia a un valor `i32` y luego usamos el operador de dereferencia para seguir la referencia hasta el valor.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
  1 let x = 5;
  2 let y = &x;

  3 assert_eq!(5, x);
  4 assert_eq!(5, *y);
}
```

Lista 15-6: Usando el operador de dereferencia para seguir una referencia a un valor `i32`

La variable `x` contiene un valor `i32` de `5` [1]. Establecemos `y` igual a una referencia a `x` [2]. Podemos afirmar que `x` es igual a `5` [3]. Sin embargo, si queremos hacer una afirmación sobre el valor en `y`, tenemos que usar `*y` para seguir la referencia hasta el valor a que apunta (de ahí el nombre _dereferencia_) para que el compilador pueda comparar el valor real [4]. Una vez que desreferenciamos `y`, tenemos acceso al valor entero al que `y` apunta que podemos comparar con `5`.

Si intentáramos escribir `assert_eq!(5, y);` en su lugar, obtendríamos este error de compilación:

```bash
error[E0277]: no se puede comparar `{entero}` con `&{entero}`
 --> src/main.rs:6:5
  |
6 |     assert_eq!(5, y);
  |     ^^^^^^^^^^^^^^^^ no implementación para `{entero} ==
&{entero}`
  |
  = ayuda: la característica `PartialEq<&{entero}>` no está implementada
para `{entero}`
```

No se permite comparar un número y una referencia a un número porque son tipos diferentes. Debemos usar el operador de dereferencia para seguir la referencia hasta el valor a que apunta.
