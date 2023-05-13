sayılar = [3,100,8,12,89,34,99,-8,-72,0]    #sayılar tanımlanır
max = sayılar[0]        #max değişkeni oluşturulur ve herhangi bir değere atanır

for i in sayılar:       #for döngüsü ile maximum değer dizideki her sayıyla tek tek karşılaştırılır eğer değer maximumdan büyük ise karşılaştırılan değer yeni max olur
    if i > max:
        max = i  
        
print(sayılar)      #liste ekrana yazılır

print(max)          #max değişkeni ekrana yazdırılır

input("Çıkmak için ENTER'a basınız")