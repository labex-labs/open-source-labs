# Panic

El reto te pide que uses la función `panic` para fallar rápidamente en errores que no deben ocurrir durante la operación normal o que no estás preparado para manejar con gracia.

## Requisitos

- Conocimientos básicos del lenguaje de programación Golang.
- Familiaridad con el manejo de errores en Golang.
- Comprensión de la función `panic` en Golang.

## Ejemplo

```sh
# Ejecutar este programa hará que se produzca un panic, imprima
# un mensaje de error y trazas de gorutinas, y salga con
# un estado no nulo.

# Cuando el primer panic en `main` se activa, el programa sale
# sin llegar al resto del código. Si quieres ver el programa
# intentar crear un archivo temporal, comenta el primer panic.
$ go run panic.go
panic: a problem

goroutine 1 [running]:
main.main() /.../panic.go:12 +0x47
...
exit status 2

# Tenga en cuenta que a diferencia de algunos lenguajes que usan excepciones
# para el manejo de muchos errores, en Go es idiomático
# usar valores de retorno que indiquen errores donde sea posible.
```
