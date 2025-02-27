# Agregando Metadatos a una Nueva Caja

Digamos que tienes una caja que quieres publicar. Antes de publicar, necesitarás agregar algunos metadatos en la sección `[package]` del archivo `Cargo.toml` de la caja.

Tu caja necesitará un nombre único. Mientras estás trabajando en una caja localmente, puedes nombrar la caja como quieras. Sin embargo, los nombres de las cajas en *https://crates.io* se asignan en un primer llegado, primer servido. Una vez que se ha tomado un nombre de caja, nadie más puede publicar una caja con ese nombre. Antes de intentar publicar una caja, busca el nombre que quieres usar. Si el nombre ya ha sido utilizado, necesitarás encontrar otro nombre y editar el campo `name` en el archivo `Cargo.toml` en la sección `[package]` para usar el nuevo nombre para la publicación, como se muestra a continuación:

Nombre del archivo: `Cargo.toml`

```tomlrust
[package]
name = "guessing_game"
```

Incluso si has elegido un nombre único, cuando ejecutes `cargo publish` para publicar la caja en este momento, recibirás una advertencia y luego un error:

```bash
$ cargo publish
    Updating crates.io index
warning: manifest has no description, license, license-file, documentation,
homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata
for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields:
description, license. Please see https://doc.rust-
lang.org/cargo/reference/manifest.html for how to upload metadata
```

Esto resulta en un error porque te falta información crucial: se requiere una descripción y una licencia para que las personas sepan lo que hace tu caja y bajo qué términos pueden usarla. En `Cargo.toml`, agrega una descripción que sea de una o dos frases, porque aparecerá con tu caja en los resultados de búsqueda. Para el campo `license`, necesitas dar un _valor de identificador de licencia_. El Software Package Data Exchange (SPDX) de The Linux Foundation en *http://spdx.org/licenses* lista los identificadores que puedes usar para este valor. Por ejemplo, para especificar que has licenciado tu caja con la Licencia MIT, agrega el identificador `MIT`:

Nombre del archivo: `Cargo.toml`

```toml
[package]
name = "guessing_game"
license = "MIT"
```

Si quieres usar una licencia que no aparece en el SPDX, debes colocar el texto de esa licencia en un archivo, incluir el archivo en tu proyecto y luego usar `license-file` para especificar el nombre de ese archivo en lugar de usar la clave `license`.

La guía sobre qué licencia es adecuada para tu proyecto está fuera del alcance de este libro. Muchas personas en la comunidad de Rust licencian sus proyectos de la misma manera que Rust, utilizando una doble licencia de `MIT OR Apache-2.0`. Esta práctica demuestra que también puedes especificar múltiples identificadores de licencia separados por `OR` para tener múltiples licencias para tu proyecto.

Con un nombre único, la versión, tu descripción y una licencia agregadas, el archivo `Cargo.toml` de un proyecto listo para publicar podría verse así:

Nombre del archivo: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"
description = "A fun game where you guess what number the
computer has chosen."
license = "MIT OR Apache-2.0"

[dependencies]
```

La documentación de Cargo en *https://doc.rust-lang.org/cargo* describe otros metadatos que puedes especificar para garantizar que los demás puedan descubrir y usar tu caja más fácilmente.
