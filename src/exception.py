
class ParkirError(Exception):
    """Exception dasar untuk seluruh kesalahan sistem parkir."""

    def __init__(self, message, **context):
        super().__init__(message)
        self.context = context

    def __str__(self):
        if not self.context:
            return super().__str__()

        detail = ", ".join(
            f"{key}={value}" for key, value in self.context.items()
        )
        return f"{super().__str__()} ({detail})"


class PlatNomorTidakValidError(ParkirError):
    """Plat nomor kendaraan tidak memenuhi ketentuan."""


class TarifTidakValidError(ParkirError):
    """Tarif parkir tidak valid."""


class ParkirPenuhError(ParkirError):
    """Tidak tersedia slot parkir yang sesuai."""


class JenisSlotTidakSesuaiError(ParkirError):
    """Jenis kendaraan tidak sesuai dengan slot."""


class JenisSlotTidakValidError(ParkirError):
    """Jenis slot tidak dikenali."""


class KendaraanTidakDidukungError(ParkirError):
    """Objek kendaraan tidak didukung sistem."""


class KendaraanSudahParkirError(ParkirError):
    """Kendaraan masih memiliki tiket parkir aktif."""


class TiketTidakDitemukanError(ParkirError):
    """ID tiket tidak ditemukan."""


class TiketSudahKeluarError(ParkirError):
    """Tiket sudah digunakan untuk proses keluar."""


class WaktuTidakValidError(ParkirError):
    """Waktu masuk atau keluar tidak valid."""
