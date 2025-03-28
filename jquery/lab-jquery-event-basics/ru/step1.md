# Настройка реакций на события для DOM-элементов

> В ВМ уже предоставлен `index.html`.

jQuery делает простым настройку реакций на события для элементов страницы. Эти события часто вызываются взаимодействием конечного пользователя с страницей, например, когда в элемент формы вводится текст или перемещается указатель мыши. В некоторых случаях, таких как события загрузки и выгрузки страницы, событие вызывает сама браузер.

jQuery предлагает удобные методы для большинства событий браузера. Эти методы — включая `.click()`, `.focus()`, `.blur()`, `.change()` и др. — являются сокращением для метода `.on()` jQuery. Метод on полезен для связывания одной и той же функции обработчика с несколькими событиями, когда вы хотите передать данные в обработчик события, когда работаете с пользовательскими событиями или когда хотите передать объект с несколькими событиями и обработчиками.

```js
// Настройка события с использованием удобного метода
$("p").click(function () {
  console.log("You clicked a paragraph!");
});
```

```js
// Эквивалентная настройка события с использованием метода `.on()`
$("p").on("click", function () {
  console.log("click");
});
```

> Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
