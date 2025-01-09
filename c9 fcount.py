count = 0

file = open("file.txt","r")
content = file.read().split()

print(content,len(content))
file.close

file = open("file.txt","a")
newCont = "dewdewded ewfew ewfewfe"
file.write(f"<h2> {newCont} </h2>")
