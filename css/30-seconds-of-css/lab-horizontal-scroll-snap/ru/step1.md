# Горизонтальный скроллинг с зацеплением

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать горизонтально прокручиваемый контейнер, который будет зацепляться за элементы при скроллинге, следуйте шагам:

1. Используйте `display: grid` и `grid-auto-flow: column` для создания горизонтального макета.
2. Используйте `scroll-snap-type: x mandatory` и `overscroll-behavior-x: contain` для создания эффекта зацепления при горизонтальном скроллинге.
3. Измените `scroll-snap-align` на `start`, `stop` или `center`, чтобы настроить выравнивание зацепления.

Вот пример HTML и CSS кода, который вы можете использовать:

HTML

```
<div class="horizontal-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640"></a>
</div>
```

CSS

```
.horizontal-snap {
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  height: calc(180px + 1rem);
  padding: 1rem;
  max-width: 480px;
  margin: 0 auto;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
}

.horizontal-snap > a {
  scroll-snap-align: center;
}

.horizontal-snap img {
  width: 180px;
  max-width: none;
  object-fit: contain;
  border-radius: 1rem;
}
```

Пожалуйста, нажмите на кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
