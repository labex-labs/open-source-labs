# Análisis de URLs

El laboratorio requiere analizar una URL de ejemplo que incluye un esquema, información de autenticación, host, puerto, ruta, parámetros de consulta y fragmento de consulta. La URL analizada se debe utilizar para extraer los componentes individuales de la URL.

- Se deben importar los paquetes `url` y `net`.
- La URL de ejemplo se debe analizar y comprobar si hay errores.
- El esquema, la información de autenticación, el host, el puerto, la ruta, los parámetros de consulta y el fragmento de consulta se deben extraer de la URL analizada.
- La función `SplitHostPort` se debe utilizar para extraer el nombre de host y el puerto del campo `Host`.
- La función `ParseQuery` se debe utilizar para analizar los parámetros de consulta en un mapa.

```sh
# Ejecutar nuestro programa de análisis de URLs muestra todos los
# diferentes componentes que extrajimos.
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

A continuación está el código completo:

```go
// Las URLs proporcionan una [forma uniforme de localizar recursos](https://adam.herokuapp.com/past/2010/3/30/urls_are_the_uniform_way_to_locate_resources/).
// Aquí está cómo analizar URLs en Go.

package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {

	// Analizaremos esta URL de ejemplo, que incluye un
	// esquema, información de autenticación, host, puerto,
	// ruta, parámetros de consulta y fragmento de consulta.
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	// Analiza la URL y asegúrate de que no haya errores.
	u, err := url.Parse(s)
	if err!= nil {
		panic(err)
	}

	// Acceder al esquema es sencillo.
	fmt.Println(u.Scheme)

	// `User` contiene toda la información de autenticación; llama
	// a `Username` y `Password` en esto para obtener los valores individuales.
	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	// El `Host` contiene tanto el nombre de host como el puerto,
	// si está presente. Utiliza `SplitHostPort` para extraerlos.
	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println(host)
	fmt.Println(port)

	// Aquí extraemos la `ruta` y el fragmento después del `#`.
	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	// Para obtener los parámetros de consulta en un formato de `k=v` de cadena,
	// utiliza `RawQuery`. También puedes analizar los parámetros de consulta
	// en un mapa. Los mapas de parámetros de consulta analizados son de
	// cadenas a slices de cadenas, por lo que indice en `[0]` si solo
	// quieres el primer valor.
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}

```
