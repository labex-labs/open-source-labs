# Counter Game

To get started, open the editor. You can see the following files from your editor.

```txt
├── public
├── src
│   ├── components
│   │  └── HomePage
│   │       ├── HomePage.css
│   │       └── HomePage.js
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Requirements

- To install the project dependencies, use the following command:

  ```bash
  npm i
  ```

- Please complete this challenge in the `components/HomePage/HomePage.js` file.
- Use the `useState` hook to define two state variables: `count` and `timer`.
- Use the `useEffect` hook to start the timer when the timer state variable changes.
- Check the `timer` value. If it is zero, the effect returns early and doesn't do anything.
- If the `timer` value is not zero, it sets up an interval that decrements the `timer` value by 1 every second (1000 milliseconds).
- Return a cleanup function that clears the interval when the component is unmounted or when the timer value changes.

## Example

Once you have completed the code, run it with the following command：

```bash
npm start
```

The finished result is as follows:

![finished](./assets/finished.gif)
