# Image layers

There is something else interesting about the images we build with Docker. When running they appear to be a single OS and application. But the images themselves are actually built in **_layers_**. If you scroll back and look at the output from your `docker image build` command you will notice that there were 5 steps and each step had several tasks. You should see several "fetch" and "pull" tasks where Docker is grabbing various bits from Docker Store or other places. These bits were used to create one or more container _layers_. Layers are an important concept. To explore this, we will go through another set of exercises.

First, check out the image you created earlier by using the _history_ command (remember to use the `docker image ls` command from earlier exercises to find your image IDs):

```
docker image history <image ID>
```

<!-- add image of container layer example here-->

What you see is the list of intermediate container images that were built along the way to creating your final Node.js app image. Some of these intermediate images will become _layers_ in your final container image. In the history command output, the original Alpine layers are at the bottom of the list and then each customization we added in our Dockerfile is its own step in the output. This is a powerful concept because it means that if we need to make a change to our application, it may only affect a single layer! To see this, we will modify our app a bit and create a new image.

Type the following in to your console window:

```bash
echo "console.log(\"this is v0.2\");" >> index.js
```

This will add a new line to the bottom of your _index.js_ file from earlier so your application will output one additional line of text. Now we will build a new image using our updated code. We will also tag our new image to mark it as a new version so that anybody consuming our images later can identify the correct version to use:

```bash
docker image build -t hello:v0.2 .
```

You should see output similar to this:

```
Sending build context to Docker daemon  86.15MB
Step 1/5 : FROM alpine
```
