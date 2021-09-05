def western_numbers(n):
    num=str(n).lstrip('0')
    digits=len(num)
    a=''
    if digits==1:
        if n in Dict1:
            return Dict1[n]
    else:
        while digits>1:
            if digits==12 or digits==11 or digits==10:
                a=a+billions(n)
                n=n%1000000000
                num=str(n)
                digits=len(num)
            elif digits==9 or digits==8 or digits==7:
                a=a+million(n)
                n=n%1000000
                num=str(n)
                digits=len(num)
            elif digits==5 or digits==4 or digits==6:
                a=a+thousand(n)
                n=n%1000
                num=str(n)
                digits=len(num)
            elif digits==3:
                a=a+hundred(n)
                n=n%100
                num=str(n)
                digits=len(num)
            elif digits==2:
                a=a+tens(n)
                n=n%10
                num=str(n)
                digits=len(num)
        return a
def billions(n):
    num=str(n).lstrip('0')
    digits=len(num)
    a1=n//1000000000
    if digits==10:
        if a1 in Dict1:
            b= Dict1[a1]+' billion '
            return b
    elif digits==11:
        b=a1//10
        c=a1%10
        if a1 in Dict1:
            return Dict1[a1]+' billion '
        elif a1 in Dict2:
            return Dict2[a1]+' billion '
        elif b in Dict2 and c in Dict1:
            d= Dict2[b]+' '+Dict1[c]+' billion '
            return d
        elif b in Dict2 and c not in Dict1:
            d=Dict2[b] +' billion '
            return d
        elif b not in Dict2 and c in Dict1:
            d=Dict1[c] +' billion '
            return d
    elif digits==12:
        w=a1//100
        b=(a1%100)//10
        c=(a1%100)%10
        if w in Dict1 and b not in Dict1 and c not in Dict1:
            return Dict1[w]+' hundred billion '
        elif w in Dict1 and b in Dict1 and c not in Dict1:
            return Dict1[w]+' hundred '+Dict2[b]+' billion '
        elif w in Dict1 and b not in Dict1 and c in Dict1:
            return Dict1[w]+' hundred '+Dict1[c]+' billion '
        elif w in Dict1 and b in Dict1 and c in Dict1:
            return Dict1[w]+' hundred '+Dict2[b]+' '+Dict1[c]+' billion '

def million(n):
    num=str(n)
    digits=len(num)
    a2=n//1000000
    if digits==7:
        if a2 in Dict1:
            b= Dict1[a2]+' million '
            return b
    elif digits==8:
        b=a2//10
        c=a2%10
        if a2 in Dict1:
            return Dict1[a2]+' millions '
        elif a2 in Dict2:
            return Dict2[a2]+' millions '
        elif b in Dict2 and c in Dict1:
            d= Dict2[b]+' '+Dict1[c]+' millions '
            return d
        elif b in Dict2 and c not in Dict1:
            d=Dict2[b] +' millions '
            return d
        elif b not in Dict2 and c in Dict1:
            d=Dict1[c] +' millions '
            return d
    elif digits==9:
        w=a2//100
        b=(a2%100)//10
        c=(a2%100)%10
        if w in Dict1 and b not in Dict1 and c not in Dict1:
            return Dict1[w]+' hundred million '
        elif w in Dict1 and b in Dict1 and c not in Dict1:
            return Dict1[w]+' hundred '+Dict2[b]+' million '
        elif w in Dict1 and b not in Dict1 and c in Dict1:
            return Dict1[w]+' hundred '+Dict1[c]+' million '
        elif w in Dict1 and b in Dict1 and c in Dict1:
            return Dict1[w]+' hundred '+Dict2[b]+' '+Dict1[c]+' million '

def thousand(n):
    num=str(n)
    digits=len(num)
    a3=n//1000
    if digits==4:
        if a3 in Dict1:
            b= Dict1[a3]+' thousand '
            return b
    elif digits==5:
        b=a3//10
        c=a3%10
        if a3 in Dict1:
            return Dict1[a3]+' thousand '
        elif a3 in Dict2:
            return Dict2[a3]+' thousand '
        elif b in Dict2 and c in Dict1:
            d= Dict2[b]+' '+Dict1[c]+' thousand '
            return d
        elif b in Dict2 and c not in Dict1:
            d=Dict2[b] +' thousand '
            return d
        elif b not in Dict2 and c in Dict1:
            d=Dict1[c] +' thousand '
            return d
    elif digits==6:
        w=a3//100
        b=(a3%100)//10
        c=(a3%100)%10
        if w in Dict1 and b not in Dict1 and c not in Dict1:
            return Dict1[w]+' hundred thousand '
        elif w in Dict1 and b in Dict1 and c not in Dict1:
            return Dict1[w]+' hundred '+Dict2[b]+' thousand '
        elif w in Dict1 and b not in Dict1 and c in Dict1:
            return Dict1[w]+' hundred '+Dict1[c]+' thousand '
        elif w in Dict1 and b in Dict1 and c in Dict1:
            return Dict1[w]+' hundred '+Dict2[b]+' '+Dict1[c]+' thousand '
def hundred(n):
    num=str(n)
    digits=len(num)
    a4=n//100
    if a4 in Dict1:
        b=Dict1[a4]+' hundred '
        return b
    else:
        b=''
        return b
def tens(n):
    num=str(n)
    digits=len(num)
    a5=n//10
    b=n%10
    if n in Dict1:
        return Dict1[n]
    elif n in Dict2:
        return Dict2[n]
    elif a5 in Dict2 and b in Dict1:
        d= Dict2[a5]+' '+Dict1[b]
        return d
    elif a5 not in Dict2 and b in Dict1:
        d=Dict1[b]
        return d
    elif a5 in Dict2 and b not in Dict1:
        d=Dict2[a5]
        return d
n=int(input())
Dict1={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',
           13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
Dict2={1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
q=western_numbers(n)
print(q)
