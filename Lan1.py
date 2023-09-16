import re
filename = "TextFile1.txt"
newfilename = "result.txt"

# read the file
data = open(filename,'r')
bulkemails = data.read()
# regex = something@domain.com.xxx
mail=re.compile(r'[\w\.]+@[a-zA-Z_\.]+\.\w+')
results = mail.findall(bulkemails)
print("\n\t\tDay la thu nghiem tim mail\n")
print(results)
# 00 + Ma quoc gia + ma vung + sđt
#+84 + Ma quoc gia + ma vung + sđt    4-3-4||3-4-3||3-3-3
sdt=re.compile(r'[.-_()]?[00+]?\d{3,4}[()-\. ]*\d{3,4}[()-\. ]*\d{3,4}[.-_()]?')
ssss=sdt.findall(bulkemails)
print("\n\t\tDay la thu nghiem tim sdt\n")
print(ssss)
# ten web: https://www.xx.xx or www.xx.xx
tenmien=re.compile(r'https?[www\.]?://[a-zA-Z]+\.\w+|www\.[a-zA-Z]+\.\w+')
ma=tenmien.findall(bulkemails)
print("\n\t\tDay la thu nghiem tim ten web\n")
print(ma)
xxx=re.compile(r'[\w\.]+@[a-zA-Z_\.]+\.\w+|[.-_()]?[00+]?\d{3,4}[()-\. ]?\d{3,4}[()-\. ]?\d{3,4}[.-_()]?|https?[www\.]?://[a-zA-Z]+\.\w+|www\.[a-zA-Z]+\.\w+')
sss=xxx.findall(bulkemails)
print(sss)
kq=""
for i in sss:
    vitri=bulkemails.find(i)
    kq += '('+str(vitri)+','+str(len(i))+','+i+')'
#write the file
wri=open(newfilename,'w')
wri.write(kq)
wri.close()



