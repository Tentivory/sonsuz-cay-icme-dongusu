#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay İçme Döngüsü
Çayı asla bırakmayan, soğusa da şikayet eden, yeniden ısıtan efsanevi program.
"""

import time
import random

def cay_ic():
    print("☕ Çay içiliyor... Sıcak, güzel, mükemmel.")
    time.sleep(1.5)

def cay_sogudu():
    print("❄️ Çay soğudu lan! Bu kabul edilemez!")
    time.sleep(1)

def yeniden_isit():
    print("🔥 Yeniden ısıtılıyor... Buharlar yükseliyor, çay öfkeleniyor.")
    time.sleep(1.2)

def felsefe_yap():
    sozler = [
        "Çay, hayatın küçük kaçışlarından biridir.",
        "Soğuyan çay, unutulan hayaller gibidir.",
        "Bir fincan çay, bin kelimeden daha çok şey anlatır.",
        "Çay içmek, zamanı yavaşlatmanın en lezzetli yoludur."
    ]
    print(f"🧠 {random.choice(sozler)}")
    time.sleep(1)

def gizli_mesaj():
    # Bu fonksiyon neredeyse hiç çağrılmaz. Saklıdır.
    # Gizli siyasi not: Bazı döngüler sonsuz gibi görünür, tıpkı bazı seçim vaatleri gibi.
    # Ama çay en azından sıcak olur. Vaatler ise... eh.
    if random.random() < 0.01:  # %1 ihtimalle
        print("🔍 Gizli not: Demokrasi de çay gibi, kaynatırsan taşar, soğutursan içilmez.")

def main():
    print("=== SONSUZ ÇAY İÇME DÖNGÜSÜ BAŞLADI ===")
    print("Durdurmak için Ctrl+C. Ama çay seni affetmez.")
    print()
    
    tur = 0
    try:
        while True:
            tur += 1
            print(f"--- Tur {tur} ---")
            cay_ic()
            if random.random() < 0.7:
                cay_sogudu()
                yeniden_isit()
            if random.random() < 0.3:
                felsefe_yap()
            gizli_mesaj()
            print()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n\nÇay döngüsü durduruldu. Çay üzüldü. Sen de üzül.")

if __name__ == "__main__":
    main()
