# Собственная полоса прокрутки

В ВМ уже предоставлены `index.html` и `style.css`.

Для настройки стиля полосы прокрутки для элементов с прокручиваемым переполнением вы можете использовать `::-webkit-scrollbar` для стилизации элемента полосы прокрутки, `::-webkit-scrollbar-track` для стилизации дорожки полосы прокрутки (фон полосы прокрутки) и `::-webkit-scrollbar-thumb` для стилизации ползунка полосы прокрутки (двигаемый элемент). Однако обратите внимание, что этот метод работает только в браузерах на основе WebKit, и стилизация полосы прокрутки не находится на любом стандарте. Вот пример использования этих селекторов в HTML и CSS:

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1e3f20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4a7856;
  border-radius: 12px;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
