# Шаблон фона в стиле «пузырьки»

В виртуальной машине уже предоставлены файлы `index.html` и `style.css`.

Для создания фона в стиле «пузырьки» вы можете выполнить следующие шаги:

1. Установите свойство `background-color` в черный цвет.
2. Используйте свойство `background-image` с двумя значениями `radial-gradient()`, чтобы создать два кружка.
3. Укажите размер шаблона с помощью свойства `background-size`. Используйте `background-position` для правильного расположения двух градиентов.
4. Установите `background-repeat` в значение `repeat`.
5. Обратите внимание, что фиксированная `height` и `width` элемента используются только для демонстрации.

Вот пример HTML - кода для элемента div с классом `polka-dot`:

```html
<div class="polka-dot"></div>
```

А вот соответствующий CSS - код:

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image:
    radial-gradient(#fff 10%, transparent 11%),
    radial-gradient(#fff 10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб - сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб - страницу.
