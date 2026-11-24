
from gedung_parkir import (
    Motor,
    Mobil,
    MobilListrik,
    GedungParkir,
    SlotParkir
)

from exception import ParkirError


# ==========================================
# FUNGSI PENGUJIAN EXCEPTION
# ==========================================

def jalankan_skenario(judul, aksi):
    print(f"\n--- {judul} ---")

    try:
        hasil = aksi()

    except ParkirError as error:
        print("Gagal:", error)

    else:
        print("Berhasil:", hasil)

    finally:
        print("Pengujian selesai.")


# ==========================================
# PROGRAM UTAMA
# ==========================================

def main():

    # 1. Membuat gedung parkir
    gedung = GedungParkir("Parkir Primakara")
    gedung.tambah_lantai(2)

    print("================================")
    print("   SISTEM PARKIR PRIMAKARA")
    print("================================")

    print("Nama gedung:", gedung.nama_gedung)

    # 2. Membuat kendaraan
    motor = Motor("DK1234AB")
    mobil = Mobil("DK5678CD")
    listrik = MobilListrik("DK9999EF")

    # 3. Proses parkir berhasil
    tiket_motor = gedung.parkir(motor, 8)
    tiket_mobil = gedung.parkir(mobil, 8)
    tiket_listrik = gedung.parkir(listrik, 8)

    print("\n=== DATA KENDARAAN ===")
    print(motor)
    print(mobil)
    print(listrik)

    print("\n=== TIKET PARKIR ===")
    print("Tiket motor:", tiket_motor.id_tiket)
    print("Tiket mobil:", tiket_mobil.id_tiket)
    print("Tiket mobil listrik:", tiket_listrik.id_tiket)

    # 4. Pengujian custom exception

    # Plat nomor tidak valid
    jalankan_skenario(
        "Plat Nomor Tidak Valid",
        lambda: Motor("")
    )

    # Tarif tidak valid
    jalankan_skenario(
        "Tarif Tidak Valid",
        lambda: setattr(motor, "tarif_per_jam", -1000)
    )

    # Jenis slot tidak valid
    jalankan_skenario(
        "Jenis Slot Tidak Valid",
        lambda: SlotParkir("X1", "Bus")
    )

    # Kendaraan tidak didukung
    jalankan_skenario(
        "Kendaraan Tidak Didukung",
        lambda: gedung.parkir("Sepeda", 8)
    )

    # Kendaraan masih memiliki tiket aktif
    jalankan_skenario(
        "Kendaraan Sudah Parkir",
        lambda: gedung.parkir(motor, 9)
    )

    # Jenis slot tidak sesuai
    jalankan_skenario(
        "Jenis Slot Tidak Sesuai",
        lambda: SlotParkir("M1", "Motor").tempati(
            Mobil("DK3333AA")
        )
    )

    # Waktu tidak valid
    jalankan_skenario(
        "Waktu Tidak Valid",
        lambda: gedung.parkir(Motor("DK1111AA"), -5)
    )

    # Parkir penuh
    def uji_parkir_penuh():
        gedung_uji = GedungParkir("Gedung Uji")
        gedung_uji.parkir(Motor("DK1112AA"), 8)
        return gedung_uji.parkir(Motor("DK1113AA"), 8)

    jalankan_skenario(
        "Parkir Penuh",
        uji_parkir_penuh
    )

    # 5. Proses kendaraan keluar
    print("\n=== PROSES KENDARAAN KELUAR ===")

    print("Biaya motor: Rp", gedung.keluar("1", 10))
    print("Biaya mobil: Rp", gedung.keluar("2", 11))
    print("Biaya mobil listrik: Rp", gedung.keluar("3", 12))

    # 6. Pengujian tiket

    # Tiket tidak ditemukan
    jalankan_skenario(
        "Tiket Tidak Ditemukan",
        lambda: gedung.keluar("999", 12)
    )

    # Tiket sudah digunakan
    jalankan_skenario(
        "Tiket Sudah Keluar",
        lambda: gedung.keluar("1", 12)
    )

    # 7. Menampilkan kondisi slot
    print("\n=== STATUS SLOT PARKIR ===")
    gedung.tampilkan_slot()

    # 8. Menampilkan jumlah kendaraan
    print("\nJumlah kendaraan terdaftar:",
          Motor.jumlah_terdaftar())


if __name__ == "__main__":
    main()
