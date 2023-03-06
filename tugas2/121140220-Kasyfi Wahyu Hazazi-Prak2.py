class Kasyfi:
    jumlah_kaki = 2
    jumlah_tangan = 2
    
    def __init__(self,nama,nim,kelas,sks,):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
    
    def manggil_Kasyfi(self):
        print ("halo!, perkenalkan nama saya",self.nama,"dengan NIM",self.nim,"kelas",self.kelas, "dan jumlah SKS",self.sks) 

orang1 = Kasyfi("Kasyfi Wahyu Hazazi", 121140220, "RD", 144)

orang1.manggil_Kasyfi()