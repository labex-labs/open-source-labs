# Приведение первой буквы каждого слова к верхнему регистру

Теперь, когда мы можем разделить строку на слова, нам нужно сделать первую букву каждого слова заглавной, а остальные - строчными. Реализуем эту функциональность.

1. В вашей сессии Node.js напишем функцию для приведения первой буквы одного слова к верхнему регистру. Введите:

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Test with a few examples
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

Вывод должен быть следующим:

```
Hello
World
Javascript
```

2. Теперь применим эту функцию к массиву слов с использованием метода `map()`. Введите:

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

Вывод должен быть следующим:

```
[ 'Hello', 'World', 'Javascript' ]
```

Метод `map()` создает новый массив, применяя функцию к каждому элементу исходного массива. В данном случае мы применяем нашу функцию `capitalizeWord` к каждому слову.

3. Наконец, объединим слова с заглавной буквой в строку в формате Pascal case (паскаль-кейс):

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

Вывод должен быть следующим:

```
HelloWorldJavascript
```

Метод `join("")` объединяет все элементы массива в одну строку, используя указанный разделитель (в данном случае пустую строку) между каждым элементом.

Эти шаги демонстрируют основной процесс преобразования строки в Pascal case:

1. Разделить строку на слова.
2. Привести первую букву каждого слова к верхнему регистру.
3. Объединить слова без каких-либо разделителей.
