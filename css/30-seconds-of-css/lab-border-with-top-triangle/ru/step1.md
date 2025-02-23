# Граница с верхним треугольником

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать контейнер с содержимым с треугольником вверху, следуйте шагам:

1. Используйте псевдо-элементы `::before` и `::after`, чтобы создать два треугольника.
2. Задайте `border-color` и `background-color` треугольников, чтобы они совпадали с контейнером.
3. Задайте `border-width` для треугольника `::before` на `1px` шире, чем для треугольника `::after`, чтобы он служил в качестве границы.
4. Разместите треугольник `::after` на `1px` правее треугольника `::before`, чтобы показалась левая граница.

Вот пример HTML-кода для контейнера:

```html
<div class="container">Border with top triangle</div>
```

И вот соответствующий CSS-код:

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
