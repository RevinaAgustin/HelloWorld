# akses Modifer
# public
# class Here:
#     def __init__(self, nama, hp):
#         self.nama = nama
#         self.hp = hp
# class Hero_Status(Hero):
#     def __init__(self, nama):
#         super().__init__(nama, 100)

# chaeunwoo = Hero_Status("cha eun woo")
# print(chaeunwoo, nama, "dan", chaeunwoo.hp)



#protected
# class Hero:
#     def __init__(self, nama, hp, power):
#         self._nama = nama
#         self._hp = hp
#         self._power = power
#     def _buff(self, buff):
#         print("Total Power", self._power + buff)
# class Hero_Status(Hero):
#     def __init__(self, nama, hp, power):
#         super().__init__ (nama, hp, power)
#     def debuff(self, debuff):
#         print("Total Power:", self._power - debuff)

# chaeunwoo = Hero("chaeunwoo", 100, 200)
# chaeunwoo._buff(300)
# kimjongucnh = Hero_Status("kimjongucnh", 100, 200)
# kimjongucnh._power = 200
# kimjongucnh.debuff(100)

#setter getter
class IF:
    def __init__(self, nama, nim):
        self._nama = nama
        self._nim = nim
    def pindah_kelas(self, nimBaru):
        self._nim = nimBaru #setter
        def show_nim(self):
            return self._nim #getter
    def __cetak(self):
        print(f"Nama Mahasiswa: {self._nama} dan NIM mahasiswa tsb adalah {self._nim}")

Aiss = IF("Aiss", 1152700013)
print("Sebelum pindah kelas: ")
Aiss.cetak()
print("Sesudah pindah kelas:")
Aiss.pindah_kelas(1152700011)
Aiss.cetak()

# class MerekHP:
#     __jumlah = 0
#     def __init__(self, nama):
#         self.nama = nama
#         MerekHP .__jumlah += 1
# classmethod
# def showMerek(cls):
#     print(f"merk hp: {cls.__name__}")
#     staticmethod
#     def showJumlahHP():
#         print(f"Jumlah HP keseluruhan: {MerekHP.__jumlah}")
# class Xiomi(MerekHP):
#     def __init__(self, nama):
#         super().__init__(nama)
# class Samsung(MerekHP):
#     def __init__(self, nama):
#         super().__init__(nama)

# samsung _1 = Samsung("Samsung Galaxy")  