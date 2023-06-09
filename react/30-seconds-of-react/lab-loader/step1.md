# Spinning Loader

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

**Renders a spinning loader component.**

To render a spinning loader component, follow these steps:

1. Render an SVG element whose dimensions are determined by the `size` prop.
2. Use CSS to animate the SVG, creating a spinning animation. Specifically, add the `.loader` class to the SVG and set the `animation` property to `rotate 2s linear infinite`. Also, define the `rotate` keyframes with a `transform` property that rotates the SVG 360 degrees.
3. Add a `circle` element to the SVG, which represents the spinning circle. To animate the circle, add the `.loader circle` selector and set the `animation` property to `dash 1.5s ease-in-out infinite`. Also, define the `dash` keyframes with `stroke-dasharray` and `stroke-dashoffset` properties that create a dashed stroke pattern that moves around the circle.
4. Finally, create a `Loader` component that renders the SVG with the `size` prop passed in as the width and height attributes.

```css
.loader {
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}

.loader circle {
  animation: dash 1.5s ease-in-out infinite;
}

@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
```

```jsx
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

To use the `Loader` component with a size of 24, call `ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);`.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
