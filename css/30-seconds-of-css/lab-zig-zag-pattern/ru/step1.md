# Зигзагообразный фон

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания зигзагообразного фона используйте следующие шаги:

1. Задайте белый фон с использованием `background-color`.
2. Создайте части зигзагообразного узора с использованием `background-image` с четырьмя значениями `linear-gradient()`.
3. Укажите размер узора с использованием `background-size`.
4. Разместите части узора в правильных местах с использованием `background-position`.
5. Чтобы повторять узор, используйте `background-repeat`.
6. **Примечание:** `height` и `width` элемента фиксированы только для целей демонстрации.

Вот пример кода:

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%), linear-gradient(
      315deg,
      #000 25%,
      transparent 25%
    ), linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
