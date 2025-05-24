# System Font Stack

`index.html` and `style.css` have already been provided in the VM.

To achieve a native app feel, use the native font of the operating system. Define a list of fonts using `font-family`. The browser looks for each successive font, preferring the first one if possible, and falls back to the next if it cannot find the font (on the system or defined in CSS). Use `-apple-system` for San Francisco on iOS and macOS (not Chrome), and `BlinkMacSystemFont` for San Francisco on macOS Chrome. For Windows 10, use `'Segoe UI'`, for Android use `Roboto`, for Linux with KDE use `Oxygen-Sans`, for Ubuntu (all variants) use `Ubuntu`, and for Linux with GNOME Shell use `Cantarell`. For macOS 10.10 and below, use `'Helvetica Neue'` and `Helvetica`. For a fallback sans serif font that is widely supported by all operating systems, use `Arial`. To apply the system font to a specific text, use the following HTML and CSS:

```html
<p class="system-font-stack">This text uses the system font.</p>
```

```css
.system-font-stack {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial,
    sans-serif;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
