# 交替文本

虚拟机中已经提供了`index.html`和`style.css`。

要创建交替文本动画，请执行以下步骤：

1. 创建一个`<span>`元素，其类名为“alternating”，`id`为“alternating - text”，用于容纳要交替显示的文本：

```html
<p>
  I love coding in <span class="alternating" id="alternating - text"></span>.
</p>
```

2. 在CSS中，定义一个名为“alternating - text”的动画，通过设置`display: none`使`<span>`元素消失：

```css
.alternating {
  animation - name: alternating - text;
  animation - duration: 3s;
  animation - iteration - count: infinite;
  animation - timing - function: ease;
}

@keyframes alternating - text {
  90% {
    display: none;
  }
}
```

3. 在JavaScript中，定义一个包含要交替显示的不同单词的数组，并使用第一个单词初始化`<span>`元素的内容：

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating - text");

let i = 0;
element.innerHTML = texts[0];
```

4. 使用`EventTarget.addEventListener()`为`'animationiteration'`事件定义一个事件监听器。每当动画的一次迭代完成时，这将运行事件处理程序。在事件处理程序中，使用`Element.innerHTML`将`texts`数组中的下一个元素显示为`<span>`元素的内容：

```js
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener("animationiteration", listener, false);
```

请点击右下角的“Go Live”以在端口8080上运行Web服务。然后，你可以刷新**Web 8080**标签页来预览网页。
