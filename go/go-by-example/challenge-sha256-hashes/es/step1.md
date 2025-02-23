# Hash SHA256

Dada una cadena, calcule su hash SHA256.

## Requisitos

- El programa debe importar los paquetes `crypto/sha256` y `fmt`.
- El programa debe utilizar la función `sha256.New()` para crear un nuevo hash.
- El programa debe utilizar la función `Write` para escribir los bytes de la cadena en el hash.
- El programa debe utilizar la función `Sum` para obtener el resultado final del hash como una porción de bytes.
- El programa debe imprimir la cadena original y el resultado del hash en formato hexadecimal.

## Ejemplo

```sh
# Ejecutar el programa calcula el hash y lo imprime en
# un formato hexadecimal legible para humanos.
$ go run sha256-hashes.go
sha256 esta cadena
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# Puedes calcular otros hashes utilizando un patrón similar al
# mostrado anteriormente. Por ejemplo, para calcular
# hashes SHA512 importa `crypto/sha512` y utiliza
# `sha512.New()`.

# Tenga en cuenta que si necesita hashes criptográficamente seguros,
# debe investigar detenidamente
# [la fuerza del hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```
