# Pruebas con diferentes tipos de cadenas

Exploremos cómo diferentes tipos de caracteres afectan el tamaño en bytes de una cadena.

En la consola de Node.js, probemos nuestra función `byteSize` con varias cadenas:

1. Texto en inglés sencillo:

```javascript
byteSize("The quick brown fox jumps over the lazy dog");
```

Salida esperada:

```
43
```

2. Números y caracteres especiales:

```javascript
byteSize("123!@#$%^&*()");
```

Salida esperada:

```
13
```

3. Una mezcla de caracteres ASCII y no ASCII:

```javascript
byteSize("Hello, 世界!");
```

Salida esperada:

```
13
```

4. Varios emojis:

```javascript
byteSize("😀😃😄😁");
```

Salida esperada:

```
16
```

Note que con los tipos de caracteres mixtos, especialmente con caracteres no ASCII como los caracteres chinos y los emojis, el tamaño en bytes es mayor que la cantidad de caracteres.

Esto es importante de entender cuando se trabaja con datos que pueden contener caracteres internacionales o símbolos especiales, ya que afecta los requisitos de almacenamiento y los tamaños de transferencia de datos.

Salga de la consola de Node.js escribiendo:

```javascript
.exit
```

Esto lo devolverá al indicador de terminal normal.
