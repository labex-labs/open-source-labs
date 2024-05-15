# Address Already in Use

If you see an `OSError` with the message "Address already in use" when trying to start the server, it means that another program is already using the port 5000, which is the default port for the development server. You can either identify and stop the other program or choose a different port.

To identify the process using port 5000, you can use the `netstat` or `lsof` command. Here are examples for Linux, macOS, and Windows:

- Linux:

```bash
netstat -nlp | grep 5000
```

- macOS / Linux:

```bash
lsof -P -i :5000
```

- Windows:

```bash
-ano > netstat | findstr 5000
```

Once you have identified the process, you can use other operating system tools to stop it. After stopping the process, you should be able to run the development server without any issues.
