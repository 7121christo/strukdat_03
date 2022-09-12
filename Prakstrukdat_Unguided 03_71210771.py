#71210771 - Christophorus Adyatma Wahyu Setya Nayottama

kalimat=str(input("Masukkan sebuah kalimat: "))
kata=str(input("Masukkan sebuah kata dari kalimat: "))

kalimat = kalimat.lower().split()
kata = kata.lower()


a=0
for i in kalimat:
    if i == kata:
        a += 1

print(a)