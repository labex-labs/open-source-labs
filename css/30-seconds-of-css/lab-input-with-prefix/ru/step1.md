# Ввод с префиксом

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания ввода с визуальным нередактируемым префиксом следуйте шагам:

1. Используйте `display: flex`, чтобы создать контейнерный элемент с классом `.input-box`.
2. Удалите границу и контур из поля `<input>` и примените их к родительскому элементу вместо этого, чтобы оно выглядело как поле ввода.
3. Используйте псевдо-класс селектор `:focus-within` для стилизации родительского элемента соответственно, когда пользователь взаимодействует с полем `<input>`.

Вот HTML-код:

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

А вот CSS-код:

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box.prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
