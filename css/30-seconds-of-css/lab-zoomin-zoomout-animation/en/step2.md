# Basic CSS Styling

Now that we have our HTML structure in place, let's create the basic CSS styling for our animation element.

1. Open the `style.css` file in the editor.

2. If the file is empty or missing, create it with the following content:

```css
body {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
}

.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
}
```

3. Let's understand what this CSS does:
   - We set some basic styling for the page (font, width, and margins)
   - We style the heading with a dark gray color
   - For our animation element `.zoom-in-out-box`, we:
     - Add a margin of 24px around it
     - Set its width and height to 50px
     - Give it a vibrant pink background color

4. Save the `style.css` file after making these changes.

5. To see your progress, click on the "Go Live" button in the bottom right corner of VSCode. This will start a web server on port 8080. Then refresh the **Web 8080** tab to see your styled box.

You should now see a small pink square on your web page. This square is the element we will animate in the next steps.
