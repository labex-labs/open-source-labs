# Star Rating

> `index.html` and `script.js` have already been provided in the VM.. In general, you only need to add code to `script.js` and `style.css`.

Create a `Star` component that renders each individual star with the appropriate appearance based on the parent component's state. Then, define a `StarRating` component that uses the `useState()` hook to define the `rating` and `selection` state variables with the appropriate initial values.

In `StarRating`, create a method named `hoverOver` that updates `selection` according to the provided `event`. If `event` is not provided or it is `null`, reset `selection` to `0`. Use the `.data-star-id` attribute of the event's target to determine the value of `selection`.

Next, create an array of 5 elements using `Array.from()` and create individual `<Star>` components using `Array.prototype.map()`. Handle the `onMouseOver` and `onMouseLeave` events of the wrapping element using `hoverOver`. Handle the `onClick` event using `setRating`.

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

Finally, render the `StarRating` component with an initial value of `2` by calling `ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);`.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
