# 系统字体堆栈

虚拟机中已提供了 `index.html` 和 `style.css`。

为了营造原生应用的感觉，请使用操作系统的原生字体。使用 `font-family` 定义字体列表。浏览器会依次查找每种字体，如果可能的话会优先使用第一种字体，如果找不到该字体（无论是在系统中还是在 CSS 中定义的），则会回退到下一种字体。对于 iOS 和 macOS 上的旧金山字体（不适用于 Chrome），使用 `-apple-system`；对于 macOS Chrome 上的旧金山字体，使用 `BlinkMacSystemFont`。对于 Windows 10，使用 `'Segoe UI'`；对于安卓，使用 `Roboto`；对于使用 KDE 的 Linux，使用 `Oxygen-Sans`；对于所有版本的 Ubuntu，使用 `Ubuntu`；对于使用 GNOME Shell 的 Linux，使用 `Cantarell`。对于 macOS 10.10 及以下版本，使用 `'Helvetica Neue'` 和 `Helvetica`。为了使用一种所有操作系统都广泛支持的备用无衬线字体，请使用 `Arial`。要将系统字体应用于特定文本，请使用以下 HTML 和 CSS：

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

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
