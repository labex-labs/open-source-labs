# Configurando una Cuenta en Crates.io

Antes de publicar cualquier caja, debes crear una cuenta en *https://crates.io* y obtener un token de API. Para hacer eso, visita la página principal en *https://crates.io* y inicia sesión a través de una cuenta de GitHub. (La cuenta de GitHub es actualmente un requisito, pero en el futuro el sitio puede admitir otros métodos de creación de una cuenta.) Una vez que hayas iniciado sesión, visita tus ajustes de cuenta en *https://crates.io/me* y recupera tu clave API. Luego ejecuta el comando `cargo login` con tu clave API, como se muestra a continuación:

```bash
cargo login abcdefghijklmnopqrstuvwxyz012345
```

Este comando informará a Cargo de tu token de API y lo almacenará localmente en _\~/.cargo/credentials_. Tenga en cuenta que este token es un _secreto_: no lo comparta con nadie más. Si lo comparte con alguien por cualquier motivo, debería revocarlo y generar un nuevo token en *https://crates.io*.
