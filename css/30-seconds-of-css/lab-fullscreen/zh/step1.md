# 全屏

虚拟机中已经提供了`index.html`和`style.css`。

要对处于全屏模式的元素设置样式，你可以使用`:fullscreen` CSS 伪元素选择器。你还可以创建一个按钮，通过`<button>`和`Element.requestFullscreen()`使元素进入全屏模式以进行预览。以下是一个示例代码：

```html
<div class="container">
  <p>
    <em>点击下方按钮可使元素进入全屏模式。</em>
  </p>
  <div class="element" id="element">
    <p>我在全屏模式下会改变颜色！</p>
  </div>
  <br />
  <button
    onclick="var el = document.getElementById('element'); el.requestFullscreen();"
  >
    进入全屏！
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

/* 针对 Internet Explorer */
.element:-ms-fullscreen p {
  visibility: visible;
}

/* 针对现代浏览器 */
.element:fullscreen {
  background-color: #e4708a;
  width: 100vw;
  height: 100vh;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
