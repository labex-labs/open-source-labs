# 轮播

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

这段代码渲染了一个轮播组件。其步骤如下：

1. 它使用 `useState()` 钩子创建 `active` 状态变量，并将其初始化为 `0`（轮播中第一个项目的索引）。
2. 它使用 `useEffect()` 钩子通过 `setTimeout()` 设置一个定时器。当定时器触发时，它将 `active` 的值更新为轮播中下一个项目的索引（必要时使用取模运算符循环到开头）。当组件卸载时，它还会清除定时器。
3. 它通过遍历每个轮播项目来计算 `className`，并根据项目当前是否处于活动状态应用相应的类。
4. 它使用 `React.cloneElement()` 渲染轮播项目，通过 `...rest` 传递任何其他属性，并为每个项目添加计算出的 `className`。

CSS 样式定义了轮播及其项目的布局。轮播容器具有 `position: relative`，而项目默认具有 `position: absolute` 和 `visibility: hidden`。当一个项目处于活动状态时，它会获得一个 `visible` 类，该类将其 `visibility` 设置为 `visible`。

```css
.carousel {
  position: relative;
}

.carousel-item {
  position: absolute;
  visibility: hidden;
}

.carousel-item.visible {
  visibility: visible;
}
```

以下是完整代码：

```jsx
const Carousel = ({ carouselItems, ...rest }) => {
  const [active, setActive] = React.useState(0);
  let scrollInterval = null;

  React.useEffect(() => {
    scrollInterval = setTimeout(() => {
      setActive((active + 1) % carouselItems.length);
    }, 2000);
    return () => clearTimeout(scrollInterval);
  });

  return (
    <div className="carousel">
      {carouselItems.map((item, index) => {
        const activeClass = active === index ? " visible" : "";
        return React.cloneElement(item, {
          ...rest,
          className: `carousel-item${activeClass}`
        });
      })}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <Carousel
    carouselItems={[
      <div>carousel item 1</div>,
      <div>carousel item 2</div>,
      <div>carousel item 3</div>
    ]}
  />
);
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
