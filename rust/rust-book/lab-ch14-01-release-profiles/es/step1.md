# Personalizando compilaciones con perfiles de lanzamiento

En Rust, los _perfiles de lanzamiento_ son perfiles predefinidos y personalizables con diferentes configuraciones que permiten a un programador tener más control sobre varias opciones para compilar código. Cada perfil se configura independientemente de los demás.

Cargo tiene dos perfiles principales: el perfil `dev` que Cargo utiliza cuando ejecutas `cargo build`, y el perfil `release` que Cargo utiliza cuando ejecutas `cargo build --release`. El perfil `dev` está definido con valores predeterminados adecuados para el desarrollo, y el perfil `release` tiene valores predeterminados adecuados para las compilaciones de lanzamiento.

Es posible que estos nombres de perfil te resulten familiares a partir de la salida de tus compilaciones:

```bash
$ cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
$ cargo build --release
    Finished release [optimized] target(s) in 0.0s
```

`dev` y `release` son estos diferentes perfiles utilizados por el compilador.

Cargo tiene configuraciones predeterminadas para cada uno de los perfiles que se aplican cuando no has agregado explícitamente ninguna sección `[profile.*]` en el archivo `Cargo.toml` del proyecto. Al agregar secciones `[profile.*]` para cualquier perfil que desees personalizar, reemplazas cualquier subconjunto de las configuraciones predeterminadas. Por ejemplo, aquí son los valores predeterminados para la configuración `opt-level` de los perfiles `dev` y `release`:

Nombre de archivo: `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 0

[profile.release]
opt-level = 3
```

La configuración `opt-level` controla el número de optimizaciones que Rust aplicará a tu código, con un rango de 0 a 3. Aplicar más optimizaciones se extiende el tiempo de compilación, por lo que si estás en desarrollo y compilas tu código con frecuencia, querrás menos optimizaciones para compilar más rápido incluso si el código resultante se ejecuta más lentamente. Por lo tanto, el `opt-level` predeterminado para `dev` es `0`. Cuando estés listo para lanzar tu código, es mejor dedicar más tiempo a la compilación. Solo compilarás una vez en modo de lanzamiento, pero ejecutarás el programa compilado muchas veces, por lo que el modo de lanzamiento intercambia un tiempo de compilación más largo por un código que se ejecuta más rápido. Es por eso que el `opt-level` predeterminado para el perfil `release` es `3`.

Puedes reemplazar una configuración predeterminada agregando un valor diferente para ella en `Cargo.toml`. Por ejemplo, si queremos usar el nivel de optimización 1 en el perfil de desarrollo, podemos agregar estas dos líneas al archivo `Cargo.toml` de nuestro proyecto:

Nombre de archivo: `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 1
```

Este código reemplaza la configuración predeterminada de `0`. Ahora, cuando ejecutamos `cargo build`, Cargo usará los valores predeterminados del perfil `dev` más nuestra personalización de `opt-level`. Debido a que establecimos `opt-level` en `1`, Cargo aplicará más optimizaciones que el predeterminado, pero no tantas como en una compilación de lanzamiento.

Para ver la lista completa de opciones de configuración y valores predeterminados para cada perfil, consulta la documentación de Cargo en *https://doc.rust-lang.org/cargo/reference/profiles.html*.
