# Системный шрифтовой стек

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания ощущения нативного приложения используйте шрифт операционной системы. Определите список шрифтов с использованием `font-family`. Браузер ищет каждый следующий шрифт, предпочитая первый, если это возможно, и переходит к следующему, если не может найти шрифт (на системе или определенный в CSS). Используйте `-apple-system` для San Francisco на iOS и macOS (не для Chrome), и `BlinkMacSystemFont` для San Francisco на macOS Chrome. Для Windows 10 используйте `'Segoe UI'`, для Android используйте `Roboto`, для Linux с KDE используйте `Oxygen-Sans`, для Ubuntu (все варианты) используйте `Ubuntu`, а для Linux с GNOME Shell используйте `Cantarell`. Для macOS 10.10 и ниже используйте `'Helvetica Neue'` и `Helvetica`. Для резервного безсерифийного шрифта, который широко поддерживается всеми операционными системами, используйте `Arial`. Чтобы применить системный шрифт к определенному тексту, используйте следующий HTML и CSS:

```html
<p class="system-font-stack">This text uses the system font.</p>
```

```css
.system-font-stack {
  font-family:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu,
    Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
