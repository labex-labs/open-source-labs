# 尝试不同的动画属性

让我们通过尝试不同的动画属性来定制我们的动画。这将帮助你理解这些属性是如何影响动画行为的。

1. 打开 `style.css` 文件，并修改 `.zoom-in-out-box` 选择器，尝试不同的动画属性：

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 2s ease-in-out infinite;
  /* Add a slight rotation during the animation */
  border-radius: 10px;
}
```

2. 让我们来理解一下我们做了哪些更改：
   - 我们将动画持续时间延长到了 `2s`（2 秒）
   - 我们将计时函数改为 `ease-in-out`，这使得动画的开始和结束都更加平滑
   - 我们添加了一个 10px 的 `border-radius`，使方块的角变成圆角

3. 我们还可以修改关键帧来添加旋转效果：

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1) rotate(0deg);
  }
  50% {
    transform: scale(1.5, 1.5) rotate(45deg);
    background-color: #2196f3;
  }
  100% {
    transform: scale(1, 1) rotate(0deg);
  }
}
```

4. 在这个更新后的关键帧定义中：
   - 我们在 `transform` 属性中添加了 `rotate()` 函数
   - 在 50% 的进度时，元素在放大的同时旋转 45 度
   - 我们还在 50% 的进度时将背景颜色改为蓝色

5. 完成这些更改后，保存 `style.css` 文件。

6. 刷新 **Web 8080** 标签页，查看增强后的动画效果。

现在你的动画应该变慢了（每个周期 2 秒），方块有圆角，在缩放的同时会旋转，并且在动画进行到一半时会改变颜色。这展示了 CSS 动画如何结合多个属性的变化来实现丰富的视觉效果。

你可以自由地进一步尝试不同的属性和值，看看它们会如何影响你的动画。
