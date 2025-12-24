with open("D:\COding\Python\demo.txt","r") as f:
    data = f.read()
    print(data)
    
with open("D:\COding\Python\demo.txt","w") as f:
    f.write("New data add")
    
f.close()  