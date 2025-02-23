# Pile de police système

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour obtenir une sensation d'application native, utilisez la police native du système d'exploitation. Définissez une liste de polices à l'aide de `font-family`. Le navigateur recherche chaque police successivement, privilégiant la première si possible, et passant à la suivante s'il ne peut pas trouver la police (sur le système ou définie en CSS). Utilisez `-apple-system` pour San Francisco sur iOS et macOS (pas Chrome), et `BlinkMacSystemFont` pour San Francisco sur macOS Chrome. Pour Windows 10, utilisez `'Segoe UI'`, pour Android utilisez `Roboto`, pour Linux avec KDE utilisez `Oxygen-Sans`, pour Ubuntu (toutes les variantes) utilisez `Ubuntu`, et pour Linux avec GNOME Shell utilisez `Cantarell`. Pour macOS 10.10 et inférieur, utilisez `'Helvetica Neue'` et `Helvetica`. Pour une police sans-serif de repli largement prise en charge par tous les systèmes d'exploitation, utilisez `Arial`. Pour appliquer la police système à un texte spécifique, utilisez le HTML et le CSS suivants :

```html
<p class="system-font-stack">Ce texte utilise la police système.</p>
```

```css
.system-font-stack {
  font-family:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu,
    Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
