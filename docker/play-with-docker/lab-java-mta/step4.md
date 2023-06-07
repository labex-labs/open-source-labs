# Step 1: Building the App in a Container

In this section of the lab, you are going to take a Java EE web app running on Wildfly, move it to Tomcat EE, and run it in a Docker container.

The easiest way to move an enterprise Java app into Docker is create a WAR file and deploy it to the app server.

Clone the lab repo into the PWD lab. Remember, you can click the command or manually type it into the terminal window.

```bash
git clone https://github.com/dockersamples/javaee-demo
cd javaee-demo
```

You will build the application using Maven and deploy it to container to see how it looks. Building and deploying the application can be done without having either Maven or an application server on your computer.

First, look at how the original application works. You can do this by building the application in Docker using a Wildfly container which was the app server the project first used. Although the GitHub repo contains an EAR file, you will build the application from source and deploy it using a multi-stage build Dockerfile. Here's the text of the two-stage [Dockerfile.wildfly](https://github.com/dockersamples/javaee-demo/blob/master/movieplex7/Dockerfile.wildfly) file that you can find in the `movieplex7` directory.

```dockerfile
FROM maven:3-jdk-7 AS app
WORKDIR /usr/src/movieplex7
COPY pom.xml .
RUN mvn -B -f pom.xml -s /usr/share/maven/ref/settings-docker.xml dependency:resolve
COPY . .
RUN mvn -B -s /usr/share/maven/ref/settings-docker.xml package -DskipTests

FROM jboss/wildfly
RUN /opt/jboss/wildfly/bin/add-user.sh admin Admin --silent
COPY --from=app /usr/src/movieplex7/target/movieplex7-1.0-SNAPSHOT.war .
EXPOSE 8080 9990
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
```

The first part of the Dockerfile uses a maven container to build the war file. Instead of building the application locally, it is built inside the container with the tool chain needed to compile the application. In the second part of the Dockerfile, you use a Wildfly container and copy the war file built in the previous container to the app server for deployment.

There are a few additional commands to expose the ports and start Wildfly.

Here's how to build the app:

```bash
cd movieplex7
docker image build -t movieplex7 -f Dockerfile.wildfly .
```

This creates a Docker image with the application deployed on Wildfly.

To run the application:

```bash
docker container run -d -p 8080:8080 --name movieplex7 movieplex7
```

[Click here to see it running](/movieplex7-1.0-SNAPSHOT){:data-term=".term1"}{:data-port="8080"}

![Movieplex7 Landing Page in Wildfly]({{site.baseurl}}/images/wildfly-movieplex7.png)

Your app is working just fine in Docker now, with no code changes and running in the original app server. Feel free to play around with the functionality of the site to understand the app better.
