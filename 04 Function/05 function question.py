#  Write a python function to remove a given word from a string and strip 
#  it at the same time.

def remove_strip(a, word):
    newstr = a.replace("not", "")
    return newstr.strip()


a = "      Harsh is not good programmer       "
n = remove_strip(a,"not")
print(n)
