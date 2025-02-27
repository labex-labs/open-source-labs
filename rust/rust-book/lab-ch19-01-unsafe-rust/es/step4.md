# Llamar a una función o método inseguro

El segundo tipo de operación que se puede realizar en un bloque `unsafe` es llamar a funciones inseguras. Las funciones y métodos inseguros se ven exactamente como las funciones y métodos regulares, pero tienen una palabra clave `unsafe` adicional antes del resto de la definición. La palabra clave `unsafe` en este contexto indica que la función tiene requisitos que debemos cumplir cuando llamamos a esta función, porque Rust no puede garantizar que hayamos cumplido estos requisitos. Al llamar a una función insegura dentro de un bloque `unsafe`, estamos diciendo que hemos leído la documentación de esta función y que asumimos la responsabilidad de cumplir con los contratos de la función.

Aquí hay una función insegura llamada `dangerous` que no hace nada en su cuerpo:

    unsafe fn dangerous() {}

    unsafe {
        dangerous();
    }

Debemos llamar a la función `dangerous` dentro de un bloque `unsafe` separado. Si intentamos llamar a `dangerous` sin el bloque `unsafe`, obtendremos un error:

```bash
error[E0133]: call to unsafe function is unsafe and requires
unsafe function or block
 --> src/main.rs:4:5
  |
4 |     dangerous();
  |     ^^^^^^^^^^^ call to unsafe function
  |
  = note: consult the function's documentation for information on
how to avoid undefined behavior
```

Con el bloque `unsafe`, estamos afirmando a Rust que hemos leído la documentación de la función, que entendemos cómo usarla correctamente y que hemos verificado que estamos cumpliendo con el contrato de la función.

Los cuerpos de las funciones inseguras son en realidad bloques `unsafe`, por lo que para realizar otras operaciones inseguras dentro de una función insegura, no es necesario agregar otro bloque `unsafe`.
