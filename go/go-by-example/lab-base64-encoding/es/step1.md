# Codificación Base64

Se te pide escribir un programa en Golang que codifique y decodifique una cadena dada utilizando tanto la codificación base64 estándar como la compatible con URL.

- El programa debe importar el paquete `encoding/base64` con el nombre `b64` en lugar del nombre predeterminado `base64`.
- El programa debe codificar la cadena dada utilizando tanto la codificación base64 estándar como la compatible con URL.
- El programa debe decodificar la cadena codificada utilizando tanto la decodificación base64 estándar como la compatible con URL.
- El programa debe imprimir las cadenas codificadas y decodificadas en la consola.

```sh
# La cadena se codifica en valores ligeramente diferentes con los
# codificadores base64 estándar y de URL (el `+` final vs `-`)
# pero ambas se decodifican a la cadena original como se desea.
```

A continuación está el código completo:

```go
// Go proporciona soporte integrado para la [codificación/decodificación base64
// ](https://en.wikipedia.org/wiki/Base64).

package main

// Esta sintaxis importa el paquete `encoding/base64` con
// el nombre `b64` en lugar del nombre predeterminado `base64`. Ahorrará
// un poco de espacio más adelante.
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// Aquí está la `string` que codificaremos/decodificaremos.
	data := "abc123!?$*&()'-=@~"

	// Go admite tanto la codificación base64 estándar como la compatible con URL.
	// Aquí está cómo codificar utilizando el codificador estándar. El codificador
	// requiere un `[]byte` por lo que convertimos nuestra `string` a ese tipo.
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// La decodificación puede devolver un error, que puedes comprobar
	// si no sabes de antemano que la entrada sea bien formada.
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// Esto codifica/decodifica utilizando un formato base64 compatible con URL.
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}

```
