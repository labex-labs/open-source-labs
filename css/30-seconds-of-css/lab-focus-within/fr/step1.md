# Focus Within

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour modifier l'apparence d'un formulaire lorsque l'un de ses éléments enfants est au focus, utilisez le pseudo-classe `:focus-within` pour appliquer des styles à l'élément parent. Par exemple, dans le code HTML donné, si l'un des champs de saisie est au focus, l'élément `form` aura un fond vert. Pour appliquer des styles aux éléments enfants, utilisez des sélecteurs CSS appropriés tels que `label` et `input`.

```html
<form>
  <label for="username">Nom d'utilisateur:</label>
  <input id="username" type="text" />
  <br />
  <label for="password">Mot de passe:</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
