# Static Files Lab

## Introduction

In this lab, you will learn how to add style to your Flask application using static files. Static files, such as CSS, JavaScript, and images, are served directly to the client without any modification. By adding CSS to your Flask application, you can enhance the visual appearance of your HTML templates.

## Steps

### Step 1: Create the static directory

1. Create a new directory called `static` in your Flask project directory.
2. Inside the `static` directory, create a new file called `style.css`.

### Step 2: Add CSS styles to `style.css`

1. Open the `style.css` file.
2. Copy and paste the following CSS code into the file:

```css
/* flaskr/static/style.css */

html {
  font-family: sans-serif;
  background: #eee;
  padding: 1rem;
}

body {
  max-width: 960px;
  margin: 0 auto;
  background: white;
}

h1 {
  font-family: serif;
  color: #377ba8;
  margin: 1rem 0;
}

a {
  color: #377ba8;
}

hr {
  border: none;
  border-top: 1px solid lightgray;
}

nav {
  background: lightgray;
  display: flex;
  align-items: center;
  padding: 0 0.5rem;
}

nav h1 {
  flex: auto;
  margin: 0;
}

nav h1 a {
  text-decoration: none;
  padding: 0.25rem 0.5rem;
}

nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

nav ul li a,
nav ul li span,
header .action {
  display: block;
  padding: 0.5rem;
}

.content {
  padding: 0 1rem 1rem;
}

.content > header {
  border-bottom: 1px solid lightgray;
  display: flex;
  align-items: flex-end;
}

.content > header h1 {
  flex: auto;
  margin: 1rem 0 0.25rem 0;
}

.flash {
  margin: 1em 0;
  padding: 1em;
  background: #cae6f6;
  border: 1px solid #377ba8;
}

.post > header {
  display: flex;
  align-items: flex-end;
  font-size: 0.85em;
}

.post > header > div:first-of-type {
  flex: auto;
}

.post > header h1 {
  font-size: 1.5em;
  margin-bottom: 0;
}

.post .about {
  color: slategray;
  font-style: italic;
}

.post .body {
  white-space: pre-line;
}

.content:last-child {
  margin-bottom: 0;
}

.content form {
  margin: 1em 0;
  display: flex;
  flex-direction: column;
}

.content label {
  font-weight: bold;
  margin-bottom: 0.5em;
}

.content input,
.content textarea {
  margin-bottom: 1em;
}

.content textarea {
  min-height: 12em;
  resize: vertical;
}

input.danger {
  color: #cc2f2e;
}

input[type="submit"] {
  align-self: start;
  min-width: 10em;
}
```

### Step 3: Link the CSS file in the base.html template

1. Open the `base.html` file in the `templates` directory.
2. Locate the `<head>` section of the HTML file.
3. Add the following line of code inside the `<head>` section:

```html+jinja
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

### Step 4: Test the CSS styles

1. Start your Flask development server.
2. Open your web browser and navigate to `http://127.0.0.1:5000/auth/login`.
3. The login page should now have the CSS styles applied.

## Summary

In this lab, you learned how to add CSS styles to your Flask application using static files. By creating a `style.css` file in the `static` directory and linking it in your HTML templates, you can enhance the visual appearance of your application.
