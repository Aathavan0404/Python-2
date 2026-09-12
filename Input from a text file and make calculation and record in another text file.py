f1 = open("Marks.txt")
f2 = open("Final.txt","w")

line= f1.readline()
#reads the first line of the file and assigns it to the variable 'line'. The pointer moves to the next line after reading.

while (line): #loop works until the line becomes empty
    data = (line.strip()).split(",")
#strip() removes the leading and trailing whitespace characters from the string. 
#split(",") splits the string into a list of substrings based on the comma delimiter.
    Total = float(data[1])+float(data[2])
    f2.write("{},{},{},{}\n".format(data[0],data[1],data[2],Total))
#format function used to write data in this format
    line=f1.readline() 
#Readline reads the line how many times we call it. It reads the line and moves the pointer to the next line. 

f1.close()
f2.close()
