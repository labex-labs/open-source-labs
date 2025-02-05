# 星级评分

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

创建一个 `Star` 组件，根据父组件的状态以适当的外观渲染每颗单独的星星。然后，定义一个 `StarRating` 组件，它使用 `useState()` 钩子来定义具有适当初始值的 `rating` 和 `selection` 状态变量。

在 `StarRating` 中，创建一个名为 `hoverOver` 的方法，该方法根据提供的 `event` 更新 `selection`。如果未提供 `event` 或其值为 `null`，则将 `selection` 重置为 `0`。使用事件目标的 `.data-star-id` 属性来确定 `selection` 的值。

接下来，使用 `Array.from()` 创建一个包含 5 个元素的数组，并使用 `Array.prototype.map()` 创建单独的 `<Star>` 组件。使用 `hoverOver` 处理包装元素的 `onMouseOver` 和 `onMouseLeave` 事件。使用 `setRating` 处理 `onClick` 事件。

```css
.star {
  color: #ff9933;
  cursor: pointer;
}
```

```jsx
const Star = ({ marked, starId }) => {
  return (
    <span data-star-id={starId} className="star" role="button">
      {marked ? "\u2605" : "\u2606"}
    </span>
  );
};

const StarRating = ({ value }) => {
  const [rating, setRating] = React.useState(parseInt(value) || 0);
  const [selection, setSelection] = React.useState(0);

  const hoverOver = (event) => {
    let val = 0;
    if (event && event.target && event.target.getAttribute("data-star-id"))
      val = event.target.getAttribute("data-star-id");
    setSelection(val);
  };

  return (
    <div
      onMouseLeave={() => hoverOver(null)}
      onMouseOver={hoverOver}
      onClick={(e) =>
        setRating(e.target.getAttribute("data-star-id") || rating)
      }
    >
      {Array.from({ length: 5 }, (v, i) => (
        <Star
          starId={i + 1}
          key={`star_${i + 1}`}
          marked={selection ? selection >= i + 1 : rating >= i + 1}
        />
      ))}
    </div>
  );
};
```

最后，通过调用 `ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);` 来渲染初始值为 `2` 的 `StarRating` 组件。

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
