with open("practice.txt","a+") as f:
    # f.write("hi everyone\n")
    # f.write("we are learning file I/O\n")
    # f.write("using java\n")
    # f.write("i linke programming in Java")
    f.seek(0)
    print(f.read())