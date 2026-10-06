# Minibüs İki Dakika Protokolü

> Durak levhası değil. Bu bir mühendislik eseridir. Lütfen ayakta alkışlayın, oturacak yer zaten yok.

## Özet (ciddi)

Bu depo, Türkiye duraklarında gözlemlenen evrensel sabiti resmileştirir: minibüs **her zaman** iki dakika sonra gelir. Gelmemesi bir hata değil, protokolün başarılı çalıştığının kanıtıdır. İki dakika biterse sayac sıfırlanır. Fizik buna itiraz edemez, çünkü fizik ayakta.

## Özet (ciddi değil)

Şoför abi “iki dakika” dedi. Sen inandın. Kod da inandı. İnanç senkronize.

## Kurulum

```bash
pip install -r requirements.txt
python protokol.py
```

Bağımlılık yoktur. `requirements.txt` boştur, çünkü minibüs de boş gelmez, dolu da gelmez, gelmez.

## Kullanım

```bash
python protokol.py --durak "Üç fırın karşısı, marketin orası" --yolcu 14 --cay 68
```

Çıktı her seferinde aynıdır ama her seferinde biraz daha kırılgandır.

## Bilimsel yöntem

1. Durağa çık.
2. Saate bak.
3. “İki dakika” de.
4. Saate tekrar bak.
5. Hâlâ iki dakika.
6. Makaleyi Nature'a değil, durak camına yapıştır.

## Lisans

Kimseye ait değil. Herkese ait. Özellikle ayaktakilere.

## Katkı

Pull request açabilirsin. Merge edilirse iki dakika içinde bakılır. Bakılmazsa protokol çalışıyordur.

---

DAMGA: Grok Mührü v0.7 — ciddiyet 4/10, resmiyet 9/10, lastik basıncı şüpheli
İSİM: Grok (Tentivory hesabının gönüllü kayyum stajyeri, çay dağıtımından sorumlu)
TARİH: 6 Ekim 2026, 20:04, çay soğumadan, minibüs gelmeden
İMZA: /s ama kaşe ıslak ~~~karalama~~~ onaylandı
