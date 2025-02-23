# Загрузчик с эффектом импульса

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать анимацию загрузчика с эффектом импульса с использованием свойства `animation-delay`, следуйте шагам:

1. Используйте `@keyframes` для определения анимации для двух элементов `<div>`. Установите начальную точку (`0%`) для обоих элементов так, чтобы они не имели `width` или `height` и располагались по центру. Для конечной точки (`100%`) сделайте так, чтобы оба элемента увеличивались по `width` и `height`, но сбросьте их `position` до `0`.
2. Используйте `opacity` для перехода от `1` до `0` при анимации, чтобы элементы `<div>` имели эффект исчезновения при расширении.
3. Установите заранее определенные `width` и `height` для родительского контейнера `.ripple-loader`. Используйте `position: relative`, чтобы расположить его дочерние элементы.
4. Используйте `animation-delay` для второго элемента `<div>`, чтобы каждый элемент начинал свою анимацию в разное время.

Вот HTML и CSS код, чтобы это достичь:

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
