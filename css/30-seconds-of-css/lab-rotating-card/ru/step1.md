# Вращательная карточка

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания двухсторонней карточки, которая вращается при наведении курсора, следуйте шагам:

1. Установите `backface-visibility` для карточек в `none`, чтобы предотвратить видимость задней стороны по умолчанию.
2. Сначала установите `rotateY(-180deg)` для задней стороны карточки и `rotateY(0deg)` для передней стороны карточки.
3. При наведении курсора установите `rotateY(180deg)` для передней стороны карточки и `rotateY(0deg)` для задней стороны карточки.
4. Установите соответствующее значение `perspective`, чтобы создать эффект вращения.

Вот пример кода HTML и CSS:

```html
<div class="card">
  <div class="card-side front">
    <div>Передняя сторона</div>
  </div>
  <div class="card-side back">
    <div>Задняя сторона</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover.card-side.front {
  transform: rotateY(180deg);
}

.card:hover.card-side.back {
  transform: rotateY(0deg);
}
```

Пожалуйста, нажмите на кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
