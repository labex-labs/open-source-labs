# 添加背景图像

接下来，我们将为图像创建一个子目录。在 `polls/static/polls/` 目录中创建一个 `images` 子目录。在这个目录中，添加任何你想用作背景的图像文件。在本教程中，我们使用的是一个名为 `background.png` 的文件，你可以在虚拟机的 `/tmp/background.png` 目录中找到它。

你需要将 `/tmp/background.png` 复制到 `polls/static/polls/images/background.png`。

然后，在你的样式表（`polls/static/polls/style.css`）中添加对图像的引用：

```css
body {
  background: white url("images/background.png") no-repeat;
}
```

重新加载 **Web 8080** 标签页，你应该会看到背景图像加载在屏幕的左上角。

![背景图像示例](../assets/20230908-15-39-41-8dGms0NM.png)

> `{% static %}` 模板标签不适用于非 Django 生成的静态文件，比如你的样式表。你应该始终使用 **相对路径** 来相互链接你的静态文件，因为这样你就可以更改 `STATIC_URL`（`static` 模板标签用于生成其 URL），而无需同时修改静态文件中的一堆路径。

这些是 **基础知识**。有关该框架中设置和其他部分的更多详细信息，请参阅 `静态文件操作指南 </howto/static-files/index>` 和 `静态文件参考 </ref/contrib/staticfiles>`。`部署静态文件 </howto/static-files/deployment>` 讨论了如何在真实服务器上使用静态文件。

当你熟悉静态文件后，请阅读 **自定义 Django 管理站点** 以了解如何自定义 Django 自动生成的管理站点。
