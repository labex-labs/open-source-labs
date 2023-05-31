# Detecting Device Type with JavaScript

To detect whether a device is a mobile device or a desktop, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the JavaScript function `detectDeviceType()` which tests the `Navigator.userAgent` property against a regular expression.
3. The function will return either 'Mobile' or 'Desktop'.

Here's an example code snippet:

```js
const detectDeviceType = () =>
  /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
    navigator.userAgent
  )
    ? "Mobile"
    : "Desktop";

detectDeviceType(); // 'Mobile' or 'Desktop'
```

By using this function, you can determine whether your web page is being viewed on a mobile device or a desktop.
