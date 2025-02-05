# 带有浮动章节标题的列表

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个每个章节标题都浮动的列表，请按照以下步骤操作：

1. 对列表容器应用 `overflow-y: auto`，以允许垂直滚动。
2. 在内层容器（`<dl>`）上使用 `display: grid` 创建一个两列布局。
3. 将标题（`<dt>`）设置为 `grid-column: 1`，内容（`<dd>`）设置为 `grid-column: 2`。
4. 最后，对标题应用 `position: sticky` 和 `top: 0.5rem` 以创建浮动效果。

以下是 HTML 代码：

```html
<div class="container">
  <div class="floating-stack">
    <dl>
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
</div>
```

以下是 CSS 代码：

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455a64;
  color: #fff;
  height: 80vh;
  width: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.floating-stack > dl {
  margin: 0 0 1rem;
  display: grid;
  grid-template-columns: 2.5rem 1fr;
  align-items: center;
}

.floating-stack dt {
  position: sticky;
  top: 0.5rem;
  left: 0.5rem;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  padding: 0.25rem 1rem;
  grid-column: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.floating-stack dd {
  grid-column: 2;
  margin: 0;
  padding: 0.75rem;
}

.floating-stack > dl:first-of-type > dd:first-of-type {
  margin-top: 0.25rem;
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
