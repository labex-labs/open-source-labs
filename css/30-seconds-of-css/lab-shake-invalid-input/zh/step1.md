# 无效输入时抖动

虚拟机中已提供了`index.html`和`style.css`。

要在输入无效时创建抖动动画，请执行以下步骤：

1. 使用`pattern`属性定义一个正则表达式，指定允许的输入。例如，使用`[A-Za-z]*`仅允许字母。
2. 使用`@keyframes`定义一个抖动动画。设置`margin-left`属性以使输入左右移动。
3. 使用`:invalid`伪类将抖动动画应用于输入。
4. 可选地，为输入添加红色阴影以指示错误。

以下是一个示例代码片段：

```html
<input type="text" placeholder="Letters only" pattern="[A-Za-z]*" />
```

```css
@keyframes shake {
  0% {
    margin-left: 0rem;
  }
  25% {
    margin-left: 0.5rem;
  }
  75% {
    margin-left: -0.5rem;
  }
  100% {
    margin-left: 0rem;
  }
}

input:invalid {
  animation: shake 0.2s ease-in-out 0s 2;
  box-shadow: 0 0 0.6rem #ff0000;
}
```

请点击右下角的“Go Live”以在端口8080上运行Web服务。然后，你可以刷新**Web 8080**标签页来预览网页。
