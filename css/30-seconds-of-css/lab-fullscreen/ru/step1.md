# Полноэкранный режим

В ВМ уже предоставлены `index.html` и `style.css`.

Для стилизации элемента в полноэкранном режиме можно использовать псевдоэлементный селектор CSS `:fullscreen`. Также можно создать кнопку, которая переводит элемент в полноэкранный режим для целей предварительного просмотра, используя `<button>` и `Element.requestFullscreen()`. Вот пример кода:

```html
<div class="container">
  <p>
    <em
      >Нажмите кнопку ниже, чтобы перевести элемент в полноэкранный режим.
    </em>
  </p>
  <div class="element" id="element">
    <p>Меняю цвет в полноэкранном режиме!</p>
  </div>
  <br />
  <button
    onclick="var el = document.getElementById('element'); el.requestFullscreen();"
  >
    Перейти в полноэкранный режим!
  </button>
</div>
```

```css
.container {
  margin: 40px auto;
  max-width: 700px;
}

.element {
  padding: 20px;
  height: 300px;
  width: 100%;
  background-color: skyblue;
  box-sizing: border-box;
}

.element p {
  text-align: center;
  color: white;
  font-size: 3em;
}

/* Для Internet Explorer */
.element:-ms-fullscreen p {
  visibility: visible;
}

/* Для современных браузеров */
.element:fullscreen {
  background-color: #e4708a;
  width: 100vw;
  height: 100vh;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб-страницу.
