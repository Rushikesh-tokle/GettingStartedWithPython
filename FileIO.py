import os
f=open("sample.txt","a+")
#f.write("hello my name is rushi ")
f.seek(0)
print(f.readline())
f.close()

#using With
with open("note.txt","a+") as f:
    f.write("Hello Everyone who are present here ")
    f.seek(0)
    data=f.readline()
    print(data)
    
os.remove("sample.txt")