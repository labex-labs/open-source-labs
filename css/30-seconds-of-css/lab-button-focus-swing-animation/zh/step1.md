# 按钮摆动动画

虚拟机中已提供了`index.html`和`style.css`。

要在按钮获得焦点时创建摆动动画，你应该使用适当的`transition`来为元素的变化设置动画。然后，将`:focus`伪类应用于该元素，并使用带有`transform`的`animation`使其摆动。最后，添加`animation-iteration-count`以使动画仅播放一次。以下是在 HTML 和 CSS 中实现此操作的示例：

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
