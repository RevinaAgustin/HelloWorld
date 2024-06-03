#ASOSIASI

# class penjual():
#     def __init__(self, nama, harga, barang):
#         self.nama = nama
#         self.barang = barang
#         self.harga = harga
#     def jual(self, pembeli):
#         print(f"(self.nama) menjual (self.barang) kepada (pembeli) dengan harga (self.harga)")
# class pembeli():

#     def __init__(self, nama):
#         self.nama = nama

# def mainProgram():
#     print("Hubunga antar penjual dan pembeli")
#     guntur = penjual("guntur","narkoboy","Rp 1.000.000")
#     guntur = penjual("guntur","M4A1","Rp 3.200.000")
#     ahmid = pembeli ("ahmid")
#     fahmi = pembeli("fahmi")
#     guntur.jual(ahmid)

# mainProgram()



#AGROGASI
class karyawan():
    def __init__(self, nama, umur, jabatan, jam ):
        self.nama = nama
        self.umur = umur
        self.jabatan = jabatan
    def info(self, honor):
        totalGaji = honor.gajiPokok + honor.lembur + honor.tunjangan
        totalGaji -= honor.pajak #totalGaji = totalGaji - honor.pajak
        if totalGaji < 0:
            print(f"{self.nama} miskin")
        else:
         print(f"{self.nama} mendapatkan honor sebanyak Rp. {totalGaji} per bulan")
class honor():
    def __init__(self, gajiPokok, lembur, tunjangan, pajak):
        self.gajiPokok = gajiPokok
        self.lembur = lembur
        self.tunjangan = tunjangan
        self.pajak = pajak
def main():
   print("agregasi (saling memiliki)")
   aiss = karyawan("aiss", 24)
   guntur = karyawan("guntur" , 30)
   honor_aiss = honor(5000000, 3000000, 20000000, 1000)
   honor_guntur = honor(8000000, 2000000, 1000000, 100000000)
   aiss.info(honor_aiss)
   guntur.info(honor_guntur)
main()


class warga():
    def __init__(self, nama):
        self.nama = nama
        self.ktp = ktp(None, None)
class ktp():
    def __init__(self, nik, nomor):
        self.nik = nik
        self.nomor = nomor 
    def cetak (self, warga):
        print(f"kepemilikan nik ktp ini {self.nik} dan {self.nomor} adalah {warga.nama}")
def main():
    rafi = warga("rafi")
    rafi.ktp.nik = input("silakan masukan nik ktp:")
    rafi.ktp.nomor = input("masukan nomor:")
    rafi.ktp.cetak(rafi)
main()