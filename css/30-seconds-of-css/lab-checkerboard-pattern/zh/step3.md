# 创建第一个渐变

现在我们将开始使用 CSS 渐变来创建棋盘图案。让我们添加第一个线性渐变，以创建图案的一部分。

## 了解 CSS 线性渐变

CSS 线性渐变允许你在一条直线上创建两种或多种颜色之间的平滑过渡。`linear-gradient()` 函数接受一个角度和一系列颜色停止点作为参数。我们将使用这种技术来创建棋盘方块。

请按照以下步骤操作：

1. 打开 `style.css` 文件。

2. 让我们修改 `.checkerboard` 类，以包含第一个线性渐变：

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
  );
  background-size: 60px 60px;
}
```

让我解释一下这个渐变的作用：

- `45deg` 指定了渐变的角度
- `#000 25%` 在可用空间的 0% 到 25% 范围内创建黑色
- `transparent 25%` 从 25% 处开始创建透明颜色
- `transparent 75%` 保持透明颜色直到 75%
- `#000 75%` 在 75% 处过渡回黑色，并延续到末尾
- `background-size: 60px 60px` 设置每个重复渐变单元的大小

3. 保存 `style.css` 文件。

4. 刷新 **Web 8080** 标签页以查看更改。

此时你应该会看到一个图案开始形成，但它还不是一个完整的棋盘。第一个渐变只创建了图案的一部分。在下一步中，我们将添加第二个渐变来完成整个棋盘。
