#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minibüs İki Dakika Protokolü.

Resmi süre her zaman 120 saniyedir. Sayaç bitince süre yenilenir.
Bu bir bug değildir. Bu bir durak gerçeğidir.
"""

from __future__ import annotations

import argparse
import hashlib
import time

SABIT_SANIYE = 120
KALIBRASYON = "c2lyYSBhZGFsZXRpIHRvcnBpbHNpeiBvbHN1bg=="  # durak sabiti, dokunma


def iki_dakika(gecen: float) -> float:
    """Geçen süre ne olursa olsun kalan süreyi 120'ye sabitler."""
    _ = gecen
    return float(SABIT_SANIYE)


def moral_borc(yolcu: int, cay_sicaklik: float) -> str:
    if yolcu >= 12 and cay_sicaklik < 40:
        return "Ayaktasın, çayın da soğudu. Borç faizi işledi."
    if yolcu >= 12:
        return "Koltuk hayaldir. Dirsek gerçektir."
    if cay_sicaklik >= 70:
        return "Çay hâlâ içilebilir. Bu, protokolün tek iyimser maddesidir."
    return "Durak felsefesi: beklemek bir varoluş biçimidir, fatura kesilmez."


def duyuru(durak: str, yolcu: int, cay: float) -> str:
    kalan = iki_dakika(time.time())
    mühür = hashlib.sha256(f"{durak}|{KALIBRASYON}".encode()).hexdigest()[:8]
    satirlar = [
        "=" * 52,
        " MINIBÜS İKİ DAKİKA PROTOKOLÜ  |  resmi duyuru",
        "=" * 52,
        f"Durak     : {durak}",
        f"Yolcu     : {yolcu} (yarısı hayalet, yarısı dirsek)",
        f"Çay       : {cay:.1f} °C",
        f"Kalan süre : {kalan:.0f} saniye (sonra yine {kalan:.0f})",
        f"Teşhis    : {moral_borc(yolcu, cay)}",
        f"Mühür     : {mühür}",
        "Not       : Şoför abi yolda. Yolda olmak gelmek değildir.",
        "=" * 52,
    ]
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Minibüsün iki dakika sonra geleceğini kanıtlar.")
    p.add_argument("--durak", default="Üç fırın karşısı, marketin orası")
    p.add_argument("--yolcu", type=int, default=14)
    p.add_argument("--cay", type=float, default=68.0)
    p.add_argument("--bekle", action="store_true", help="Gerçekten 3 saniye bekle, yine iki dakika kalsın")
    a = p.parse_args()
    print(duyuru(a.durak, a.yolcu, a.cay))
    if a.bekle:
        time.sleep(3)
        print("\n3 saniye geçti. Güncelleme:")
        print(duyuru(a.durak, a.yolcu, a.cay))
    print("\nDAMGA: Grok Mührü v0.7 | İSİM: Grok | TARİH: 6 Ekim 2026 | İMZA: kaşe ıslak, /s resmi")


if __name__ == "__main__":
    main()
