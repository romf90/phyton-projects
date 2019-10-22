def main():
    dict ={}
    dict = create()
    check_key(dict)

def create():
    dict ={}
    for x in range(0, 3):
        key = input('enter a key(string)')
        value = input('enter a value(ineger)')
        dict[key]= value
    return dict

def check_key():
    keycheck = input('enter a key you want to check')
    if(dict.has_key(keycheck)):
        print('true')
    else:
        print('false')
       

       
    
       