# Squiggle Link Hover Effect

`index.html` and `style.css` have already been provided in the VM.

To create a squiggle effect when hovering over a link, you can follow these steps:

1. Create a repeating background for the link using a `linear-gradient`.

```css
a.squiggle {
  background: linear-gradient(to bottom, #0087ca 0%, #0087ca 100%);
  background-position: 0 100%;
  background-repeat: repeat-x;
  background-size: 2px 2px;
  color: inherit;
  text-decoration: none;
}
```

2. Create a `:hover` state for the link with a `background-image` of a data URL containing an SVG with a squiggly path and an animation.

```css
a.squiggle:hover {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 4'%3E%3Cstyle type='text/css'%3E.squiggle{animation:shift .3s linear infinite;}@keyframes shift {from {transform:translateX(0);}to {transform:translateX(-15px);}}%3C/style%3E%3Cpath fill='none' stroke='%230087ca' stroke-width='2' class='squiggle' d='M0,3.5 c 5,0,5,-3,10,-3 s 5,3,10,3 c 5,0,5,-3,10,-3 s 5,3,10,3'/%3E%3C/svg%3E");
  background-size: auto 4px;
}
```

3. Use the HTML code below to add the link to the page.

```html
<p>
  The <a class="squiggle" href="#">magnificent octopus</a> swam along
  gracefully.
</p>
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
