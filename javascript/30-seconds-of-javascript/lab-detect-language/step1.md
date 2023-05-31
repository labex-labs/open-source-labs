# Revised Detect Language Function

The following code detects the preferred language of the current user. It uses `Navigator.language` or the first value of `Navigator.languages` if available. If neither are available, it returns the `defaultLang` value, which is set to `'en-US'` by default.

```js
const detectLanguage = (defaultLang = "en-US") =>
  navigator.language ||
  (Array.isArray(navigator.languages) && navigator.languages[0]) ||
  defaultLang;
```

To use the function, open the Terminal/SSH and type `node`. Then, run `detectLanguage()`. This will return the preferred language code of the current user. For example, `detectLanguage()` may return `'nl-NL'`.
