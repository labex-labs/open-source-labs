# Фокус внутри

В ВМ уже предоставлены `index.html` и `style.css`.

Для изменения внешнего вида формы, когда какой-либо из ее дочерних элементов имеет фокус, используйте псевдо-класс `:focus-within` для применения стилей к родительскому элементу. Например, в данном HTML-коде, если какой-либо из полей ввода имеет фокус, элемент `form` будет иметь зеленый фон. Для применения стилей к дочерним элементам используйте соответствующие селекторы CSS, такие как `label` и `input`.

```html
<form>
  <label for="username">Username:</label>
  <input id="username" type="text" />
  <br />
  <label for="password">Password:</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
