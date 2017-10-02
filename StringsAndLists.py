def findAndReplace():
    words = "It's thanksgiving day. It's my birthday,too!"
    print words.find("day")
    return words.replace("day", "month")

def minAndMax(arr): #Yes, I know it's a list, but "lst" looks a lot like "1st" at lst glance
    print "Min:", min(arr), ", Max:", max(arr)

def firstAndLast(arr):
    arr2 = [arr[0], arr[len(arr) - 1]]
    print arr2[0], arr2[1]  
    return arr2

def newList(arr):
    arr2 = arr.sort()
    front = []
    back = []
    for i in range(0, (len(arr2)//2) - 1):
        front.append(arr2[i])
    for i in range((len(arr2)//2) - 1, len(arr2) - 1):
        back.append(arr2[i])
    back.push()
    
print findAndReplace()
minAndMax([2,54,-2,7,12,98])
firstAndLast(["hello",2,54,-2,7,12,98,"world"])
newList([19,2,54,-2,7,12,98,32,10,-3,6])