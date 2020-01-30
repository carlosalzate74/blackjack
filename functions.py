from os import system, name

# define a clear screen function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')   
    # for mac and linux
    else: 
        _ = system('clear')