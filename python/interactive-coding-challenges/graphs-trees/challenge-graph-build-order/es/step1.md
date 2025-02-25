# Orden de compilación de gráficas

## Problema

Dada una lista de proyectos y sus dependencias, necesitamos encontrar un orden de compilación válido. Un orden de compilación es una lista de proyectos en la que cada proyecto aparece antes que cualquier proyecto que dependa de él.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- La entrada puede contener un grafo cíclico.
- Podemos suponer que ya tenemos las clases Graph y Node.
- Podemos suponer que el grafo está conectado.
- Podemos suponer que las entradas son válidas.
- Podemos suponer que el problema cabe en la memoria.

## Ejemplo

Supongamos que tenemos los siguientes proyectos y dependencias:

- proyectos: a, b, c, d, e, f, g
- dependencias: (d, g), (f, c), (f, b), (f, a), (c, a), (b, a), (a, e), (b, e)

La salida debe ser: d, f, c, b, g, a, e

Tenga en cuenta que la dirección de la arista es hacia abajo, lo que significa que un proyecto depende de los proyectos debajo de él.

```txt
    f     d
   /|\    |
  c | b   g
   \|/|
    a |
    |/
    e
```

Si la entrada contiene un grafo cíclico, la salida debe ser Ninguno.
