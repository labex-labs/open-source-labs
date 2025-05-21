# 完成棋盘图案

现在，让我们添加第二个线性渐变，以完成棋盘图案，并使其在整个元素上重复显示。

1. 再次打开 `style.css` 文件。

2. 修改 `.checkerboard` 类，添加第二个线性渐变，以创建交替的图案：

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ), linear-gradient(-45deg, #000 25%, transparent 25%, transparent 75%, #000
        75%, #000);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

我们添加的内容如下：

- 第二个 `linear-gradient()`，它与第一个类似，但角度为 `-45deg`，用于创建交替的图案
- `background-repeat: repeat` 属性确保图案在整个元素上重复显示

这两个不同角度的渐变组合在一起，形成了经典的棋盘图案。第一个渐变创建了一组对角方块，而第二个渐变创建了另一组方块，填补了空白。

3. 保存 `style.css` 文件。

4. 刷新 **Web 8080** 标签页，查看最终结果。

此时，你应该会看到一个完整的棋盘图案，黑白方块交替出现。该图案应在整个 240px×240px 的元素上重复显示。

## 图案的工作原理

棋盘效果的实现方式如下：

1. 使用两个角度相反的线性渐变（45deg 和 -45deg）
2. 每个渐变在角落处创建黑色方块图案
3. 透明区域使白色背景得以显示
4. `background-size` 属性控制图案中每个方块的大小
5. `background-repeat` 属性使图案在整个元素上重复显示

这种技术展示了 CSS 渐变在创建复杂图案时的强大功能，无需使用图像文件，从而加快了加载速度，并提高了可扩展性。
