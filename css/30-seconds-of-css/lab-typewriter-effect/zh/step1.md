# 打字机效果

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建打字机效果动画，请按照以下步骤操作：

1. 定义两个动画，`typing` 和 `blink`。`typing` 动画用于字符，`blink` 动画用于光标。
2. 使用 `::after` 伪元素向容器元素添加光标。
3. 使用 JavaScript 设置内部元素的文本，并设置包含字符数的 `--characters` 变量。此变量用于为文本设置动画。
4. 使用 `white-space: nowrap` 和 `overflow: hidden` 使内容在必要时不可见。

以下是 HTML 代码：

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

以下是 CSS 代码：

```css
.typewriter-effect {
  display: flex;
  justify-content: center;
  font-family: monospace;
}

.typewriter-effect > .text {
  max-width: 0;
  animation: typing 3s steps(var(--characters)) infinite;
  white-space: nowrap;
  overflow: hidden;
}

.typewriter-effect::after {
  content: " |";
  animation: blink 1s infinite;
  animation-timing-function: step-end;
}

@keyframes typing {
  75%,
  100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%,
  75%,
  100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

最后，以下是 JavaScript 代码：

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
