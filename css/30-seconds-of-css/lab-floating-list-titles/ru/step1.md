# Список с плавающими заголовками разделов

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания списка с плавающими заголовками для каждого раздела следуйте шагам:

1. Примените `overflow-y: auto` к контейнеру списка, чтобы разрешить вертикальное переполнение.
2. Используйте `display: grid` для внутреннего контейнера (`<dl>`), чтобы создать макет с двумя колонками.
3. Установите заголовки (`<dt>`) в `grid-column: 1`, а содержимое (`<dd>`) в `grid-column: 2`.
4. Наконец, примените `position: sticky` и `top: 0.5rem` к заголовкам, чтобы создать эффект плавающей надписи.

Вот HTML-код:

```html
<div class="container">
  <div class="floating-stack">
    <dl>
      <dt>A</dt>
      <dd>Алжир</dd>
      <dd>Ангола</dd>

      <dt>B</dt>
      <dd>Бенин</dd>
      <dd>Ботсвана</dd>
      <dd>Буркина-Фасо</dd>
      <dd>Бурунди</dd>

      <dt>C</dt>
      <dd>Кабо-Верде</dd>
      <dd>Камерун</dd>
      <dd>Центральноафриканская Республика</dd>
      <dd>Чад</dd>
      <dd>Коморы</dd>
      <dd>Конго, Демократическая Республика</dd>
      <dd>Конго, Республика</dd>
      <dd>Кот-д’Ивуар</dd>

      <dt>D</dt>
      <dd>Джибути</dd>

      <dt>E</dt>
      <dd>Египет</dd>
      <dd>Экваториальная Гвинея</dd>
      <dd>Эритрея</dd>
      <dd>Эсватини (ранее Свазиленд)</dd>
      <dd>Эфиопия</dd>
    </dl>
  </div>
</div>
```

Вот CSS-код:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455a64;
  color: #fff;
  height: 80vh;
  width: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.floating-stack > dl {
  margin: 0 0 1rem;
  display: grid;
  grid-template-columns: 2.5rem 1fr;
  align-items: center;
}

.floating-stack dt {
  position: sticky;
  top: 0.5rem;
  left: 0.5rem;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  padding: 0.25rem 1rem;
  grid-column: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.floating-stack dd {
  grid-column: 2;
  margin: 0;
  padding: 0.75rem;
}

.floating-stack > dl:first-of-type > dd:first-of-type {
  margin-top: 0.25rem;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
