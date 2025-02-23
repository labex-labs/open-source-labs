# Análisis de URLs

El desafío consiste en analizar una URL de ejemplo que incluye un esquema, información de autenticación, host, puerto, ruta, parámetros de consulta y fragmento de consulta. La URL analizada se debe utilizar para extraer los componentes individuales de la URL.

## Requisitos

- Se deben importar los paquetes `url` y `net`.
- La URL de ejemplo debe ser analizada y se deben comprobar errores.
- El esquema, la información de autenticación, el host, el puerto, la ruta, los parámetros de consulta y el fragmento de consulta deben ser extraídos de la URL analizada.
- La función `SplitHostPort` debe ser utilizada para extraer el nombre de host y el puerto del campo `Host`.
- La función `ParseQuery` debe ser utilizada para analizar los parámetros de consulta en un mapa.

## Ejemplo

```sh
# Ejecutar nuestro programa de análisis de URLs muestra todos los diferentes
# componentes que extrajimos.
$ go run url-parsing.go
postgres
user:pass
user
pass
host.com:5432
host.com
5432
/path
f
k=v
map[k:[v]]
v

```
