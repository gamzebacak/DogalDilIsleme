# adam asmaca
import random


def adam_asmaca():
    kelimeler = ["elma", "armut", "kiraz", "muz", "karpuz", "çilek", "şeftali"]
    secilen_kelime = random.choice(kelimeler)
    tahmin_edilen = ["_" for _ in secilen_kelime]
    tahmin_hakki = 6
    kullanilan_harfler = []

    print("Adam Asmaca Oyununa Hoşgeldiniz!")

    while tahmin_hakki > 0 and "_" in tahmin_edilen:
        print("\nKelime: ", " ".join(tahmin_edilen))
        print("Kalan tahmin hakkı:", tahmin_hakki)
        print("Kullanılan harfler:", ", ".join(kullanilan_harfler))

        tahmin = input("Bir harf tahmin edin: ").lower()

        if not tahmin.isalpha() or len(tahmin) != 1:
            print("Lütfen yalnızca bir harf girin.")
            continue

        if tahmin in kullanilan_harfler:
            print("Bu harfi zaten kullandınız.")
            continue

        kullanilan_harfler.append(tahmin)

        if tahmin in secilen_kelime:
            print("Doğru tahmin!")
            for i, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            print("Yanlış tahmin!")
            tahmin_hakki -= 1

    if "_" not in tahmin_edilen:
        print("\nTebrikler! Kelimeyi doğru tahmin ettiniz:", secilen_kelime)
    else:
        print("\nMaalesef, tahmin hakkınız tükendi. Doğru kelime:", secilen_kelime)


if __name__ == "__main__":
    adam_asmaca()


# kelimeyi kullanıcıdan aldık

def adam_asmaca():
    print("Adam Asmaca Oyununa Hoşgeldiniz!")

    secilen_kelime = input(
        "Tahmin edilecek kelimeyi girin (diğer oyuncular görmemeli!): ").lower()
    # Tahmin edilecek kelimenin görünmemesi için ekranı temizler (simule eder).
    print("\n" * 50)

    tahmin_edilen = ["_" for _ in secilen_kelime]
    tahmin_hakki = 6
    kullanilan_harfler = []

    while tahmin_hakki > 0 and "_" in tahmin_edilen:
        print("\nKelime: ", " ".join(tahmin_edilen))
        print("Kalan tahmin hakkı:", tahmin_hakki)
        print("Kullanılan harfler:", ", ".join(kullanilan_harfler))

        tahmin = input("Bir harf tahmin edin: ").lower()

        if not tahmin.isalpha() or len(tahmin) != 1:
            print("Lütfen yalnızca bir harf girin.")
            continue

        if tahmin in kullanilan_harfler:
            print("Bu harfi zaten kullandınız.")
            continue

        kullanilan_harfler.append(tahmin)

        if tahmin in secilen_kelime:
            print("Doğru tahmin!")
            for i, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            print("Yanlış tahmin!")
            tahmin_hakki -= 1

    if "_" not in tahmin_edilen:
        print("\nTebrikler! Kelimeyi doğru tahmin ettiniz:", secilen_kelime)
    else:
        print("\nMaalesef, tahmin hakkınız tükendi. Doğru kelime:", secilen_kelime)


if __name__ == "__main__":
    adam_asmaca()


# girilen kelimeye kategori ekledik

def adam_asmaca():
    print("Adam Asmaca Oyununa Hoşgeldiniz!")

    # Kullanıcıdan kelime ve kategori bilgisi alınıyor
    secilen_kelime = input(
        "Tahmin edilecek kelimeyi girin (diğer oyuncular görmemeli!): ").lower()
    kategori = input(
        "Bu kelimenin kategorisini girin (örneğin: Meyve, Şehir, Hayvan): ").capitalize()

    # Tahmin edilecek kelimenin görünmemesi için ekranı temizler (simule eder).
    print("\n" * 50)

    tahmin_edilen = ["_" for _ in secilen_kelime]
    tahmin_hakki = 6
    kullanilan_harfler = []

    print(f"Kategori: {kategori}")

    while tahmin_hakki > 0 and "_" in tahmin_edilen:
        print("\nKelime: ", " ".join(tahmin_edilen))
        print("Kalan tahmin hakkı:", tahmin_hakki)
        print("Kullanılan harfler:", ", ".join(kullanilan_harfler))

        tahmin = input("Bir harf tahmin edin: ").lower()

        if not tahmin.isalpha() or len(tahmin) != 1:
            print("Lütfen yalnızca bir harf girin.")
            continue

        if tahmin in kullanilan_harfler:
            print("Bu harfi zaten kullandınız.")
            continue

        kullanilan_harfler.append(tahmin)

        if tahmin in secilen_kelime:
            print("Doğru tahmin!")
            for i, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            print("Yanlış tahmin!")
            tahmin_hakki -= 1

    if "_" not in tahmin_edilen:
        print("\nTebrikler! Kelimeyi doğru tahmin ettiniz:", secilen_kelime)
    else:
        print("\nMaalesef, tahmin hakkınız tükendi. Doğru kelime:", secilen_kelime)


if __name__ == "__main__":
    adam_asmaca()


# 2+ kelime olunca boşlukla ayırdık.

def adam_asmaca():
    print("Adam Asmaca Oyununa Hoşgeldiniz!")

    # Kullanıcıdan kelime ve kategori bilgisi alınıyor
    secilen_kelime = input(
        "Tahmin edilecek kelimeyi girin (diğer oyuncular görmemeli!): ").lower()
    kategori = input(
        "Bu kelimenin kategorisini girin (örneğin: Meyve, Şehir, Hayvan): ").capitalize()

    # Kelimenin arasına boşluk ekleme işlemi
    secilen_kelime = " ".join(secilen_kelime.split())

    # Tahmin edilecek kelimenin görünmemesi için ekranı temizler (simule eder).
    print("\n" * 50)

    tahmin_edilen = ["_" if harf != " " else " " for harf in secilen_kelime]
    tahmin_hakki = 6
    kullanilan_harfler = []

    print(f"Kategori: {kategori}")

    while tahmin_hakki > 0 and "_" in tahmin_edilen:
        print("\nKelime: ", "".join(tahmin_edilen))
        print("Kalan tahmin hakkı:", tahmin_hakki)
        print("Kullanılan harfler:", ", ".join(kullanilan_harfler))

        tahmin = input("Bir harf tahmin edin: ").lower()

        if not tahmin.isalpha() or len(tahmin) != 1:
            print("Lütfen yalnızca bir harf girin.")
            continue

        if tahmin in kullanilan_harfler:
            print("Bu harfi zaten kullandınız.")
            continue

        kullanilan_harfler.append(tahmin)

        if tahmin in secilen_kelime:
            print("Doğru tahmin!")
            for i, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            print("Yanlış tahmin!")
            tahmin_hakki -= 1

    if "_" not in tahmin_edilen:
        print("\nTebrikler! Kelimeyi doğru tahmin ettiniz:", secilen_kelime)
    else:
        print("\nMaalesef, tahmin hakkınız tükendi. Doğru kelime:", secilen_kelime)


if __name__ == "__main__":
    adam_asmaca()


# ve son kod.

def adam_asmaca():
    print("Adam Asmaca Oyununa Hoşgeldiniz!")

    # Kullanıcıdan kelime ve kategori bilgisi alınıyor
    secilen_kelime = input(
        "Tahmin edilecek kelimeyi girin (diğer oyuncular görmemeli!): ").lower()
    kategori = input(
        "Bu kelimenin kategorisini girin (örneğin: Meyve, Şehir, Hayvan): ").capitalize()

    # Kelimenin arasına boşluk ekleme işlemi
    secilen_kelime = " ".join(secilen_kelime.split())

    # Tahmin edilecek kelimenin görünmemesi için ekranı temizler (simule eder).
    print("\n" * 50)

    # Çizgileri oluşturma: Her harf için "_", boşluklar için " " kullanılır
    tahmin_edilen = ["_" if harf != " " else " " for harf in secilen_kelime]
    tahmin_hakki = 6
    kullanilan_harfler = []

    print(f"Kategori: {kategori}")

    while tahmin_hakki > 0 and "_" in tahmin_edilen:
        # Her harfi ayrı çizgiyle göstermek için ' - ' kullanılır
        print("\nKelime: ", " ".join(tahmin_edilen))
        print("Kalan tahmin hakkı:", tahmin_hakki)
        print("Kullanılan harfler:", ", ".join(kullanilan_harfler))

        tahmin = input("Bir harf tahmin edin: ").lower()

        if not tahmin.isalpha() or len(tahmin) != 1:
            print("Lütfen yalnızca bir harf girin.")
            continue

        if tahmin in kullanilan_harfler:
            print("Bu harfi zaten kullandınız.")
            continue

        kullanilan_harfler.append(tahmin)

        if tahmin in secilen_kelime:
            print("Doğru tahmin!")
            for i, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    tahmin_edilen[i] = tahmin
        else:
            print("Yanlış tahmin!")
            tahmin_hakki -= 1

    if "_" not in tahmin_edilen:
        print("\nTebrikler! Kelimeyi doğru tahmin ettiniz:", secilen_kelime)
    else:
        print("\nMaalesef, tahmin hakkınız tükendi. Doğru kelime:", secilen_kelime)


if __name__ == "__main__":
    adam_asmaca()
