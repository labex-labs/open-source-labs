# Tag Input Field

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To render a tag input field, you can define a `TagInput` component using the `useState()` hook to initialize an array from the `tags` prop. Use `Array.prototype.map()` on the collected nodes to render the list of tags. To add a new tag, define the `addTagData` method, which will be executed when the `Enter` key is pressed. The `addTagData` method calls `setTagData` to add the new tag using the spread (`...`) operator to prepend the existing tags and add the new tag at the end of the `tagData` array. To remove a tag, define the `removeTagData` method, which will be executed on clicking the delete icon in the tag. Use `Array.prototype.filter()` in the `removeTagData` method to remove the tag using its `index` to filter it out from the `tagData` array.

You can style the tag input field using the provided CSS. The `TagInput` component takes a `tags` prop, which is an array of tags to be rendered. To use the component, you can call `ReactDOM.createRoot()` with the `TagInput` component and pass in an array of tags as the `tags` prop.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
