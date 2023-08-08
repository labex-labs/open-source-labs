# Styling Flask Application

## Introduction

In this lab, we will learn how to add CSS to our Flask application to make it visually appealing. We will use static files, specifically a CSS file, to style our application. Static files are files that don't change, such as CSS files, JavaScript files, and images.

## Steps

### Step 1: Create CSS file

First, we need to create a CSS file that will hold our styles. In Flask, static files are stored in a directory named `static`. Let's create a CSS file named `style.css` in the `flaskr/static` directory.

```bash
# Navigate to the static directory
cd flaskr/static

# Create style.css file
touch style.css
```

### Step 2: Add CSS rules

Next, copy the following CSS rules into the `style.css` file. These rules will style various HTML elements in our application.

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
/* More CSS rules... */
```

### Step 3: Link CSS file in HTML

Now, we need to link our CSS file in the HTML templates. Flask automatically adds a `static` view that serves static files. We can use the `url_for` function in the `base.html` template to link our CSS file.

```html+jinja
<!-- base.html -->

{{ url_for('static', filename='style.css') }}
```

### Step 4: Verify the changes

To verify the changes, start your Flask application and navigate to the login page at http://127.0.0.1:5000/auth/login. The page should now be styled according to the rules in the `style.css` file.

## Summary

In this lab, we learned how to add styles to our Flask application using a CSS file. We created a CSS file, added some CSS rules, and then linked the CSS file in our HTML templates using Flask's `url_for` function. Now, our Flask application looks much more visually appealing. Remember, if you make changes to a static file, you may need to refresh the browser page or clear your browser's cache to see the changes.
