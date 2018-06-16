str = input("Enter String :")
for i in  range(int(len(str)/2)):
    if(str[i] != str[len(str)-i-1]):
        print('Not')
        break;
