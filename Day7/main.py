#file = open("example.txt","r")
#print(file.read())     /read the all lines
#print(file.readline()) /line by line read line
#print(file.readlines()) 
#file.close()
#read the lines in the list format


#file=open("example1.txt","a")
#file.write("jp nagar bangalore")

#file.close()

#file=open("example1.txt","a")
#file.write("welcome era")
#file.close()


#with open(r"C:\Users\Lenovo\OneDrive\Pictures\ram.jpg","rb")as f:
    #image = f.read()
    #print(image)


#try:
 #   file = open("sample.txt","r")
  #  print(file.read())
#except FileNotFoundError:
 #   print("File not found,pls open existing file")
#finally:
 #   file.close()


#try:
 #   file = open("sample.txt","r")
  #  print(file.read())
#except Exception as e:
 #   print(f"Error : {e}")
#finally:
 #   file.close()

try:
    file = open("example.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found,pls open existing file")
finally:
    file.close()










   