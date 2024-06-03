# class pbo:
# #     pass

# #IF_A = PBO() #object
# # print(IF_A)

class PBO:
    def __init__(self, nama, nilai): #parameter
        self.NamaMahasiswa = nama
        self.NilaiMahasiswa = nilai

IF_A = PBO("Wahyudi", 80) #object
IF_B = PBO("faris", 80) #object
#mecetak artribut
print("Nama mahasiswa: ",IF_A.NamaMahasiswa, "\nNilai Mahasiswa: ", IF_A.NilaiMahasiswa)
print("Nama mahasiswa: ",IF_B.NamaMahasiswa, "\nNilai Mahasiswa: ", IF_B.NilaiMahasiswa)

x = 20
y = 2

#class \ blueprint\ template

class PBO:
    def _init_(self, nama, umur):
        self.namaSaya = nama
        self.umurSaya = umur

        #ATAU

    def _init_(self, umur):
        self.namaSaya = "jonathan"
        self.umurSaya = umur
    #method
    def cetakNamaUmur(self):
        return f"nama saya: {self.namaSaya}, umur saya: {self.umurSaya}"
    
    def hitungUmur(self):
        return f"nama saya: {self.namaSaya}, umur saya: {self.umurSaya}"
    
# test = PBO("Jonathan", 100) #object
# test2 = PBO("guntur", 200) #object
# print(test.catakNamaUmur())
# print(test.umurSaya)    
# print(test2.catakNamaUmur())
print(test.hitungUmur())

objectOrang = []
pilihan = int(input("Masukan Berapa Object: "))
for i in range(pilihan):
    inputNama = input("Masukan Nama Saya: ")
    inputUmur = int(input("Masukan Umur Saya: "))
    object = PBO(inputNama, inputUmur)
    objectOrang.append(object)

for object in objectOrang:
    print("Nama", object.namaSaya, "Umur", object.umurSaya)