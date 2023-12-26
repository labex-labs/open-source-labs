# Drag Drop

To get started, open the editor. You can see the following files from your editor.

```txt
├── public
├── src
│   ├── App.js
│   ├── App.css
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

- Please complete this challenge in the `App.js` file.
- The `onDragStart` function is defined. It is an event handler for the dragstart event on a task card. It sets the data transfer data to the task's name property, which will be used to identify the task when it's dropped.
- The `onDrop` function is defined. It is an event handler for the drop event on the task board. It retrieves the task's name from the data transfer data, updates the category of the task in the tasks state based on the drop location (cat), and sets the updated tasks state using setTasks.

## Example

Once you have completed the code, run it with the following command: 

```bash
npm start
```

The finished result is as follows:

![finished](./assets/finished.gif)
