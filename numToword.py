'''Write a program to convert Number to Word'''

def toWord(s):
    words={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
            11:'eleven',12:'twelve',13:'therteen',14:'fourteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
            21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',30:'thirty',
            31:'thirty one',32:'thirty two',33:'thirty three',34:'thirty four',35:'thirty five',36:'thirty six',37:'thirty seven',38:'thirty eight',39:'thirty nine',40:'fourty',
            41:'fourty one',42:'fourty two',43:'fourty three',44:'fourty four',45:'fourty five',46:'fourty six',47:'fourty seven',48:'fourty eight',49:'fourty nine',50:'fifty',
            51:'fifty one',52:'fifty two',53:'fifty three',54:'fifty four',55:'fifty five',56:'fifty six',57:'fifty seven',58:'fifty eight',59:'fifty nine',60:'sixty',
            61:'sixty one',62:'sixty two',63:'sixty three',64:'sixty four',65:'sixty five',66:'sixty six',67:'sixty seven',68:'sixty eight',69:'sixty nine',70:'seventy',
            71:'seventy one',72:'seventy two',73:'seventy three',74:'seventy four',75:'seventy five',76:'seventy six',77:'seventy seven',78:'seventy eight',79:'seventy nine',80:'eighty',
            81:'eighty one',82:'eighty two',83:'eighty three',84:'eighty four',85:'eighty five',86:'eighty six',87:'eighty seven',88:'eighty eight',89:'eighty nine',90:'ninety',
            91:'ninety one',92:'ninety two',93:'ninety three',94:'ninety four',95:'ninety five',96:'ninety six',97:'ninety seven',98:'ninety eight'}
    if len(s)<3:
        return (words[int(s)])
    word=''
    flag=True
    for i in range(len(s)):
        if s[i] == '0':
            flag=False
            continue
        if int(s[i])>0 and int(s[i])<=9 and flag:
            word=word+words[int(s[i])]+' '+'hundred'
            flag=False
            continue
        if int(s[i])>0 and int(s[i])<=9:
            word=word+' '+words[int(s[i:])]
            break
    return (word)            

if __name__=='__main__':
    
    number=input('Enter the Number: ')
    i=len(number)-1
    s=''
    convert=['thousand','million','billion','trillion','quadrallion']
    cWord=[]
    while i>=0:
        if len(s) == 3:
            cWord.append(toWord(s[::-1]))
            s=''
        s=s+number[i]
        i-=1
    cWord.append(toWord(s[::-1]))
    i=len(cWord)-2
    for w in cWord[::-1]:
        print(w,end=" ")
        if i>=0 and w!='':
            print(convert[i],end=" ")
        i-=1
