# Compilando para la versión de lanzamiento

Cuando tu proyecto está finalmente listo para ser lanzado, puedes usar `cargo build --release` para compilarlo con optimizaciones.

```bash
cargo build --release
```

Este comando creará un ejecutable en `target/release` en lugar de `target/debug`. Las optimizaciones hacen que tu código de Rust se ejecute más rápido, pero activarlas aumenta el tiempo que tarda en compilarse tu programa. Por eso hay dos perfiles diferentes: uno para el desarrollo, cuando quieres recompilar rápidamente y con frecuencia, y otro para compilar el programa final que darás a un usuario que no se recompilará repetidamente y que se ejecutará lo más rápido posible. Si estás benchmarkeando el tiempo de ejecución de tu código, asegúrate de ejecutar `cargo build --release` y benchmarkear con el ejecutable en `target/release`.
