# exceptions.py

class ParkirError(Exception):
    """Exception dasar untuk seluruh kesalahan pada sistem parkir."""

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
    pass


class TarifTidakValidError(ParkirError):
    pass


class ParkirPenuhError(ParkirError):
    pass


class JenisSlotTidakSesuaiError(ParkirError):
    pass


class JenisSlotTidakValidError(ParkirError):
    pass


class KendaraanTidakDidukungError(ParkirError):
    pass


class KendaraanSudahParkirError(ParkirError):
    pass


class TiketTidakDitemukanError(ParkirError):
    pass


class TiketSudahKeluarError(ParkirError):
    pass


class WaktuTidakValidError(ParkirError):
    pass
