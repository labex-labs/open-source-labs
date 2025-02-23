# Análisis de números

Analizar números a partir de cadenas es una tarea común en muchos programas. Este desafío te pide que uses el paquete integrado `strconv` para analizar diferentes tipos de números a partir de cadenas.

## Requisitos

- Utiliza el paquete `strconv` para analizar números a partir de cadenas.
- Analiza un número de punto flotante con `ParseFloat`.
- Analiza un entero con `ParseInt`.
- Analiza un número con formato hexadecimal con `ParseInt`.
- Analiza un entero sin signo con `ParseUint`.
- Analiza un entero en base 10 con `Atoi`.
- Maneja los errores devueltos por las funciones de análisis.

## Ejemplo

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: parsing "wat": sintaxis no válida

# A continuación, veremos otra tarea de análisis común: URLs.
```
