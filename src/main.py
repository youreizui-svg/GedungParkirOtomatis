
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

    # ======================================
    # A. SKENARIO BERHASIL
    # ======================================

    print("\n========================================")
    print("            SKENARIO BERHASIL")
    print("========================================")

    # 1. Membuat gedung parkir
    gedung = GedungParkir("Parkir Primakara")
    gedung.tambah_lantai(2)

    print("\nNama gedung:", gedung.nama_gedung)

    # 2. Membuat kendaraan
    motor = Motor("DK1234AB")
    mobil = Mobil("DK5678CD")
    listrik = MobilListrik("DK9999EF")

    # 3. Proses kendaraan masuk
    print("\n--- Proses Kendaraan Masuk ---")

    tiket_motor = gedung.parkir(motor, 8)
    print("Motor berhasil parkir.")

    tiket_mobil = gedung.parkir(mobil, 8)
    print("Mobil berhasil parkir.")

    tiket_listrik = gedung.parkir(listrik, 8)
    print("Mobil listrik berhasil parkir.")

    # 4. Menampilkan data kendaraan
    print("\n--- Data Kendaraan ---")
    print("Motor:", motor)
    print("Mobil:", mobil)
    print("Mobil listrik:", listrik)

    # 5. Menampilkan tiket parkir
    print("\n--- Data Tiket Parkir ---")
    print("Tiket motor:", tiket_motor.id_tiket)
    print("Tiket mobil:", tiket_mobil.id_tiket)
    print("Tiket mobil listrik:", tiket_listrik.id_tiket)

    # 6. Menguji kesamaan objek
    print("\n--- Pengujian Kesamaan Kendaraan ---")
    print("Objek motor sama:", motor == Motor("DK1234AB"))

    # ======================================
    # B. SKENARIO GAGAL
    # ======================================

    print("\n========================================")
    print("             SKENARIO GAGAL")
    print("========================================")

    # 1. Plat nomor tidak valid
    jalankan_skenario(
        "Plat Nomor Tidak Valid",
        lambda: Motor("")
    )

    # 2. Tarif tidak valid
    jalankan_skenario(
        "Tarif Tidak Valid",
        lambda: setattr(motor, "tarif_per_jam", -1000)
    )

    # 3. Jenis slot tidak valid
    jalankan_skenario(
        "Jenis Slot Tidak Valid",
        lambda: SlotParkir("X1", "Bus")
    )

    # 4. Kendaraan tidak didukung
    jalankan_skenario(
        "Kendaraan Tidak Didukung",
        lambda: gedung.parkir("Sepeda", 8)
    )

    # 5. Kendaraan sudah memiliki tiket aktif
    jalankan_skenario(
        "Kendaraan Sudah Parkir",
        lambda: gedung.parkir(motor, 9)
    )

    # 6. Jenis slot tidak sesuai
    jalankan_skenario(
        "Jenis Slot Tidak Sesuai",
        lambda: SlotParkir("M1", "Motor").tempati(
            Mobil("DK3333AA")
        )
    )

    # 7. Waktu tidak valid
    jalankan_skenario(
        "Waktu Tidak Valid",
        lambda: gedung.parkir(Motor("DK1111AA"), -5)
    )

    # 8. Parkir penuh
    def uji_parkir_penuh():
        gedung_uji = GedungParkir("Gedung Uji")

        gedung_uji.parkir(Motor("DK1112AA"), 8)

        return gedung_uji.parkir(
            Motor("DK1113AA"), 8
        )

    jalankan_skenario(
        "Parkir Penuh",
        uji_parkir_penuh
    )

    # 9. Tiket tidak ditemukan
    jalankan_skenario(
        "Tiket Tidak Ditemukan",
        lambda: gedung.keluar("999", 12)
    )

    # 10. Tiket sudah digunakan
    # Pengujian ini dilakukan setelah proses keluar di bawah.


    # ======================================
    # C. SKENARIO BERHASIL KELUAR
    # ======================================

    print("\n========================================")
    print("         PROSES KENDARAAN KELUAR")
    print("========================================")

    biaya_motor = gedung.keluar("1", 10)
    print("Biaya motor: Rp", biaya_motor)

    biaya_mobil = gedung.keluar("2", 11)
    print("Biaya mobil: Rp", biaya_mobil)

    biaya_listrik = gedung.keluar("3", 12)
    print("Biaya mobil listrik: Rp", biaya_listrik)

    # ======================================
    # D. LANJUTAN SKENARIO GAGAL
    # ======================================

    jalankan_skenario(
        "Tiket Sudah Keluar",
        lambda: gedung.keluar("1", 12)
    )

    # ======================================
    # E. STATUS AKHIR PARKIR
    # ======================================

    print("\n========================================")
    print("          STATUS AKHIR PARKIR")
    print("========================================")

    gedung.tampilkan_slot()

    print("\nJumlah kendaraan terdaftar:",
          Motor.jumlah_terdaftar())


if __name__ == "__main__":
    main()
