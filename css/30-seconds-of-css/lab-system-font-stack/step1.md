# System Font Stack

To achieve a native app feel, the system font stack uses the native font of the operating system. The code can be written in `index.html` and `style.css`. 

The font is defined using `font-family`. The browser looks for each successive font and falls back to the next one if it cannot find the font on the system or defined in CSS. 

The following fonts are used for different operating systems: 
- `-apple-system` and `BlinkMacSystemFont` are San Francisco fonts used on iOS, macOS (Chrome excluded) and macOS Chrome respectively.
- `'Segoe UI'` is used on Windows 10.
- `Roboto` is used on Android.
- `Oxygen-Sans` is used on Linux with KDE.
- `Ubuntu` is used on Ubuntu (all variants).
- `Cantarell` is used on Linux with GNOME Shell.
- `'Helvetica Neue'` and `Helvetica` are used on macOS 10.10 and below.
- `Arial` is a widely supported font.
- `sans-serif` is the fallback sans serif font if none of the other fonts are supported.

Here's an example of how to use the system font stack in HTML and CSS:
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