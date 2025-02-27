# Desestimando Versiones de Crates.io con cargo yank

Aunque no puedes eliminar versiones anteriores de una caja, puedes evitar que futuros proyectos la agreguen como una nueva dependencia. Esto es útil cuando una versión de una caja está rota por una u otra razón. En tales situaciones, Cargo admite desestimar una versión de una caja.

_Desestimar_ una versión impide que nuevos proyectos dependan de esa versión mientras permite que todos los proyectos existentes que dependen de ella continúen. Esencialmente, un desestimado significa que todos los proyectos con un _Cargo.lock_ no se romperán y cualquier archivo _Cargo.lock_ generado en el futuro no usará la versión desestimada.

Para desestimar una versión de una caja, en el directorio de la caja que has publicado previamente, ejecuta `cargo yank` y especifica qué versión quieres desestimar. Por ejemplo, si hemos publicado una caja llamada `guessing_game` versión 1.0.1 y queremos desestimarla, en el directorio del proyecto de `guessing_game` ejecutaríamos:

```bash
$ cargo yank --vers 1.0.1
Updating crates.io index
Yank guessing_game@1.0.1
```

Al agregar `--undo` al comando, también puedes deshacer un desestimado y permitir que los proyectos vuelvan a depender de una versión:

```bash
$ cargo yank --vers 1.0.1 --undo
Updating crates.io index
Unyank guessing_game@1.0.1
```

Un desestimado _no_ elimina ningún código. No puede, por ejemplo, eliminar secretos cargados accidentalmente. Si eso sucede, debes restablecer esos secretos inmediatamente.
