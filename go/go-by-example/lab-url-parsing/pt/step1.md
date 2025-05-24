# Análise de URLs (URL Parsing)

O laboratório requer a análise de uma URL de exemplo que inclui um esquema (scheme), informações de autenticação, host, porta, caminho (path), parâmetros de consulta (query params) e fragmento de consulta (query fragment). A URL analisada deve ser usada para extrair os componentes individuais da URL.

- Os pacotes `url` e `net` devem ser importados.
- A URL de exemplo deve ser analisada e verificada quanto a erros.
- O esquema, informações de autenticação, host, porta, caminho, parâmetros de consulta e fragmento de consulta devem ser extraídos da URL analisada.
- A função `SplitHostPort` deve ser usada para extrair o nome do host e a porta do campo `Host`.
- A função `ParseQuery` deve ser usada para analisar os parâmetros de consulta em um mapa.

```sh
# Executar nosso programa de análise de URL mostra todas as diferentes
# partes que extraímos.
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

A seguir, o código completo:

```go
// URLs fornecem uma [maneira uniforme de localizar recursos](https://adam.herokuapp.com/past/2010/3/30/urls_are_the_uniform_way_to_locate_resources/).
// Veja como analisar URLs em Go.

package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {

	// Vamos analisar esta URL de exemplo, que inclui um
	// esquema, informações de autenticação, host, porta, caminho,
	// parâmetros de consulta e fragmento de consulta.
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	// Analise a URL e certifique-se de que não há erros.
	u, err := url.Parse(s)
	if err != nil {
		panic(err)
	}

	// Acessar o esquema é simples.
	fmt.Println(u.Scheme)

	// `User` contém todas as informações de autenticação; chame
	// `Username` e `Password` para obter valores individuais.
	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	// O `Host` contém tanto o nome do host quanto a porta,
	// se presentes. Use `SplitHostPort` para extraí-los.
	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println(host)
	fmt.Println(port)

	// Aqui extraímos o `path` e o fragmento após o `#`.
	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	// Para obter parâmetros de consulta no formato `k=v`,
	// use `RawQuery`. Você também pode analisar os parâmetros de consulta
	// em um mapa. Os mapas de parâmetros de consulta analisados são de
	// strings para fatias de strings, então indexe em `[0]`
	// se você quiser apenas o primeiro valor.
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}

```
