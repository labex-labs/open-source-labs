# Initialize the Database File

Now that we have registered the `init_db()` function with the app, we can use the `flask` command to initialize the database file.

```shell
$ flask --app flaskr init-db
Initialized the database.
```

This command will create a `flaskr.sqlite` file in the `instance` folder of your project.
