f1 = open("Marks.txt")
f2 = open("Final.txt","w")

for line in f1:
    data = (line.strip()).split(",")
    Total = float(data[1])+float(data[2])
    f2.write("%s-%3d\n"%(data[0],Total))
             
f1.close()
f2.close()
