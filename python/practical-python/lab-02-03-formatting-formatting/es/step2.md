# Códigos de formato

Los códigos de formato (después del `:` dentro de `{}`) son similares a `printf()` de C. Los códigos comunes incluyen:

```code
d       Entero decimal
b       Entero binario
x       Entero hexadecimal
f       Flotante como [-]m.dddddd
e       Flotante como [-]m.dddddde+-xx
g       Flotante, pero uso selectivo de notación científica
s       Cadena
c       Carácter (desde un entero)
```

Los modificadores comunes ajustan el ancho del campo y la precisión decimal. Esta es una lista parcial:

```code
:>10d   Entero alineado a la derecha en un campo de 10 caracteres
:<10d   Entero alineado a la izquierda en un campo de 10 caracteres
:^10d   Entero centrado en un campo de 10 caracteres
:0.2f   Flotante con precisión de 2 dígitos
```
