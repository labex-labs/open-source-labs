# Codificación Base64

Se te pide escribir un programa en Golang que codifique y decodifique una cadena dada utilizando tanto la codificación base64 estándar como la compatible con URL.

## Requisitos

- El programa debe importar el paquete `encoding/base64` con el nombre `b64` en lugar del nombre predeterminado `base64`.
- El programa debe codificar la cadena dada utilizando tanto la codificación base64 estándar como la compatible con URL.
- El programa debe decodificar la cadena codificada utilizando tanto la decodificación base64 estándar como la compatible con URL.
- El programa debe imprimir las cadenas codificadas y decodificadas en la consola.

## Ejemplo

```sh
# La cadena se codifica en valores ligeramente diferentes con los
# codificadores base64 estándar y de URL (el `+` final vs `-`)
# pero ambas se decodifican a la cadena original como se desea.
$ go run base64-encoding.go
YWJjMTIzIT8kKiYoKSctPUB+
abc123!?$*&()'-=@~

YWJjMTIzIT8kKiYoKSctPUB-
abc123!?$*&()'-=@~

```
