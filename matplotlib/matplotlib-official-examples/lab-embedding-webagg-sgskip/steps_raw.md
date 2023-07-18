# Embedding Matplotlib WebAgg Lab

## Introduction

Matplotlib is a Python library that is used for creating static, animated, and interactive visualizations in Python. In this lab, you will learn how to embed Matplotlib WebAgg interactive plotting in your own web application and framework.

## Steps

### Step 1: Create a Simple Example Figure

The first step is to create a simple example figure. In this case, we will create a figure that displays a sine wave.

```python
import numpy as np
import matplotlib.pyplot as plt

def create_figure():
    """
    Creates a simple example figure.
    """
    fig = plt.figure()
    ax = fig.add_subplot()
    t = np.arange(0.0, 3.0, 0.01)
    s = np.sin(2 * np.pi * t)
    ax.plot(t, s)
    return fig

figure = create_figure()
plt.show()
```

### Step 2: Define the HTML Content

In this step, we will define the HTML content that will be used to display the figure in a web application. We will use Python string formatting to replace the placeholders in the HTML content with the appropriate values.

```python
html_content = """<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="_static/css/page.css" type="text/css">
    <link rel="stylesheet" href="_static/css/boilerplate.css" type="text/css">
    <link rel="stylesheet" href="_static/css/fbm.css" type="text/css">
    <link rel="stylesheet" href="_static/css/mpl.css" type="text/css">
    <script src="mpl.js"></script>

    <script>
      function ondownload(figure, format) {
        window.open('download.' + format, '_blank');
      };

      function ready(fn) {
        if (document.readyState != "loading") {
          fn();
        } else {
          document.addEventListener("DOMContentLoaded", fn);
        }
      }

      ready(
        function() {
          var websocket_type = mpl.get_websocket_type();
          var websocket = new websocket_type("%(ws_uri)sws");

          var fig = new mpl.figure(
              %(fig_id)s,
              websocket,
              ondownload,
              document.getElementById("figure"));
        }
      );
    </script>

    <title>matplotlib</title>
  </head>

  <body>
    <div id="figure">
    </div>
  </body>
</html>
"""
```

### Step 3: Create a Tornado Web Application

In this step, we will create a Tornado web application that will serve the HTML content and handle websocket connections.

```python
import io
import json
import mimetypes
from pathlib import Path
import signal
import socket

try:
    import tornado
except ImportError as err:
    raise RuntimeError("This example requires tornado.") from err
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

import numpy as np

import matplotlib as mpl
from matplotlib.backends.backend_webagg import (
    FigureManagerWebAgg, new_figure_manager_given_figure)

class MyApplication(tornado.web.Application):
    class MainPage(tornado.web.RequestHandler):
        def get(self):
            manager = self.application.manager
            ws_uri = f"ws://{self.request.host}/"
            content = html_content % {
                "ws_uri": ws_uri, "fig_id": manager.num}
            self.write(content)

    class MplJs(tornado.web.RequestHandler):
        def get(self):
            self.set_header('Content-Type', 'application/javascript')
            js_content = FigureManagerWebAgg.get_javascript()

            self.write(js_content)

    class Download(tornado.web.RequestHandler):
        def get(self, fmt):
            manager = self.application.manager
            self.set_header(
                'Content-Type', mimetypes.types_map.get(fmt, 'binary'))
            buff = io.BytesIO()
            manager.canvas.figure.savefig(buff, format=fmt)
            self.write(buff.getvalue())

    class WebSocket(tornado.websocket.WebSocketHandler):
        supports_binary = True

        def open(self):
            manager = self.application.manager
            manager.add_web_socket(self)
            if hasattr(self, 'set_nodelay'):
                self.set_nodelay(True)

        def on_close(self):
            manager = self.application.manager
            manager.remove_web_socket(self)

        def on_message(self, message):
            message = json.loads(message)
            if message['type'] == 'supports_binary':
                self.supports_binary = message['value']
            else:
                manager = self.application.manager
                manager.handle_json(message)

        def send_json(self, content):
            self.write_message(json.dumps(content))

        def send_binary(self, blob):
            if self.supports_binary:
                self.write_message(blob, binary=True)
            else:
                data_uri = ("data:image/png;base64," +
                            blob.encode('base64').replace('\n', ''))
                self.write_message(data_uri)

    def __init__(self, figure):
        self.figure = figure
        self.manager = new_figure_manager_given_figure(id(figure), figure)

        super().__init__([
            (r'/_static/(.*)',
             tornado.web.StaticFileHandler,
             {'path': FigureManagerWebAgg.get_static_file_path()}),

            (r'/_images/(.*)',
             tornado.web.StaticFileHandler,
             {'path': Path(mpl.get_data_path(), 'images')}),

            ('/', self.MainPage),

            ('/mpl.js', self.MplJs),

            ('/ws', self.WebSocket),

            (r'/download.([a-z0-9.]+)', self.Download),
        ])

figure = create_figure()
application = MyApplication(figure)
```

### Step 4: Start the Tornado Server

In this step, we will start the Tornado server and listen for incoming connections.

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8080,
                        help='Port to listen on (0 for a random port).')
    args = parser.parse_args()

    http_server = tornado.httpserver.HTTPServer(application)
    sockets = tornado.netutil.bind_sockets(args.port, '')
    http_server.add_sockets(sockets)

    for s in sockets:
        addr, port = s.getsockname()[:2]
        if s.family is socket.AF_INET6:
            addr = f'[{addr}]'
        print(f"Listening on http://{addr}:{port}/")

    ioloop = tornado.ioloop.IOLoop.instance()

    def shutdown():
        ioloop.stop()
        print("Server stopped")

    old_handler = signal.signal(
        signal.SIGINT,
        lambda sig, frame: ioloop.add_callback_from_signal(shutdown))

    try:
        ioloop.start()
    finally:
        signal.signal(signal.SIGINT, old_handler)
```

## Summary

In this lab, you learned how to embed Matplotlib WebAgg interactive plotting in your own web application and framework. By following the steps outlined in this lab, you can create interactive visualizations that can be accessed by users through a web browser.
