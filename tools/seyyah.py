#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧭 Âyet-ül Kübra Seyyahı - Terminal Tabanlı Tefekkür, Araştırma ve Quiz Aracı
Yazar: @dijital-seyyah
"""

import sys
import os
import json
import random
import argparse

# Windows konsolunda UTF-8 çıktı desteğini sağla
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'mertebeler.json')

def load_data():
    if not os.path.exists(DATA_PATH):
        print(f"HATA: Veri dosyası bulunamadı: {DATA_PATH}")
        sys.exit(1)
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def cmd_list(args):
    data = load_data()
    print("=" * 80)
    print("🌌 ÂYET-ÜL KÜBRA: SEYYAHIN 33 TEVHİD DURAĞI")
    print("=" * 80)
    current_makam = None
    for m in data['mertebeler']:
        if m['makam'] != current_makam:
            current_makam = m['makam']
            print(f"\n📂 [{current_makam.upper()}]")
            print("-" * 80)
        print(f"  [{m['id']:02d}] {m['baslik']:<34} | {m['kategori']:<24}")
    print("\nDetayları incelemek için: python tools/seyyah.py show <no>")

def cmd_show(args):
    data = load_data()
    m_id = args.id
    match = next((m for m in data['mertebeler'] if m['id'] == m_id), None)
    if not match:
        print(f"HATA: {m_id} numaralı durak bulunamadı (1 - 33 arası giriniz).")
        return

    print("=" * 80)
    print(f"🧭 DURAK #{match['id']:02d}: {match['baslik'].upper()}")
    print("=" * 80)
    print(f"📌 Makam              : {match['makam']} (Mertebe #{match['mertebe_no']})")
    print(f"🏷️  Kategori           : {match['kategori']}")
    print(f"📖 Âyet Referansı     : {match['ayet_referansi']}")
    print(f"🔬 Modern Bilim Bağı  : {match['modern_bilim']}")
    print(f"✨ Tecelli Eden Esmâ  : {', '.join(match['esma'])}")
    print(f"📄 İlgili Dosya       : {match.get('dosya', 'Belirtilmedi')}")
    print("-" * 80)
    print("💡 TEMEL TEVHİD DELİLİ:")
    print(f"   \"{match['temel_delil']}\"")
    print("=" * 80)

def cmd_search(args):
    data = load_data()
    q = args.kelime.lower()
    print(f"🔍 '{args.kelime}' terimi için araştırma sonuçları:\n")
    results = []
    for m in data['mertebeler']:
        text_corpus = f"{m['baslik']} {m['temel_delil']} {m['kategori']} {m['modern_bilim']} {' '.join(m['esma'])} {m['ayet_referansi']}".lower()
        if q in text_corpus:
            results.append(m)

    if not results:
        print("❌ Eşleşen bir durak veya kavram bulunamadı.")
        return

    for r in results:
        print(f"  • [#{r['id']:02d}] {r['baslik']} ({r['kategori']})")
        print(f"    Delil: {r['temel_delil']}")
        print(f"    Esmâ : {', '.join(r['esma'])}\n")
    print(f"Toplam {len(results)} durakta bulundu.")

def cmd_random(args):
    data = load_data()
    m = random.choice(data['mertebeler'])
    print("=" * 80)
    print("🌟 GÜNÜN TEFEKKÜR DURAĞI")
    print("=" * 80)
    print(f"🧭 Durak #{m['id']:02d}: {m['baslik']}")
    print(f"📖 Âyet: {m['ayet_referansi']}")
    print(f"\n💬 \"{m['temel_delil']}\"")
    print(f"\n🔬 Bilimsel İzdüşüm: {m['modern_bilim']}")
    print(f"✨ Tecelli Eden Esmâ: {', '.join(m['esma'])}")
    print("=" * 80)
    print("💡 Tefekkür Sorusu: Bu hakikati bugün çevrendeki hangi olay veya varlıkta müşahede ettin?")

def cmd_stats(args):
    data = load_data()
    mertebeler = data['mertebeler']
    kategoriler = {}
    esmalar = set()
    for m in mertebeler:
        k = m['kategori']
        kategoriler[k] = kategoriler.get(k, 0) + 1
        for e in m['esma']:
            esmalar.add(e)

    print("=" * 65)
    print("📊 ÂYET-ÜL KÜBRA ARAŞTIRMALARI - İSTATİSTİKLER")
    print("=" * 65)
    print(f"Toplam Durak Sayısı : {len(mertebeler)}")
    print(f"Farklı Esmâ Sayısı  : {len(esmalar)}")
    print("\nKategori Dağılımı:")
    for kat, sayi in kategoriler.items():
        bar = "█" * (sayi * 2)
        print(f"  {kat:<32} : {sayi:02d} {bar}")
    print("=" * 65)

def cmd_quiz(args):
    data = load_data()
    mertebeler = data['mertebeler']
    adet = min(args.sayi, len(mertebeler))
    secilenler = random.sample(mertebeler, adet)

    print("=" * 80)
    print(f"🎯 ÂYET-ÜL KÜBRA TEFEKKÜR QUIZI ({adet} Soru)")
    print("=" * 80)

    puan = 0
    sorular = []
    for idx, dogru_m in enumerate(secilenler, 1):
        # 3 yanlış şık seç
        digerleri = [m for m in mertebeler if m['id'] != dogru_m['id']]
        yanlislar = random.sample(digerleri, 3)
        siklar = yanlislar + [dogru_m]
        random.shuffle(siklar)

        dogru_harf = chr(ord('A') + siklar.index(dogru_m))
        soru_metni = (
            f"\nSoru {idx}: Aşağıdaki temel tevhid delili hangi mertebeye aittir?\n"
            f"   \"{dogru_m['temel_delil']}\"\n"
        )
        for i, sik in enumerate(siklar):
            harf = chr(ord('A') + i)
            soru_metni += f"   [{harf}] {sik['baslik']} ({sik['kategori']})\n"
        
        sorular.append({
            'soru': soru_metni,
            'dogru': dogru_harf,
            'mertebe': dogru_m
        })

    if args.auto:
        # Otomatik test / CI modu
        print("Otomatik doğrulama modu devrede:")
        for s in sorular:
            print(s['soru'])
            print(f"Doğru Cevap: [{s['dogru']}] - {s['mertebe']['baslik']}")
        print("\n✅ Quiz motoru başarıyla çalıştırıldı.")
        return

    for idx, s in enumerate(sorular, 1):
        print(s['soru'])
        cevap = input("Cevabınız (A/B/C/D): ").strip().upper()
        if cevap == s['dogru']:
            print("🎉 TEBRİKLER! Doğru cevap.")
            puan += 1
        else:
            print(f"❌ Yanlış. Doğru cevap [{s['dogru']}] - {s['mertebe']['baslik']} olmalıydı.")
            print(f"   İlgili Âyet: {s['mertebe']['ayet_referansi']}")

    print("\n" + "=" * 80)
    print(f"🏁 Quiz Tamamlandı! Toplam Puanınız: {puan} / {adet}")
    print("=" * 80)

def cmd_export(args):
    data = load_data()
    cikti = []
    cikti.append("# 📋 Âyet-ül Kübra 33 Mertebe Tefekkür Tablosu\n")
    cikti.append("| ID | Makam | Başlık | Kategori | Temel Delil | Modern Bilim |")
    cikti.append("|:---:|:---|:---|:---|:---|:---|")
    for m in data['mertebeler']:
        cikti.append(f"| {m['id']:02d} | {m['makam']} | **{m['baslik']}** | {m['kategori']} | {m['temel_delil']} | {m['modern_bilim']} |")
    
    tablo_str = "\n".join(cikti)
    if args.dosya:
        with open(args.dosya, 'w', encoding='utf-8') as f:
            f.write(tablo_str)
        print(f"✅ Tablo başarıyla dışa aktarıldı: {args.dosya}")
    else:
        print(tablo_str)

def main():
    parser = argparse.ArgumentParser(
        description="Âyet-ül Kübra Araştırmaları - Dijital Seyyah Terminal Kılavuzu"
    )
    subparsers = parser.add_subparsers(dest='command', help='Komutlar')

    subparsers.add_parser('list', help='33 durağın tamamını listeler')
    
    show_parser = subparsers.add_parser('show', help='Belirli bir durağın detaylarını görüntüler')
    show_parser.add_argument('id', type=int, help='Durak ID numarası (1-33)')

    search_parser = subparsers.add_parser('search', help='Duraklar ve deliller içinde arama yapar')
    search_parser.add_argument('kelime', type=str, help='Aranacak kelime veya kavram')

    subparsers.add_parser('gunun-tefekkuru', help='Rastgele bir tefekkür durağı getirir')
    subparsers.add_parser('stats', help='Genel istatistikleri gösterir')

    quiz_parser = subparsers.add_parser('quiz', help='İnteraktif tefekkür testi başlatır')
    quiz_parser.add_argument('-n', '--sayi', type=int, default=5, help='Soru sayısı (varsayılan: 5)')
    quiz_parser.add_argument('--auto', action='store_true', help='Otomatik test / CI modunda çalıştır')

    export_parser = subparsers.add_parser('export', help='Markdown tablosu olarak dışa aktarır')
    export_parser.add_argument('-o', '--dosya', type=str, default=None, help='Kaydedilecek dosya yolu (opsiyonel)')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'list': cmd_list,
        'show': cmd_show,
        'search': cmd_search,
        'gunun-tefekkuru': cmd_random,
        'stats': cmd_stats,
        'quiz': cmd_quiz,
        'export': cmd_export
    }
    commands[args.command](args)

if __name__ == '__main__':
    main()
