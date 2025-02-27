# Comentarios de Documentación como Pruebas

Agregar bloques de código de ejemplo en tus comentarios de documentación puede ayudar a demostrar cómo utilizar tu biblioteca, y hacer eso tiene un bono adicional: ejecutar `cargo test` ejecutará los ejemplos de código en tu documentación como pruebas. Nada es mejor que documentación con ejemplos. Pero nada es peor que ejemplos que no funcionan porque el código ha cambiado desde que se escribió la documentación. Si ejecutamos `cargo test` con la documentación de la función `add_one` de la Lista 14-1, veremos una sección en los resultados de las pruebas que se ve así:

```rust
   Doc-tests my_crate

running 1 test
test src/lib.rs - add_one (line 5)... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.27s
```

Ahora, si cambiamos ya sea la función o el ejemplo para que el `assert_eq!` en el ejemplo lance un panic y ejecutamos `cargo test` nuevamente, veremos que las pruebas de documentación detectan que el ejemplo y el código están desincronizados entre sí.
