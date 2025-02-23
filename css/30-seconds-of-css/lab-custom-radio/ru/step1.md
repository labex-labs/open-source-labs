# Кастомная радиокнопка

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать стилизованную радиокнопку с анимацией при изменении состояния, следуйте шагам:

1. Создайте `.radio-container`, используя flexbox, чтобы создать соответствующий макет для радиокнопок.
2. Сбросьте стили на элементе `<input>` и используйте его для создания контура и фона радиокнопки.
3. Используйте элемент `::before`, чтобы создать внутреннюю окружность радиокнопки.
4. Создайте эффект анимации при изменении состояния, используя `transform: scale(1)` и CSS-анимацию.

Вот пример HTML-отрывка:

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">Apples</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">Oranges</label>
</div>
```

И вот соответствующий CSS:

```css
.radio-container {
  display: flex;
  align-items: center;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border: 1px solid #cccfdb;
  border-radius: 50%;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: 0.3s transform ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
  margin-right: 6px;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
