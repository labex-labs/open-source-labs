# Run the app

Using your terminal, navigate to the directory with the app files and start up the app:

```
$ docker-compose up
```

Docker Compose will build the image and start a container for the app. You should see this output:

```
Creating network "nodeexample_default" with the default driver
Creating nodeexample_web_1
Attaching to nodeexample_web_1
web_1  | [nodemon] 1.9.2
web_1  | [nodemon] to restart at any time, enter `rs`
web_1  | [nodemon] watching: *.*
web_1  | [nodemon] starting `node --debug=5858 app.js`
web_1  | Debugger listening on port 5858
web_1  | HTTP server listening on port 80
```

The app is now running. Open up [http://localhost:8000/](http://localhost:8000) to see it in action, and take a moment to appreciate the poetry.

![Image of Browser with quotations from app](../images/browser-broken.gif "Image of a green background with quotes cycling through. Last image is just two quotation marks")

It’s undoubtedly beautiful, but the problem is obvious: we’re outputting a blank message at the end before cycling back to the first line. It’s time to debug.
