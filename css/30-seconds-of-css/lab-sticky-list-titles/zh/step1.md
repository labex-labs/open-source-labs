# 带有粘性部分标题的列表

虚拟机中已经提供了 `index.html` 和 `style.css`。

要为每个部分创建带有粘性标题的列表，请执行以下步骤：

1. 通过使用 `overflow-y: auto` 使列表容器（`<dl>`）垂直溢出。
2. 通过将标题（`<dt>`）的 `position` 设置为 `sticky` 并应用 `top: 0`，将其粘贴到容器顶部。
3. 使用以下 HTML 和 CSS 代码：

HTML：

```html
<div class="container">
  <dl class="sticky-stack">
    <dt>A</dt>
    <dd>阿尔及利亚</dd>
    <dd>安哥拉</dd>

    <dt>B</dt>
    <dd>贝宁</dd>
    <dd>博茨瓦纳</dd>
    <dd>布基纳法索</dd>
    <dd>布隆迪</dd>

    <dt>C</dt>
    <dd>佛得角</dd>
    <dd>喀麦隆</dd>
    <dd>中非共和国</dd>
    <dd>乍得</dd>
    <dd>科摩罗</dd>
    <dd>刚果民主共和国</dd>
    <dd>刚果共和国</dd>
    <dd>科特迪瓦</dd>

    <dt>D</dt>
    <dd>吉布提</dd>

    <dt>E</dt>
    <dd>埃及</dd>
    <dd>赤道几内亚</dd>
    <dd>厄立特里亚</dd>
    <dd>斯威士兰（原称斯威士兰）</dd>
    <dd>埃塞俄比亚</dd>
  </dl>
</div>
```

CSS：

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.sticky-stack {
  background: #37474f;
  color: #fff;
  margin: 0;
  height: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.sticky-stack dt {
  position: sticky;
  top: 0;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  padding: 0.25rem 1rem;
}

.sticky-stack dd {
  margin: 0;
  padding: 0.75rem 1rem;
}

.sticky-stack dd + dt {
  margin-top: 1rem;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
