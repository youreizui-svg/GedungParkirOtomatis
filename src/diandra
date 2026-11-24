from abc import ABC, abstractmethod
# 1. CLASS KENDARAAN (ABSTRACT CLASS)
class Kendaraan(ABC):
    jumlah_kendaraan = 0

    def __init__(self, plat_nomor, tarif_per_jam):
        self.plat_nomor = plat_nomor
        self.tarif_per_jam = tarif_per_jam
        Kendaraan.jumlah_kendaraan += 1

    @staticmethod
    def validasi_plat(plat):
        return isinstance(plat, str) and len(plat.strip()) >= 3

    @property
    def plat_nomor(self):
        return self.__plat_nomor

    @plat_nomor.setter
    def plat_nomor(self, nilai):
        if not self.validasi_plat(nilai):
            raise ValueError("Plat nomor tidak valid")
        self.__plat_nomor = nilai

    @property
    def tarif_per_jam(self):
        return self.__tarif_per_jam

    @tarif_per_jam.setter
    def tarif_per_jam(self, nilai):
        if (not isinstance(nilai, (int, float))
                or isinstance(nilai, bool) or nilai <= 0):
            raise ValueError("Tarif harus positif")
        self.__tarif_per_jam = nilai

    @abstractmethod
    def hitung_biaya(self, jam):
        return self.tarif_per_jam * jam

    def tampilkan_info(self):
        return f"{self.plat_nomor} - Rp{self.tarif_per_jam}/jam"

    def __str__(self):
        return self.tampilkan_info()

    def __eq__(self, obj):
        return (type(self) == type(obj)
                and self.plat_nomor == obj.plat_nomor)

    @classmethod
    def jumlah_terdaftar(cls):
        return Kendaraan.jumlah_kendaraan


# 2. CLASS MOTOR
class Motor(Kendaraan):
    def __init__(self, plat_nomor, jenis_motor="Matic"):
        super().__init__(plat_nomor, 2000)
        self.jenis_motor = jenis_motor

    def hitung_biaya(self, jam):
        return super().hitung_biaya(jam)


# 3. CLASS MOBIL
class Mobil(Kendaraan):
    def __init__(self, plat_nomor, jumlah_pintu=4):
        super().__init__(plat_nomor, 5000)
        self.jumlah_pintu = jumlah_pintu

    def hitung_biaya(self, jam):
        return super().hitung_biaya(jam)


# 4. CLASS MOBIL LISTRIK
class MobilListrik(Mobil):
    def __init__(self, plat_nomor, jumlah_pintu=4):
        super().__init__(plat_nomor, jumlah_pintu)
        self.tarif_per_jam = 7000

    def hitung_biaya(self, jam):
        return super().hitung_biaya(jam)


# 5. CLASS SLOT PARKIR
class SlotParkir:
    def __init__(self, nomor_slot, jenis_slot):
        self.nomor_slot = nomor_slot
        self.jenis_slot = jenis_slot
        self.__kendaraan = None

    @property
    def jenis_slot(self):
        return self.__jenis_slot

    @jenis_slot.setter
    def jenis_slot(self, nilai):
        if nilai not in ("Motor", "Mobil"):
            raise ValueError("Jenis slot tidak valid")
        self.__jenis_slot = nilai

    def tersedia(self):
        return self.__kendaraan is None

    def cocok(self, kendaraan):
        if isinstance(kendaraan, Motor):
            return self.jenis_slot == "Motor"
        if isinstance(kendaraan, Mobil):
            return self.jenis_slot == "Mobil"
        return False

    def tempati(self, kendaraan):
        if self.tersedia() and self.cocok(kendaraan):
            self.__kendaraan = kendaraan
            return True
        return False

    def kosongkan(self):
        kendaraan = self.__kendaraan
        self.__kendaraan = None
        return kendaraan


# 6. CLASS LANTAI PARKIR
class LantaiParkir:
    def __init__(self, nomor_lantai):
        self.nomor_lantai = nomor_lantai
        self.daftar_slot = [
            SlotParkir(f"M{nomor_lantai}1", "Motor"),
            SlotParkir(f"C{nomor_lantai}1", "Mobil"),
            SlotParkir(f"C{nomor_lantai}2", "Mobil")
        ]

    def tambah_slot(self, slot):
        self.daftar_slot.append(slot)

    def cari_slot_kosong(self, jenis):
        for slot in self.daftar_slot:
            if slot.tersedia() and slot.jenis_slot == jenis:
                return slot
        return None


# 7. CLASS TIKET PARKIR
class TiketParkir:
    def __init__(self, id_tiket, kendaraan, slot, waktu_masuk):
        self.id_tiket = id_tiket
        self.kendaraan = kendaraan
        self.slot = slot
        self.waktu_masuk = waktu_masuk
        self.waktu_keluar = None

    def hitung_durasi(self):
        if self.waktu_keluar is None:
            return 0
        return max(1, self.waktu_keluar - self.waktu_masuk)

    def hitung_total(self):
        return self.kendaraan.hitung_biaya(self.hitung_durasi())


# 8. CLASS GEDUNG PARKIR
class GedungParkir:
    nomor_tiket = 1

    def __init__(self, nama_gedung):
        self.nama_gedung = nama_gedung
        self.daftar_lantai = [LantaiParkir(1)]
        self.daftar_tiket = []

    def tambah_lantai(self, nomor):
        self.daftar_lantai.append(LantaiParkir(nomor))

    def parkir(self, kendaraan, waktu_masuk):
        if isinstance(kendaraan, Motor):
            jenis = "Motor"
        elif isinstance(kendaraan, Mobil):
            jenis = "Mobil"
        else:
            return None

        for lantai in self.daftar_lantai:
            slot = lantai.cari_slot_kosong(jenis)

            if slot is not None and slot.tempati(kendaraan):
                tiket = TiketParkir(
                    str(GedungParkir.nomor_tiket),
                    kendaraan,
                    slot,
                    waktu_masuk
                )

                GedungParkir.nomor_tiket += 1
                self.daftar_tiket.append(tiket)
                return tiket

        return None

    def keluar(self, id_tiket, waktu_keluar):
        for tiket in self.daftar_tiket:
            if (tiket.id_tiket == str(id_tiket)
                    and tiket.waktu_keluar is None):

                tiket.waktu_keluar = waktu_keluar
                biaya = tiket.hitung_total()
                tiket.slot.kosongkan()
                return biaya

        return None

    def tampilkan_slot(self):
        for lantai in self.daftar_lantai:
            for slot in lantai.daftar_slot:
                status = "Kosong" if slot.tersedia() else "Terisi"
                print(slot.nomor_slot, status)


# 9. PROGRAM UTAMA
if __name__ == "__main__":
    gedung = GedungParkir("Parkir Primakara")
    gedung.tambah_lantai(2)

    motor = Motor("DK1234AB")
    mobil = Mobil("DK5678CD")
    listrik = MobilListrik("DK9999EF")

    tiket_motor = gedung.parkir(motor, 8)
    tiket_mobil = gedung.parkir(mobil, 8)
    tiket_listrik = gedung.parkir(listrik, 8)

    print("Gedung:", gedung.nama_gedung)
    print("Motor:", motor)
    print("Mobil:", mobil)
    print("Mobil listrik:", listrik)

    print("Tiket motor:", tiket_motor.id_tiket)
    print("Tiket mobil:", tiket_mobil.id_tiket)
    print("Tiket mobil listrik:", tiket_listrik.id_tiket)

    print("Biaya motor:", gedung.keluar("1", 10))
    print("Biaya mobil:", gedung.keluar("2", 11))
    print("Biaya mobil listrik:", gedung.keluar("3", 12))

    print("Objek sama:", motor == Motor("DK1234AB"))

    try:
        motor.plat_nomor = ""
    except ValueError as error:
        print("Validasi:", error)

    print("Tarif mobil listrik:", listrik.tarif_per_jam)
