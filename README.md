# Ezventure

Game petualangan RPG 3D bergaya voxel, **co-op sampai 3 pemain**, dibuat supaya bisa dimainkan bareng anak kecil (usia 5 tahun ke atas). Seluruh game ada di **satu file HTML** (`index.html`), jalan di browser HP maupun desktop, bisa di-install sebagai PWA, tanpa server game dan tanpa login.

**Main sekarang:** https://sikhsanf.github.io/ezventure/

> Dunia **Terra** diganggu oleh Prof. Zarko dan Zat Mutan buatannya yang bikin hewan dan tanaman jadi sakit dan berubah. Pilih profesi, naik level, jelajahi kota dan lapangan, kalahkan monster, dan bantu Terra pulih.

---

## Daftar isi

1. [Fitur utama](#fitur-utama)
2. [Cara main](#cara-main)
3. [Profesi dan kelas lanjutan](#profesi-dan-kelas-lanjutan)
4. [Dunia Terra](#dunia-terra)
5. [Sistem game](#sistem-game)
6. [Co-op](#co-op)
7. [Bahasa dan aksesibilitas](#bahasa-dan-aksesibilitas)
8. [Arsitektur teknis](#arsitektur-teknis)
9. [Build, test, dan deploy](#build-test-dan-deploy)
10. [Struktur repo](#struktur-repo)
11. [Prinsip desain](#prinsip-desain)
12. [Batasan dan rencana](#batasan-dan-rencana)

---

## Fitur utama

- **6 profesi** dengan kota, senjata, armor, dan skill sendiri.
- **Kenaikan kelas di Lv 10** lewat ujian di markas, tiap profesi pecah jadi 2 jalur dengan skill dan visual berbeda.
- **Dunia terbuka berpetak**: 6 kota, 19 lapangan (monster Lv 1–25), peta dunia, portal antar-area, dan balon udara untuk perjalanan jauh.
- **Co-op online 3 pemain** lewat peer-to-peer (WebRTC), dengan reconnect otomatis kalau koneksi putus sebentar.
- **Pet** per kota (jalan bareng, kasih bonus, dan menyerang monster agresif secara otomatis).
- **Misi harian** di Pusat Misi, reset tiap tengah malam, dengan kartu berwarna menurut tingkat kesulitan.
- **Siklus siang/malam dan cuaca acak**, dengan monster dan bos yang berbeda.
- **Efek visual per skill** yang mengikuti nama skill (drone beneran muncul, tembok perisai, tombak gempa, dan seterusnya).
- **Toko equipment** dengan pratinjau 3D senjata dan armor.
- **Simpan otomatis** di perangkat (localStorage), dengan beberapa slot karakter.
- **Dua bahasa**: Indonesia dan Inggris.

## Cara main

1. Buka tautan game, tekan **Main**, pilih slot, pilih profesi, atur penampilan, beri nama.
2. Ikuti tutorial di Kamp Pelatihan. Panah penunjuk misi akan memandu ke tujuan.
3. **Gerak**: joystick (HP) atau kontrol layar. **Serang**: tombol serang, **tahan** untuk menyerang terus-menerus. **Skill**: tombol skill di samping.
4. Ambil misi di Pusat Misi kota, kalahkan monster, kumpulkan koin dan XP, lalu belanja equipment.
5. Di Lv 10, temui Ketua di markas untuk ujian kenaikan kelas.

## Profesi dan kelas lanjutan

| Profesi | Kota | Jalur lanjutan (Lv 10) |
|---|---|---|
| Ksatria / Warrior | Benteng Besi (Ironhold) | **Ksatria**, **Pendekar Amuk** |
| Ilmuwan (Mage) | Menara Bintang (Starspire) | **Ahli Kimia**, **Ahli Listrik** |
| Pemanah (Ranger) | Pondok Daun (Leafhaven) | **Pemanah Jitu**, **Pemanah Angin** |
| Dokter | Kali Sehat (Healbrook) | **Dokter Spesialis**, **Dokter Herbal** |
| Ahli Kayu | Roda Kayu (Cogwood) | **Ahli Besi**, **Ahli Robot** |
| Ahli Bela Diri | Bukit Zen (Zenridge) | **Ahli Pukulan**, **Ahli Tendangan** |

- Tiap profesi punya **3 skill**. Setelah lulus ujian, skill diganti set skill jalur lanjutan.
- Jalur dipilih langsung di depan ketua markas, lengkap dengan cutscene perbandingan. Pindah jalur boleh, tapi harus ujian ulang.
- Senjata tier 6–10 dan armor baru hanya untuk kelas lanjutan.
- Karakter bersenjata dua tangan (bela diri, solder + gergaji, dan lainnya) menyerang **kanan-kiri bergantian**; tiap tangan memberi setengah damage sehingga serangan terasa lebih cepat.
- Bela diri memakai animasi **pukulan**; Ahli Tendangan memakai **tendangan**.

## Dunia Terra

**Kota** (masing-masing punya markas, toko, peternakan pet, Pusat Misi, dan portal): Benteng Besi, Menara Bintang, Pondok Daun, Kali Sehat, Roda Kayu, Bukit Zen.

**Lapangan**: Kamp Pelatihan, Padang Surya, Bukit Batu, Hutan Jamur, Lembah Bintang, Kawah Bara, Rawa Berkabut, Puncak Beku, Sarang Naga, Padang Mint, Telaga Teratai, Rimba Papan, Tambang Serbuk, Jalur Bambu, Dojo Air Terjun.

**Area tingkat tinggi (Lv 16–25)**, dirancang untuk main bareng karena batas level karakter masih Lv 15:

| Area | Level monster | Akses |
|---|---|---|
| Padang Aurora | 16–20 | utara Puncak Beku |
| Pulau Awan | 16–20 | utara Sarang Naga |
| Gua Kristal Pelangi | 21–25 | utara Padang Aurora |
| Puncak Komet | 21–25 | utara Pulau Awan |

Tiap area punya monster siang/malam/hujan, monster elit, dan satu bos. Pusat Misi punya tab Lv 16–20 dan Lv 21–25.

- Antar-area terhubung lewat **portal** (label menunjukkan tujuan) dan **peta dunia**.
- **Balon udara** mengantar antar kota dengan animasi berangkat dan tiba.
- Lab Prof. Zarko masih terkunci (cerita lanjutan).

## Sistem game

- **Level & stat**: XP dari monster dan misi; stat STR/INT/AGI dihitung otomatis dan disembunyikan dari pemain. Skill baru muncul tiap kelipatan level tertentu.
- **Serangan manual dengan soft-aim**: tidak ada auto-attack untuk karakter, bidikan dibantu otomatis.
- **Equipment**: hanya senjata dan armor, dengan pratinjau 3D di toko dan profil.
- **Pet**: tiap kota punya pet khas (kuda, domba, beruang, slime pelangi, kucing, robot mini, tupai, rusa, rubah, dan lainnya); satu pet aktif sekaligus. Pet punya bonus (lari lebih cepat, regen) dan **menyerang otomatis** monster agresif di dekat pemain dengan damage kecil yang mengikuti level. Sebagian pet aktif siang, sebagian malam.
- **Misi**: maksimal 3 aktif, dibagi tab level (1–5, 6–10, 11–15, 16–20, 21–25). Hijau = mudah, kuning = normal, merah = sulit dikerjakan sendiri. Hadiah koin sudah dibesarkan 25%.
- **Waktu & cuaca**: siang/malam dan cerah/hujan acak mengubah monster yang muncul.
- **Perjalanan**: portal, peta dunia, balon udara.
- **Audio**: efek suara sintetis lewat Web Audio.

## Co-op

- Pemain 1: menu atau tombol Co-op → **Buat room** → bagikan **kode 4 huruf**.
- Pemain 2 & 3: Co-op → masukkan kode → **Gabung**.
- Monster dikendalikan perangkat pembuat room. XP dan koin dibagi saat monster kalah; pemain level rendah dapat bonus XP.
- Koneksi lewat **PeerJS (WebRTC)**. Ada ping berkala, deteksi putus, dan **reconnect otomatis** (hingga ~35 detik) agar pindah aplikasi sebentar di HP tidak langsung memutus sesi.
- Butuh internet untuk signaling PeerJS dan font.

## Bahasa dan aksesibilitas

- Indonesia dan Inggris (tabel `TX`), dipilih lewat pengaturan.
- UI besar dan ramah sentuhan, tombol serang bisa ditahan.
- Konten **ramah anak**: tanpa tema gelap/kutukan dan tanpa simbol religius.

## Arsitektur teknis

- **Satu file HTML**: HTML + CSS + JS inline, grafis dari **Three.js r128** (dimuat dari cdnjs), semua model berupa voxel yang dirakit lewat kode, tanpa aset gambar/model eksternal.
- **Dua lapisan JS** dalam satu skrip:
  - `window.EZ` (logika murni): `CLASSES`, `SKILLS` per jalur senjata, `ADV`, `MON`, `QUESTS`, rumus damage/XP/kecepatan.
  - Game IIFE: render, dunia/zona, `buildHero`/`animHero`, `PETS`, portal & peta, UI, i18n, co-op.
- **FX**: `fxRoot` + `fxList` (fungsi yang mengembalikan `false` dilepas), helper `after`, `burst`, `ringFx`, `strikeFx`, dan pustaka visual skill `SV`. Thumbnail equipment dibuat lewat render-target.
- **Co-op**: objek `coop`, `coopTick` (ping 2,5 dtk, timeout 15 dtk), `rcAttempt` (reconnect), `guestLost`/`guestEnd`.
- **Penyimpanan**: `localStorage` dengan `sanitize` untuk memvalidasi data lama.
- **PWA**: `manifest.webmanifest`, ikon, `sw.js`; `version.json` dipakai untuk mendeteksi build baru.
- **UI kit**: blok `EZUI` diekstrak otomatis ke `ui-kit/` supaya komponen dan token bisa dipakai ulang di game lain.

## Build, test, dan deploy

Sumber utama game adalah fragmen HTML terpisah (`ezventure.html`, di luar repo). `build.py` membungkusnya ke `index.html`, mencap ID build, dan meng-generate `ui-kit/`.

```bash
python3 build.py [path/ke/ezventure.html]   # default: /home/claude/ezventure.html
git add -A && git commit -m "vNN" && git push
```

- Deploy lewat **GitHub Pages** dari branch utama.
- **Jangan edit `index.html` langsung** dan jangan menimpanya dengan fragmen; selalu lewat `build.py`.
- Pengujian memakai Playwright + Chromium (swiftshader) dengan hook debug `window.__ezv` (pindah zona, pakai skill, buka toko, dsb.). Co-op perlu jaringan sehingga diuji manual di perangkat nyata.

## Struktur repo

```
index.html              game (hasil build, jangan diedit manual)
build.py                pembungkus + penanda build + generator ui-kit
version.json            ID build terkini
manifest.webmanifest    konfigurasi PWA
sw.js                   service worker
icon-*.png, apple-touch-icon.png   ikon aplikasi
ui-kit/                 token & komponen UI yang diekstrak dari game
```

## Prinsip desain

- Mudah dipahami anak 5 tahun, sesi sekitar 15 menit, bisa dimainkan bareng orang tua.
- Co-op melawan monster saja, tanpa PvP.
- Visual cerah ala Ragnarok versi voxel.
- Nama kelas dan istilah mudah bagi orang Indonesia.
- UI/modal konsisten satu standar.

## Batasan dan rencana

- Co-op reconnect dan rasa kontrol (pet, skill) belum diuji luas di banyak perangkat nyata.
- Lab Prof. Zarko dan alur cerita akhir belum dibuka.
- Rencana: login ID + PIN dengan simpan awan (Supabase), paket APK, dan konten monster/area tambahan.

## Lisensi

Belum ditentukan. Hubungi pemilik repo sebelum memakai ulang kode atau aset.
