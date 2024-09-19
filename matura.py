wiersze=open('przyklad.txt','r')
tab=[]

# for wiersz in wiersze:
#     tab.append(wiersz.strip())

#4.1 zadanie
# count=0
# for i in tab:
#     if i[0]==i[len(i)-1]:
#         count+=1
# print(count)

# 4.2

# for wiersz in wiersze:
#     tab.append(int(wiersz.strip()))
#
# def czynniki(a):
#     licznik=0
#     i=2
#     while(a!=1):
#        if a%i==0:
#            licznik+=1
#            a=a/i
#        else:
#            i+=1
#     return licznik
# def czynniki_rozne(a):
#     sett = set()
#     licznik_roznych=1
#     i=2
#     while(a!=1):
#        if a%i==0:
#            sett.add(i)
#            a=a/i
#        else:
#            i+=1
#     return len(sett)
#
# max_czynniki_liczba=0
# max_czynniki=0
# max_czynniki_rozne_liczba=0
# max_czynniki_rozne=0
# for i in tab:
#     if czynniki(i)>max_czynniki:
#         max_czynniki=czynniki(i)
#         max_czynniki_liczba=i
#     if czynniki_rozne(i)>max_czynniki_rozne:
#         max_czynniki_rozne=czynniki_rozne(i)
#         max_czynniki_rozne_liczba = i
#
# print(str(max_czynniki_rozne_liczba) + "  "+ str(max_czynniki_rozne) + "  "+ str(max_czynniki_liczba)+ "   "+ str(max_czynniki))
#4.3
for wiersz in wiersze:
    tab.append(int(wiersz.strip()))
    tab.sort()
def wielkrotnosc(a,b):
    if a!=b and (a%b==0 or b%a==0):
        return True
    else:
        return False
licznik=0
for i in range(len(tab)):
    for j in range(i,len(tab)-1):
        if wielkrotnosc(tab[i],tab[j]):
            for k in range(j,len(tab)-2):
                    if wielkrotnosc(tab[k],tab[j]):
                            print(str(tab[i])+ "  "+ str(tab[j])+" "+ str(tab[k]))
                            licznik+=1

print(licznik)
licznik_pieciu=0
for i in range(len(tab)):
    for j in range(i,len(tab)-1):
        if wielkrotnosc(tab[i],tab[j]):
            for k in range(j,len(tab)-2):
                    if wielkrotnosc(tab[k],tab[j]):
                        for l in range(k,len(tab)-3):
                            if wielkrotnosc(tab[l],tab[k]):
                                for m in range(l, len(tab) - 4):
                                    if wielkrotnosc(tab[m], tab[l]):
                                        print(str(tab[i]) + "  " + str(tab[j]) + " " + str(tab[k])+"  "+ str(tab[l])+ "  "+str(tab[m]))
                                        licznik_pieciu+=1
print(licznik_pieciu)






