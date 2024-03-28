'''fh=open("D:\coding\patcp\cd.txt","r")
contents=fh.read()
print(contents)
fh.seek(1)
d=fh.readline()
print(d)
fh=open("D:\coding\patcp\cd.txt","a")

s="adi is a cult bjp fan \n who doesn't critizise his party openly \n"
w=fh.write(s)
print(w)
f=s.find("bjp")
print(f)
'''
s = "Hello:{0},second{1}".format(2,6)
print(s)
