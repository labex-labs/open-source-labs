# Input of Skills

To get started, open the editor. You can see the following files from your editor.

```txt
├── public
├── src
│   ├── components
│   │   └── TagInput.js
│   ├── App.css
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

- Please complete this challenge in the `src/component/TagInput.js` file.
- The `handleAddTag` function is called when a key is pressed in the input field. If the key is not the Enter key, the function returns early and does nothing. Otherwise, it checks the input value and adds it to the tags state if it is not empty and hasn't already been added. Then, it clears the input field.
- The `onDeleteTag` function is called when a tag is clicked. It filters the tags state to remove the clicked tag and updates the state with the filtered tags.

## Example

Once you have completed the code, run it with the following command: 

```bash
npm start
```

The finished result is as follows:

![finished](./assets/finished.gif)
