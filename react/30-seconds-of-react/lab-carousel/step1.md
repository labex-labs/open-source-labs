# Carousel

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

Here's the revised content:

---

This code renders a carousel component. Here are the steps it takes:

1. It uses the `useState()` hook to create the `active` state variable and initializes it to `0` (the index of the first item in the carousel).
2. It uses the `useEffect()` hook to set up a timer with `setTimeout()`. When the timer fires, it updates the value of `active` to the index of the next item in the carousel (using the modulo operator to wrap around to the beginning if necessary). It also cleans up the timer when the component unmounts.
3. It computes the `className` for each carousel item by mapping over them and applying the appropriate class based on whether the item is currently active or not.
4. It renders the carousel items using `React.cloneElement()`, passing down any additional props using `...rest`, and adding the computed `className` to each item.

The CSS styles define the layout of the carousel and its items. The carousel container has `position: relative`, while the items have `position: absolute` and `visibility: hidden` by default. When an item is active, it gets a `visible` class, which sets its `visibility` to `visible`.

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

Here's the full code:

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
          className: `carousel-item${activeClass}`,
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
      <div>carousel item 3</div>,
    ]}
  />
);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
