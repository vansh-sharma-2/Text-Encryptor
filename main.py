ref=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","1","2","3","4","5",'6',"7","8","9","0"]

l1 = []
l2 = []
l3 = []
l4 = []

def reset_list():
    global l1
    global l2
    global l3
    global l4
    l1 = []
    l2 = []
    l3 = []
    l4 = []


def prep_list(code):
    global l1
    global l2
    global l3
    global l4
    reset_list()
    rep = len(ref)
    idx=int((code[0])+(code[1]))
    while rep>0:
        l1.append((ref[idx%len(ref)]))
        idx += 1
        rep -= 1

    rep = len(ref)
    idx=int((code[2])+(code[3]))
    while rep>0:
        l2.append((ref[idx%len(ref)]))
        idx += 1
        rep -= 1
    
    rep = len(ref)
    idx=int((code[4])+(code[5]))
    while rep>0:
        l3.append((ref[idx%len(ref)]))
        idx += 1
        rep -= 1
    
    rep = len(ref)
    idx=int(0)
    while rep>0:
        l4.append((ref[idx%len(ref)]))
        idx += 1
        rep -= 1

def inc_code(cde):
    temp=str(cde)
    t1=(int((temp[0])+(temp[1])))%len(ref)
    t2=(int((temp[2])+(temp[3])))%len(ref)
    t3=(int((temp[4])+(temp[5])))%len(ref)
    t1 += 1
    t1 = t1%len(ref)
    if t1==0:
        t2 += 1
        t2 = t2%len(ref)
        if t2==0:
            t3 += 1
            t3 = t3%len(ref)
    if t1<10:
        t1=str(0)+str(t1)
    if t2<10:
        t2=str(0)+str(t2)
    if t3<10:
        t3=str(0)+str(t3)
    return (str(t1)+str(t2)+str(t3))

def en(char):
    global code
    if char in ref:
        char=l1[ref.index(char)]
        char=l2[ref.index(char)]
        char=l3[ref.index(char)]
        char=l4[ref.index(char)]
        char=l3[ref.index(char)]
        char=l2[ref.index(char)]
        char=l1[ref.index(char)]
    code=inc_code(code)
    prep_list(code)
    return char

def encode(str):
    rep = len(str)
    ret_val = ""
    while rep>0:
        ret_val = ret_val + en(str[len(str)-rep])
        rep -= 1
    return ret_val

def de(char):
    global code
    if char in ref:
        char=ref[l1.index(char)]
        char=ref[l2.index(char)]
        char=ref[l3.index(char)]
        char=ref[l4.index(char)]
        char=ref[l3.index(char)]
        char=ref[l2.index(char)]
        char=ref[l1.index(char)]
    code=inc_code(code)
    prep_list(code)
    return char

def decode(str):
    rep = len(str)
    ret_val = ""
    while rep>0:
        ret_val = ret_val + de(str[len(str)-rep])
        rep -= 1
    return ret_val

def ask_func():
    cmd = input("1. encode \n2. decode \n3. quit \n=> ")
    if cmd=="encode" or cmd=="e" or cmd=="1":
        function="encode"
    elif cmd=="decode" or cmd=="d" or cmd=="2":
        function="decode"
    elif cmd=="quit" or cmd=="3":
        function="quit"
    else:
        function="invalid"
        print("INVALID")
    return function

idx=5
while idx>1:
    cmd=ask_func()
    if cmd=="quit":
        idx=0
    elif cmd=="encode":
        idx=11
        code=input("Enter Code => ")
        prep_list(code)
        while idx>10:
            temp=str(input("=> "))
            if temp=='"quit"':
                idx=0
            elif temp=='"back"':
                idx=5
            else:
                print(encode(temp))
    elif cmd=="decode":
        idx=11
        code=input("Enter Code => ")
        prep_list(code)
        while idx>10:
            temp=str(input("=> "))
            if temp=='"quit"':
                idx=0
            elif temp=='"back"':
                idx=5
            else:
                print(decode(temp))
    else:
        idx -= 1