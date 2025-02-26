# Juego del Dinosaurio

Para comenzar, abre el editor. Puedes ver los siguientes archivos desde tu editor.

```txt
├── public
├── src
│   ├──components
│   │  └── Dino
│   │       ├── img
│   │       │   ├── cactus.png
│   │       │   └── trex.png
│   │       ├── Dino.css
│   │       └── Dino.js
│   ├── App.js
│   ├── App.css
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Requisitos

- Para instalar las dependencias del proyecto, utiliza el siguiente comando:

  ```bash
  npm i
  ```

- Completa este desafío en el archivo `src/components/Dino/Dino.js`.
- Inicializa dos hooks `useRef`: `dinoRef` y `cactusRef`. Estos hooks se utilizarán para referenciar los elementos DOM del dinosaurio y el cactus.
- Inicializa un hook `useState` llamado score con un valor inicial de 0. Este hook llevará un registro de la puntuación del jugador.
- Define la función jump. Agrega la clase "jump" al elemento DOM del dinosaurio referenciado por dinoRef. Esto desencadena una animación CSS que hace que el dinosaurio salte. Después de un tiempo de espera de 300 milisegundos, la clase "jump" se elimina, volviendo al dinosaurio a su posición original.
- Utiliza el hook `useEffect` para manejar la lógica del juego. Establece un intervalo que se ejecuta cada 10 milisegundos. Dentro de la función de intervalo, obtiene la posición actual del dinosaurio (dinoTop) y del cactus (cactusLeft) utilizando la función getComputedStyle.
- Verifica si se ha producido una colisión comparando la posición del cactus (cactusLeft) con la del dinosaurio (dinoTop). Si el cactus está dentro de un cierto rango y a la misma altura que el dinosaurio, se detecta una colisión. En este caso, se muestra una alerta con la puntuación del jugador y la puntuación se reinicia a 0 utilizando la función setScore. De lo contrario, la puntuación se incrementa en 1 utilizando setScore.
- El primer hook `useEffect` también devuelve una función de limpieza que cancela el intervalo cuando el componente se desmonta. Esto garantiza que el intervalo se limpie correctamente para evitar fugas de memoria.
- El segundo hook `useEffect` es responsable de establecer y eliminar un controlador de eventos para el evento "keydown". Cuando se presiona una tecla, se llama a la función jump. Esto permite que el jugador haga saltar al dinosaurio presionando cualquier tecla.

## Ejemplo

Una vez que hayas terminado el código, ejecútalo con el siguiente comando:

```bash
npm start
```

El resultado final es el siguiente:

![Resultado final del juego del Dinosaurio](../assets/finished.gif)
