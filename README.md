# 🌌 Âyet-ül Kübra Araştırmaları

> *"Kâinattan Hâlıkını soran bir seyyahın müşahedatıdır."*
> 
> *"Evet, bu dünya memleketine ve misafirhanesine gelen herbir misafir, gözünü açıp baktıkça görür ki: Gayet keremkârâne bir ziyafetgâh ve gayet san'atkârâne bir teşhirgâh ve gayet haşmetperverâne bir ordugâh... olan bu güzel misafirhanenin sâhibini ve bu kitab-ı kebirin müellifini tanımak ve bilmek için kendi kendine sorar."*
> — **Bediüzzaman Said Nursi, Risale-i Nur Külliyatı, 7. Şua**

[![Lisans: CC BY-SA 4.0](https://img.shields.io/badge/Lisans-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
[![CI Doğrulama](https://github.com/dijital-seyyah/Ayetul-Kubra-Arastirmalari/actions/workflows/ci.yml/badge.svg)](https://github.com/dijital-seyyah/Ayetul-Kubra-Arastirmalari/actions)
[![Kategori](https://img.shields.io/badge/Alan-Kelâm%20%7C%20Ontoloji%20%7C%20Kozmoloji-blue)](https://github.com/dijital-seyyah/Ayetul-Kubra-Arastirmalari)
[![Web Platformu](https://img.shields.io/badge/Web-İnteraktif%20Dashboard-6366f1)](https://dijital-seyyah.github.io/Ayetul-Kubra-Arastirmalari/)
[![Duraklar](https://img.shields.io/badge/Duraklar-33%20Mertebe%20Eksiksiz-brightgreen)](#-seyyahın-33-durağı-kâinatın-tevhid-şehadeti)

---

## 📌 Proje Vizyonu ve Amacı

Bu araştırma külliyatı (`Ayetul-Kubra-Arastirmalari`), Bediüzzaman Said Nursi'nin Kastamonu hayatı döneminde telif ettiği, İslâm düşünce ve kelâm tarihinin en kapsamlı tevhid ispatlarından biri olan **7. Şua (Âyet-ül Kübra)** risalesini çok boyutlu, analitik, felsefi ve modern bilimsel verilerle (astrofizik, kuantum ontolojisi, moleküler biyoloji, enformasyon teorisi) mezcederek incelemek üzere kurulmuştur.

Eser, ismini Kur'an-ı Kerim'deki (Necm, 18 & Nâziât, 20) *"Andolsun ki o, Rabbinin en büyük âyetlerinden (Âyet-ül Kübra) bir kısmını gördü"* mealindeki ilahi beyandan ve Hz. Peygamber'in (asm) Mi'rac yolculuğunda kâinatın sırlarını temaşa etmesinden mülhemdir. 

Biz de bu dijital araştırma havuzunda, kâinatı satır satır okuyan o fıtrî "seyyahın" tefekkür adımlarını takip ediyor; atom altı parçacıklardan galaksi kümelerine, DNA zincirlerinden melekût âlemine kadar **33 ayrı varlık mertebesinin** şahitliğini hem metinsel, hem makinece okunabilir veri tabanı (JSON), hem terminal aracı (CLI), hem de tarayıcı üzerinden çalışan **interaktif modern web platformu** (`index.html`) ile kayıt altına alıyoruz.

---

## 📑 İçindekiler Tablosu

1. [Proje Vizyonu ve Amacı](#-proje-vizyonu-ve-amacı)
2. [🌐 İnteraktif Web Platformu (`index.html`)](#-i̇nteraktif-web-platformu-indexhtml)
3. [🧭 Seyyah CLI Aracı (Terminal Kılavuzu & Quiz)](#-seyyah-cli-aracı-terminal-kılavuzu--quiz)
4. [Seyyahın 33 Durağı: Kâinatın Tevhid Şehadeti](#-seyyahın-33-durağı-kâinatın-tevhid-şehadeti)
5. [Kavramsal Harita ve Terminoloji](#-kavramsal-harita-ve-terminoloji)
6. [Kitabın Kalbinden Vurucu Alıntılar](#-kitabın-kalbinden-vurucu-alıntılar)
7. [Repozitori Mimarisi ve Dosya Düzeni](#-repozitori-mimarisi-ve-dosya-düzeni)
8. [Araştırma ve Katkı Metodolojisi](#-araştırma-ve-katkı-metodolojisi)
9. [Katkıda Bulunanlar ve Lisans](#-katkıda-bulunanlar-ve-lisans)

---

## 🌐 İnteraktif Web Platformu (`index.html`)

Depo kökünde yer alan [`index.html`](index.html) dosyası; sıfır bağımlılıkla çalışan, karanlık/aydınlık tema destekli, mobil ve masaüstü uyumlu eksiksiz bir web uygulamasıdır:

* **Canlı Filtreleme & Arama:** 33 mertebeyi Makam (Birinci/İkinci), Kategori veya serbest metin aramasıyla anında filtreleyin.
* **Tefekkür Kartları & Detay Modal:** Her durağın ayet referansını, temel kelâmî delilini, tecelli eden esmâlarını ve modern bilim bağını tek tıkla inceleyin.
* **Günün Tefekkürü:** Her gün rastgele bir tefekkür durağı ve derin düşünme sorusu getiren interaktif araç.
* **İnteraktif Tefekkür Testi (Quiz):** Tarayıcı üzerinde 5 soruluk dinamik test motoru ile bilginizi ölçün ve skorunuzu görün.
* **GitHub Pages Uyumu:** Herhangi bir derleme (build) sürecine ihtiyaç duymadan GitHub Pages üzerinde doğrudan canlı olarak çalışır.

---

## 🧭 Seyyah CLI Aracı (Terminal Kılavuzu & Quiz)

Proje bünyesinde geliştirilen `tools/seyyah.py` aracı ile 33 tevhid durağını terminal üzerinden keşfedebilirsiniz:

```bash
# 33 mertebenin özet tablosunu listele
python tools/seyyah.py list

# Belirli bir durağın ayrıntılı analizini görüntüle (Örn: 1. veya 33. durak)
python tools/seyyah.py show 1
python tools/seyyah.py show 33

# Anahtar kelime veya esma araması yap (Örn: kuantum, rızık, nizam, DNA)
python tools/seyyah.py search "nizam"

# Günün tefekkür durağını ve sorusunu getir
python tools/seyyah.py gunun-tefekkuru

# Kategori ve esmâ istatistiklerini grafik olarak incele
python tools/seyyah.py stats

# İnteraktif terminal quizini başlat (Örn: 5 soru)
python tools/seyyah.py quiz -n 5

# Tüm mertebeleri Markdown tablosu olarak dışa aktar
python tools/seyyah.py export -o mertebeler_tablosu.md
```

---

## 🧭 Seyyahın 33 Durağı: Kâinatın Tevhid Şehadeti

Âyet-ül Kübra, kâinatı birbirinden kopuk parçalar olarak değil; muazzam bir dayanışma (**tesanüd**), kucaklaşma (**teânuk**), yardımlaşma (**teavün**) ve cevaplaşma (**tecavüb**) ağıyla örülmüş tek bir canlı saray veya fabrika gibi ele alır.

| Bölüm / Makam | Kapsadığı Mertebeler (Duraklar) | Araştırma Odak Noktası (Tefekkür) |
| :--- | :--- | :--- |
| **1. Kozmik ve Âfâkî Âlem** | Gökyüzü (Semavat), Atmosfer (Cevv-i Sema), Yeryüzü (Arz), Denizler ve Nehirler, Dağlar ve Sahralar | Astrofiziksel hassas ayarlar (fine-tuning), kütleçekim, atmosferik döngüler, hidrosfer ve jeolojik sükûnet. |
| **2. Biyolojik ve Organik Âlem** | Bitkiler (Nebatat), Hayvanat ve Kuşlar, Canlılık (Zevilhayat), Hücre ve DNA | DNA kodlarındaki kader programı, rızık taksimatı, Rezzâkıyet, entropiye karşı canlılık (negentropy). |
| **3. Şuurlu Şahitler (İnsanlık)** | İnsan Fıtratı (Ene Aynası), Peygamberler (Enbiya), Tahkik Ehli Âlimler (Asfiya), Evliya ve Ârifler | Bilinç felsefesi, vahid-i kıyasî, enbiyanın tevatür derecesindeki ittifakı ve evliyanın keşf-i şuhud tecrübesi. |
| **4. Gayb ve Melekût Âlemi** | Melekler (Melaike), Akl-ı Selim ve Fıtrî Vicdan, Vahiy ve Sadık İlhamlar | Metafizik boyut, vicdandaki nokta-i istinad ve istimdad pusulası, gaybî haberleşme ontolojisi. |
| **5. Risalet ve Vahiy Zirvesi** | Hz. Muhammed (asm), Kur'an-ı Mu'ciz-ül Beyan, Kâinatın Heyet-i Mecmuası | Risalet-i Ahmediye'nin bin mucizesi, Kur'an'ın ebedi i'cazı ve kâinatın bütününde parlayan "Samediyet" sikkesi. |
| **6. İkinci Makam (14 Tevhid Hücceti)** | Uluhiyet, Rububiyet, Kayyûmiyet, Ferdiyet, Kudret, İlim, İrade, Hikmet, Rahmet, Adalet, Kudsiyet, Fettâhiyet, İkram, Tevhid-i Zâtî | Esmâ-i Hüsnâ ufkundan kâinatın tümel tahlili, şirkin mantıksal imkânsızlığı (Burhan-ı Temânu'). |

---

## 🧠 Kavramsal Harita ve Terminoloji

Eserin anahtar kavramları projenin `/03_Kavram_Sozlugu` dizininde felsefi ve lügat tahlilleriyle ele alınmıştır:

* **Mânâ-yı Harfî vs. Mânâ-yı İsmî:** Varlığa maddesi cihetiyle değil, Sanatkârını gösteren bir ayna ve mektup nazarıyla bakma epistemolojisi.
* **Vücûb-u Vücûd (Vâcib-ül Vücûd):** Varlığı zâtî olan, yokluğu muhal bulunan, hiçbir sebebe ve zamana muhtaç olmayan mutlak Vacib Teâlâ.
* **Vahdet ve Ehadiyet:** Bütün kâinatı kuşatan mutlak birlik (Vâhidiyet) ile en küçük zerrede tüm esmâ-i hüsnânın odaklanması (Ehadiyet).
* **Tesanüd, Teavün ve Teânuk:** Cansız unsurların tek bir canlının yaşaması için şuurlu gibi el ele verip kucaklaşmaları sırrı.
* **İmkân ve Hudûs Delilleri:** Mevcudatın var olma veya yok olma noktasında eşitken sonradan varlık sahasına çıkması mantığı.
* **Teceddüd-ü Emsâl:** Kâinatın her an kuantum seviyesinde yeniden yaratılması ve tazelenmesi hakikati.
* **Kayyûmiyet:** Varlık ağacının her salise ilahi kudretle ayakta tutulması, deizmin çürütülmesi.
* **Burhân-ı Temânu':** Çok ilahlılığın mantıksal ve ontolojik imkânsızlığı.

---

## 📂 Repozitori Mimarisi ve Dosya Düzeni

```text
📁 Ayetul-Kubra-Arastirmalari
├── 📄 index.html                           # İnteraktif modern web platformu ve dashboard
├── 📄 README.md                            # Ana rehber ve vizyon belgesi
├── 📄 CONTRIBUTORS.md                      # Araştırmaya katkı sunan mütefekkirler
├── 📄 LICENSE                              # CC BY-SA 4.0 Lisans belgesi
├── 📄 .gitignore                           # Git izleme dışı dosyalar
├── 📁 .github/workflows/ci.yml             # Otomatik veri, kod ve link doğrulama iş akışı
├── 📁 data/
│   └── mertebeler.json                     # 33 mertebenin makinece okunabilir veri tabanı
├── 📁 tools/
│   └── seyyah.py                           # İnteraktif terminal kılavuzu, arama ve quiz aracı
├── 📁 00_Mukaddime_Analizi/                # Epistemoloji ve şirk mantığının çöküşü
│   ├── mukaddime_ve_metodoloji.md          # 4 kaide, seyyahın zihin dünyası ve delil yöntemi
│   └── vahdaniyet_ve_sirkin_muhaliyeti.md  # Tevhidin zarureti ve tesadüfün imkânsızlığı
├── 📁 01_Makro_Alem_Delilleri/             # Astrofizik, jeoloji ve atmosfer
│   ├── semavat_ve_yildizlar.md             # 1. Mertebe: Gökyüzü, kütleçekim ve kozmik nizam
│   ├── cevv-i_sema_ve_bulutlar.md          # 2. Mertebe: Atmosfer, rüzgârlar ve rahmet
│   ├── arz_ve_denizler.md                  # 3. & 4. Mertebe: Dünya beşiği ve denizler
│   └── daglar_ve_sahralar.md               # 5. Mertebe: Jeolojik kazıklar (evtâd)
├── 📁 02_Mikro_Alem_Delilleri/             # Biyoloji, botanik, zooloji ve genetik
│   ├── nebatat_ve_cekirdekler.md           # 6. Mertebe: Çekirdek programı ve fotosentez
│   ├── hayvanat_ve_rizik_mizani.md         # 7. Mertebe: Zooloji, sevk-i ilahi ve şefkat
│   ├── hayat_ve_zevilhayat.md              # 8. & 9. Mertebe: Hayat hakikati ve negentropy
│   └── hucre_ve_dna_mizanlari.md           # Hücre biyolojisi ve enformasyon ontolojisi
├── 📁 03_Suurlu_ve_Gaybi_Alem/             # İnsan, nübüvvet, melekût ve iç âlem
│   ├── insan_ve_ene_aynasi.md              # 10. Mertebe: İnsan fıtratı ve cami mazhariyet
│   ├── enbiya_ve_mucizeler.md              # 11. Mertebe: Peygamberlerin ittifakı
│   ├── asfiya_ve_muhakkikler.md            # 12. Mertebe: Tahkik ehli dâhiler ve burhanlar
│   ├── evliya_ve_arPath_ehli.md            # 13. Mertebe: Kalp gözü ve keşf-i şuhud
│   ├── melaike_ve_ruhaniyat.md             # 14. Mertebe: Melekût âlemi ve kozmik zabıtlar
│   ├── akil_kalp_ve_vicdan.md              # 15. Mertebe: İç pusula ve fıtrî vicdan
│   └── vahiy_ve_sadik_ilhamlar.md          # 16. Mertebe: Gaybî haberleşme ve ilham
├── 📁 04_Risalet_ve_Kuran/                 # Zirve şahitler: Peygamber ve Semavi Kitap
│   ├── risalet-i_ahmediye.md               # 17. Mertebe: Hz. Muhammed asm'ın şahitliği
│   └── kuran-i_mucizul_beyan.md            # 18. & 19. Mertebe: Kur'an'ın i'cazı ve heyet-i mecmua
├── 📁 05_Ikinci_Makam_Tevhid_Huccetleri/   # İkinci Bab: 14 Tevhid ve Esmâ Hücceti
│   ├── ikinci_bab_ve_14_burhan.md          # 14 hüccetin mantıkî mimarisi ve esmâ tecellileri
│   └── vahdet_ve_uluhiyet_burhanlari.md    # Uluhiyet, Rububiyet ve Kayyûmiyet şerhi
├── 📁 06_Ayetler_ve_Huccetler/             # Metin, dilbilim ve tefsir tahlilleri
│   ├── arapca_huccetler_ve_tercumeleri.md  # 33 durak hüccetinin orijinal Arapça metinleri ve şerhi
│   └── kurani_referanslar_ve_tefsir_notlari.md # 33 mertebenin Kur'ânî dayanakları ve tefsir notları
├── 📁 03_Kavram_Sozlugu/                   # Felsefi, kelami ve tasavvufi kavramlar
│   ├── mana-yi_harfi.md                    # Mana-yı Harfi vs. Mana-yı İsmi
│   ├── hudus_ve_imkan.md                   # Kozmolojik ve ontolojik imkân delilleri
│   ├── vahdet_ve_ehadiyet.md               # Vâhidiyet ve Ehadiyet arasındaki farklar
│   ├── tesanud_ve_teavun.md                # Kâinattaki kozmik dayanışma nizamı
│   ├── vucub-u_vucud.md                    # Vâcibü'l-Vücûd ve zâtî vücud
│   ├── teceddud-u_emsal.md                 # Sürekli yaratılış ve yenilenme
│   ├── kayyumiyet.md                       # Varlık ağacının ayakta tutulması
│   └── burhan-i_temanu.md                  # Çok ilahlılığın mantıksal imkânsızlığı
├── 📁 04_Muzakere_ve_Makaleler/            # Akademik araştırmalar ve özgün makaleler
│   ├── dijital-seyyah_Kozmik_Tesanud_ve_Modern_Fizik.md   # Astrofizik ve Âyet-ül Kübra sentezi
│   ├── dijital-seyyah_Kuantum_Ontolojisi_ve_Ayetul_Kubra.md # Kuantum fiziği ve Mânâ-yı Harfî
│   ├── dijital-seyyah_Biyolojik_Tasarim_ve_Teleoloji.md   # Moleküler motorlar ve teleoloji
│   ├── klasik_kelam_ve_ayetul_kubra_mukayesesi.md         # Mütekellimîn vs. Kur'ânî burhan
│   └── sehadet_mertebeleri_sistematigi.md  # 33 mertebenin tam hiyerarşik haritası
└── 📁 05_Ek_Materyaller/                   # Görselleştirmeler ve çalışma rehberleri
    ├── zihin_haritasi_33_mertebe.md        # 33 mertebenin akış şeması (Mermaid)
    └── ayetul_kubra_okuma_rehberi.md       # Mütalaa halkaları için 6 haftalık ders planı
```

---

## 🔬 Araştırma ve Katkı Metodolojisi

Bu depoya katkı sağlamak, kuru bir metin aktarımı değil; **asırlık bir şaheseri 21. yüzyılın idrak ve diliyle yeniden tefekkür etmektir.**

1. **Modern Bilimle Sentez:** James Webb Uzay Teleskobu verileri, kuantum dolaşıklığı, epigenetik mekanizmalar ve biyosfer döngülerini metindeki nükte ve işaretlerle buluşturabilirsiniz.
2. **Kavramsal Derinlik:** Sözlük bölümündeki ıstılahları, İslam Kelâmı (Gazzâlî, Râzî, Taftâzânî) ve Batı Felsefesi (Kant, Leibniz, Spinoza, Plantinga) karşılaştırmalarıyla zenginleştirebilirsiniz.
3. **Mütalaa Masası:** GitHub Discussions ve Issues alanlarını sanal bir ilim meclisi olarak kullanıp müzakerelere katılabilirsiniz.

> **Parola:** *"Ey kâinatın yolcusu! Okuduğun bu kitap, seni kâtibine götürsün."*

---

## 👥 Katkıda Bulunanlar ve Lisans

Bu proje açık tefekkür ve ilim anlayışıyla [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](LICENSE) lisansı altında neşredilmektedir.

Katkıda bulunanlar listesi ve kurallar için [CONTRIBUTORS.md](CONTRIBUTORS.md) dosyasını inceleyebilirsiniz.
