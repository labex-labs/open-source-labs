# Creando una aplicación práctica

Ahora que tenemos una función funcional para calcular la diferencia entre fechas en segundos, creemos una aplicación más práctica. Construiremos un temporizador simple que calcule cuánto tiempo ha transcurrido desde que lo iniciamos.

## Creando una aplicación de temporizador

Crea un nuevo archivo llamado `timer.js` en el WebIDE:

1. Haz clic en el icono "Explorer" en la barra lateral izquierda.
2. Haz clic derecho en el explorador de archivos y selecciona "New File".
3. Nombra el archivo `timer.js` y presiona Enter.
4. Agrega el siguiente código al archivo:

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Start time - when the script starts running
const startTime = new Date();
console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);

// Function to update and display the elapsed time
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // Format the time as hours:minutes:seconds
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // Clear the console and display the updated time
  console.clear();
  console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);
  console.log(`Elapsed time: ${formattedTime}`);
}

// Update the timer every second
console.log("Timer is running... Press Ctrl+C to stop.");
const timerInterval = setInterval(updateTimer, 1000);

// Keep the script running
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nTimer stopped after 1 minute.");
}, 60000); // Run for 1 minute
```

Guarda el archivo presionando Ctrl+S o haciendo clic en Archivo > Guardar.

## Ejecutando la aplicación de temporizador

Para ejecutar la aplicación de temporizador, utiliza el siguiente comando en la terminal:

```bash
node timer.js
```

El temporizador se iniciará y se actualizará cada segundo, mostrando cuánto tiempo ha transcurrido desde que se inició. El temporizador se detendrá automáticamente después de 1 minuto, o puedes detenerlo antes presionando Ctrl+C.

## Entendiendo la aplicación de temporizador

Desglosemos cómo funciona la aplicación de temporizador:

1. Definimos la función `getSecondsDiffBetweenDates` para calcular la diferencia de tiempo en segundos.
2. Registramos la hora de inicio cuando el script comienza a ejecutarse.
3. Definimos una función `updateTimer` que:
   - Obtiene la hora actual.
   - Calcula cuántos segundos han transcurrido desde la hora de inicio.
   - Formatea el tiempo transcurrido en horas:minutos:segundos.
   - Muestra el tiempo formateado.
4. Usamos `setInterval` para ejecutar la función `updateTimer` cada 1000 milisegundos (1 segundo).
5. Usamos `setTimeout` para detener el temporizador después de 60000 milisegundos (1 minuto).

Esta aplicación demuestra un uso práctico de nuestra función de diferencia de fechas para crear un temporizador en tiempo real.
