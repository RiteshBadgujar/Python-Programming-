#Write a recursive function to print all element in a list
list=[1,2,3,4,5]

def show(list,index=0):
    if index == len(list):
        return
    print(list[index])
    show(list,index + 1 )
    
show(list)