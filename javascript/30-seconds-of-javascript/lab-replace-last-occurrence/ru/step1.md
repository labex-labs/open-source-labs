# Понимание проблемы и настройка окружения

Прежде чем мы начнем писать код, давайте разберемся, что должна делать наша функция `replaceLast`:

1. Принимать три параметра:

   - `str`: Входная строка, которую нужно изменить
   - `pattern`: Подстрока или регулярное выражение, которое нужно найти
   - `replacement`: Строка, на которую нужно заменить последнее вхождение

2. Возвращать новую строку с замененным последним вхождением шаблона.

Давайте создадим файл JavaScript для реализации нашей функции:

1. Перейдите в директорию проекта в проводнике файлов WebIDE.
2. Создайте новый файл с именем `replaceLast.js` в директории `replace-last`.
3. Добавьте в файл следующую базовую структуру:

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

Чтобы убедиться, что все настроено правильно, давайте добавим простой тест:

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

Теперь давайте запустим наш код, чтобы увидеть текущий вывод:

1. Откройте Терминал в WebIDE.
2. Перейдите в директорию `replace-last`:
   ```bash
   cd ~/project/replace-last
   ```
3. Запустите файл JavaScript с помощью Node.js:
   ```bash
   node replaceLast.js
   ```

В выводе вы должны увидеть `Hello world world`, потому что наша функция в настоящее время просто возвращает исходную строку без каких-либо изменений.
