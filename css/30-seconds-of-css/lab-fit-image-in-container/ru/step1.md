# Подгонка изображения под контейнер

В ВМ уже предоставлены `index.html` и `style.css`.

Для того чтобы подогнать изображение внутри своего контейнера, сохраняя при этом его соотношение сторон, вы можете использовать `object-fit: contain`. Для того чтобы заполнить контейнер изображением, сохраняя при этом его соотношение сторон, используйте `object-fit: cover`. Если вы хотите расположить изображение по центру контейнера, вы можете использовать `object-position: center`.

Вот пример того, как вы можете использовать эти свойства:

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

И соответствующий CSS:

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
