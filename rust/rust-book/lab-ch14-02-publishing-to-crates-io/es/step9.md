# Publicando en Crates.io

Ahora que has creado una cuenta, guardado tu token de API, elegido un nombre para tu caja y especificado los metadatos requeridos, ¡estás listo para publicar! Publicar una caja sube una versión específica a *https://crates.io* para que otros la usen.

Ten cuidado, porque una publicación es _permanente_. La versión nunca puede ser sobrescrita y el código no puede ser eliminado. Un objetivo principal de Crates.io es actuar como un archivo permanente de código para que las compilaciones de todos los proyectos que dependen de cajas de *https://crates.io* continúen funcionando. Permitir la eliminación de versiones haría imposible cumplir ese objetivo. Sin embargo, no hay límite al número de versiones de caja que puedes publicar.

Ejecuta nuevamente el comando `cargo publish`. Ahora debería tener éxito:

```bash
$ cargo publish
    Updating crates.io index
   Packaging guessing_game v0.1.0 (file:///projects/guessing_game)
   Verifying guessing_game v0.1.0 (file:///projects/guessing_game)
   Compiling guessing_game v0.1.0
(file:///projects/guessing_game/target/package/guessing_game-0.1.0)
    Finished dev [unoptimized + debuginfo] target(s) in 0.19s
   Uploading guessing_game v0.1.0 (file:///projects/guessing_game)
```

¡Felicidades! Ahora has compartido tu código con la comunidad de Rust y cualquiera puede agregar fácilmente tu caja como dependencia de su proyecto.
