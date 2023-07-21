# Introduction

In this lab, we will learn how to create a custom React Hook called `useOnWindowResize` that will execute a callback whenever the window is resized. We will use the `useRef()` and `useEffect()` hooks to listen to the `'resize'` event of the `Window` global object and clean up when the component unmounts. This Hook can be useful for creating responsive web applications that need to adjust to different screen sizes.
