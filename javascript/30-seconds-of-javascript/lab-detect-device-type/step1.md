# Detect Device Type

> To start practicing coding, open the Terminal/SSH and type `node`.

Detects whether the page is being viewed on a mobile device or a desktop.

- Use a regular expression to test the `Navigator.userAgent` property to figure out if the device is a mobile device or a desktop.

```js
const detectDeviceType = () =>
  /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
    navigator.userAgent
  )
    ? 'Mobile'
    : 'Desktop';
```

```js
detectDeviceType(); // 'Mobile' or 'Desktop'
```
