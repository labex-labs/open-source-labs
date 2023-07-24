def generate_the_sentences():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]

    for sub in subjects:
        for verb in verbs:
            for obj in objects:
                print("{} {} {}".format(sub, verb, obj))


generate_the_sentences()
