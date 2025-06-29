# 应用动画

既然我们已经定义了关键帧，接下来需要将动画应用到我们的方块元素上。

1. 再次打开 `style.css` 文件，并按如下方式修改 `.zoom-in-out-box` 选择器：

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}
```

2. 让我们来理解一下我们添加的 `animation` 属性：
   - `animation` 是一个简写属性，可一次性设置多个动画属性
   - `zoom-in-zoom-out` 是我们关键帧动画的名称
   - `1s` 指定动画的一个周期持续 1 秒
   - `ease` 是一个计时函数，它使动画开始时较慢，然后加速，最后再减慢
   - `infinite` 表示动画将无限循环

3. 完成这些更改后，保存 `style.css` 文件。

4. 如果 Web 服务器已经在运行，只需刷新 **Web 8080** 标签页。如果没有运行，点击右下角的“Go Live”启动服务器，然后打开 **Web 8080** 标签页。

现在你应该能看到你的粉色方块在持续的动画中平稳地放大和缩小。方块会逐渐变大，直到达到其原始大小的 1.5 倍，然后再缩小回正常大小。这个循环会无限重复。
