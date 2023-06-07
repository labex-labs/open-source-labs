# Step 3: Moving from Wildfly to Tomcat EE

In Step 1, you compiled and deployed the Movie Plex 7 application from source by building it in a Maven container and then deploying it in a Wildfly container. The JavaServer Faces front-end was integrated into the the same application image.

In this step you will make three changes. First, as described in the previous step, you will use a React front-end deployed in a second container. Second, you will deploy the app in a Tomcat EE application server instead of Wildfly. Last, you will deploy both at the same time using a Docker Compose file.

The new front-end is described in the last section, so take a look at the new Dockerfile that deploys your app using the Tomcat Server.

```bash
more movieplex7/Dockerfile
```

```dockerfile
FROM maven:latest AS app
WORKDIR /usr/src/movieplex7
COPY pom.xml .
RUN mvn -B -f pom.xml -s /usr/share/maven/ref/settings-docker.xml dependency:resolve
COPY . .
RUN mvn -B -s /usr/share/maven/ref/settings-docker.xml package -DskipTest

FROM tomee:8-jre-7.0.2-plume

# tomcat-users.xml sets up user accounts for the Tomcat manager GUI
# and script access for Maven deployments
WORKDIR /usr/local/tomee/
ADD tomcat/tomcat-users.xml conf/
ADD tomcat/web.xml conf/
# copy and deploy application
WORKDIR /usr/local/tomee/webapps/
COPY --from=app /usr/src/movieplex7/target/movieplex7-1.0-SNAPSHOT.war .
# start tomcat7
EXPOSE 8080
CMD ["catalina.sh", "run"]
```

You'll see that the first stage is very similar to `Dockerfile.wildfly`. Only instead of using `maven:3-jdk-7` as the base image, it uses `maven:latest`. There's still no code change, you are still compiling the code into a WAR file. The second stage is a bit different, because it uses a different application server. But the end result is the same application running on both.

You now have two Dockerfiles, one to build the Java Movie Plex 7 application and another to build the React javaScript client. Running a build for each will result in two images. You can individually run each image with the appropriate flags, but a simpler and more consistent solution is to use Docker Compose to start both images as containers that are connected by a network defined in Docker. Another nice thing about Docker Compose is that you can also build the images without having to do a separate `docker image build` command for each image. This is the `docker-compose.yml` file in the project root:

```
version: "3.3"

services:
  movieplex7:
    build:
      context: ./movieplex7
    image: movieplex7-tomee
    ports:
      - "8080:8080"
    networks:
      - www

  react-client:
    build:
      context: ./react-client
    image: react-client
    ports:
      - "80:3000"
    networks:
      - www

networks:
    www:
```

The Compose file defines each service and the ports that they are mapped to. Of note is the react-client, which maps the public port 80 to the private in-container port of 3000.

To run and build the images use:

```bash
docker-compose up --build -d
```

Once it's completed building, which the first time can take awhile, we can check on the status of the containers:

```bash
docker container ls
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
02c1ee2be5ff        movieplex7-tomee    "catalina.sh run"   26 minutes ago      Up 26 minutes       0.0.0.0:8080->8080/tcp   javaeedemo_movieplex7_1
2a65e6f08819        react-client        "npm run start"     26 minutes ago      Up 26 minutes       0.0.0.0:80->3000/tcp     javaeedemo_react-client_1
```

This shows that the containers are running. Since there is overhead to start and deploy the war file you can look at the log files of the `movieplex7` container to check if it’s started

```bash
docker logs javaeedemo_movieplex7_1
```

```
...
02-Oct-2017 21:01:22.069 INFO [main] sun.reflect.DelegatingMethodAccessorImpl.invoke Starting ProtocolHandler [http-nio-8080]
02-Oct-2017 21:01:22.084 INFO [main] sun.reflect.DelegatingMethodAccessorImpl.invoke Starting ProtocolHandler [ajp-nio-8009]
02-Oct-2017 21:01:22.088 INFO [main] sun.reflect.DelegatingMethodAccessorImpl.invoke Server startup in 15073 ms
```

Now that the application server has started, you can click [here](/){:data-term=".term1"}{:data-port="80"} and try out the new interface.

![Movieplex7 React Front-end]({{site.baseurl}}/images/react-movieplex7.png)

And the old interface is still there, you can see it by clicking on [here](/movieplex7-1.0-SNAPSHOT){:data-term=".term1"}{:data-port="8080"}.