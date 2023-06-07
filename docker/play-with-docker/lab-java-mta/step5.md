# Step 2: Adding a New Front End

One of the big advantages of containers is that they can ease the process of updating older applications by replacing parts of the application as needed. Java EE also makes it easy to consume the output of your application in different ways. This allows you to easily add a different client to an application.

### React Client

In this section, you will update the Movie Plex 7 application by adding more attributes to the movie entity and also updating the presentation layer by writing a new client using [React](https://reactjs.org/). Don't worry, all the code is provided, you don't need to know React.

As you saw earlier, the JavaServer Faces client was rather sparse and old-fashioned looking. You want to make the movie listing to include movie posters as well as more information about each movie. To do that, you will add a few attributes to the Movie entity, and include a path to a movie poster, and more information about the cast and the movie rating.

The Movie Plex 7 application includes a REST interface for querying movies. This simplifies writing a new client because you can use the API and get data via REST. The javaScript client is a bit more descriptive than the original JavaServer Faces client.

![Movieplex7 App with a React JS client displaying movie posters]({{site.baseurl}}/images/react-movieplex7-2.png)

To get a separation of the new client from the existing client and server, you will deploy the React client in a separate container.

To get ready, stop and remove the running container, and then change the directory from `movieplex7` to the root of the project. Due to a quirk in how React is built, and the base url of the Play with Docker lab, before you build the React client you need to run a script to inject the host URL into the Dockerfile:

```bash
docker container stop movieplex7
docker container rm movieplex7
cd ..
./add_ee_pwd_host.sh
more react-client/Dockerfile
```

```dockerfile
FROM node:latest
ENV API_HOST=pwd10-0-16-3-8080.host4.labs.play-with-docker.com
WORKDIR /usr/src/react-client
COPY . .
RUN npm install
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "start"]
```

React uses Node.js to build a static site for the interface. The Dockerfile is much simpler than the one for the `movieplex7` app. It uses a single-stage build, which passes the environment variable `API_HOST` to the builder. When it runs, it will start a simple Node server that serves the React pages, and exposes them on port 3000. We'll deploy it in the next section.
