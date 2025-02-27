# Temporizador

Para comenzar, abra el editor. Puede ver los siguientes archivos desde su editor.

```txt
├── public
├── src
│   ├── components
│   │   ├──common
│   │   ├── stopwatch
│   │   ├── timer
│   │   ├── App.css
│   │   └── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Requisitos

- Para instalar las dependencias del proyecto, use el siguiente comando:

  ```bash
  npm i
  ```

- Complete este desafío en el archivo `src/components/timer/Timer.js`.
- La función `onStart` es llamada cada segundo por el hook useEffect.
  - Verifica si el temporizador ha llegado a 0 horas, 0 minutos y 0 segundos. Si es así, establece isStarted en falso y devuelve.
  - Si el temporizador no está iniciado, devuelve sin hacer ningún cambio.
  - Si el temporizador está en ejecución, decrementa el temporizador en 1 segundo. -
  - Si los minutos o segundos alcanzan 0, ajusta las horas, minutos o segundos en consecuencia usando la función setTimer.
- La función `onReset` es llamada cuando se hace clic en el botón "Reiniciar".
  - Establece isStarted en falso y reinicia el temporizador a 0 horas, 0 minutos y 0 segundos.

## Ejemplo

Una vez que haya completado el código, ejecútelo con el siguiente comando:

```bash
npm start
```

El resultado final es el siguiente:

![Demostración del temporizador finalizado](../assets/finished.gif)
