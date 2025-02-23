# Fonction pour ajouter des minutes à une date

Pour ajouter un nombre spécifique de minutes à une date donnée, utilisez la fonction suivante :

```js
const addMinutesToDate = (date, n) => {
  // Crée un objet Date à partir de la date donnée
  const d = new Date(date);
  // Ajoute n minutes à l'objet Date
  d.setTime(d.getTime() + n * 60000);
  // Retourne une représentation sous forme de chaîne de la nouvelle date au format yyyy-mm-dd HH:MM:SS
  return d.toISOString().split(".")[0].replace("T", " ");
};
```

Pour utiliser cette fonction, passez une représentation sous forme de chaîne de la date en tant que premier argument et le nombre de minutes à ajouter (ou soustraire, si négatif) en tant que second argument. Par exemple :

```js
addMinutesToDate("2020-10-19 12:00:00", 10); // '2020-10-19 12:10:00'
addMinutesToDate("2020-10-19", -10); // '2020-10-18 23:50:00'
```

Notez que la fonction retourne la nouvelle date sous forme d'une chaîne au format `yyyy-mm-dd HH:MM:SS`.
