# The development server

Let's verify your Django project works. Change into the outer `mysite` directory, if you haven't already, and run the following commands:

```bash
cd ~/project/mysite
python manage.py runserver
```

You'll see the following output on the command line:

```text
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.

- 15:50:53 Django version , using settings 'mysite.settings' Starting development server at <http://127.0.0.1:8000/> Quit the server with CONTROL-C.
```

Ignore the warning about unapplied database migrations for now; we'll deal with the database shortly.

You've started the Django development server, a lightweight web server written purely in Python. We've included this with Django so you can develop things rapidly, without having to deal with configuring a production server -- such as Apache -- until you're ready for production.

Now's a good time to note: **don't** use this server in anything resembling a production environment. It's intended only for use while developing. (We're in the business of making web frameworks, not web servers.)

Now that the server's running, visit <http://127.0.0.1:8000/> with your web browser. Or, run `curl 127.0.0.1:8000` in terminal. You'll see a "Congratulations!" page, with a rocket taking off. It worked!

In LabEx VM, we must add need to add the LabEx domain to `ALLOWED_HOSTS`. Edit `mysite/settings.py` and add `*` to the end of `ALLOWED_HOSTS`, so it looks like this:

```python
ALLOWED_HOSTS = ["*"]
```

This tells Django that it's allowed to serve requests with any host header.

![Alt text](./assets/20230907-08-56-33-3uvbOwp3.png)

## Changing the port

By default, the `runserver` command starts the development server on the internal IP at port 8000.

If you want to change the server's port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

```bash
python manage.py runserver 8080
```

If you want to change the server's IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:

```bash
python manage.py runserver 0.0.0.0:8080
```

Now, switch to HTTP 8080 tab in the LabEx VM and you'll see the same "Congratulations" page.

![Alt text](./assets/20230907-08-58-22-M3Luydxk.png)

Full docs for the development server can be found in the `runserver` reference.

> Automatic reloading of `runserver`
> The development server automatically reloads Python code for each request as needed. You don't need to restart the server for code changes to take effect. However, some actions like adding files don't trigger a restart, so you'll have to restart the server in these cases.
