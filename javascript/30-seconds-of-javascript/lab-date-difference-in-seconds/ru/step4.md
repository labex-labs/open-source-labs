# Создание практического приложения

Теперь, когда у нас есть работающая функция для вычисления разницы между датами в секундах, давайте создадим более практическое приложение. Мы построим простой таймер, который будет вычислять, сколько времени прошло с момента его запуска.

## Создание приложения - таймера

Создайте новый файл с именем `timer.js` в WebIDE:

1. Нажмите на иконку "Explorer" в левой боковой панели.
2. Щелкните правой кнопкой мыши в проводнике файлов и выберите "New File".
3. Назовите файл `timer.js` и нажмите Enter.
4. Добавьте следующий код в файл:

```javascript
// Функция для вычисления разницы между двумя датами в секундах
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Время начала - когда скрипт начинает выполняться
const startTime = new Date();
console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);

// Функция для обновления и отображения прошедшего времени
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // Форматируем время в формате часы:минуты:секунды
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes
    .toString()
    .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // Очищаем консоль и отображаем обновленное время
  console.clear();
  console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);
  console.log(`Elapsed time: ${formattedTime}`);
}

// Обновляем таймер каждую секунду
console.log("Timer is running... Press Ctrl+C to stop.");
const timerInterval = setInterval(updateTimer, 1000);

// Останавливаем скрипт через 1 минуту
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nTimer stopped after 1 minute.");
}, 60000); // Запускаем на 1 минуту
```

Сохраните файл, нажав Ctrl+S или выбрав File > Save.

## Запуск приложения - таймера

Для запуска приложения - таймера используйте следующую команду в терминале:

```bash
node timer.js
```

Таймер запустится и будет обновляться каждую секунду, показывая, сколько времени прошло с момента его запуска. Таймер автоматически остановится через 1 минуту, или вы можете остановить его раньше, нажав Ctrl+C.

## Понимание работы приложения - таймера

Давайте разберем, как работает приложение - таймер:

1. Мы определяем функцию `getSecondsDiffBetweenDates` для вычисления разницы во времени в секундах.
2. Мы фиксируем время начала, когда скрипт начинает выполняться.
3. Мы определяем функцию `updateTimer`, которая:
   - Получает текущее время.
   - Вычисляет, сколько секунд прошло с момента начала.
   - Форматирует прошедшее время в формате часы:минуты:секунды.
   - Отображает отформатированное время.
4. Мы используем `setInterval` для запуска функции `updateTimer` каждые 1000 миллисекунд (1 секунда).
5. Мы используем `setTimeout` для остановки таймера через 60000 миллисекунд (1 минута).

Это приложение демонстрирует практическое применение нашей функции для вычисления разницы между датами для создания реального - времени таймера.
