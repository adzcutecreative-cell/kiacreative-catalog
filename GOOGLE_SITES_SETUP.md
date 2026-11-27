# Google Sites — Setup KIACreative

Banner siap pakai:
`C:\Users\USER\Downloads\KIACreative_Products\Landing_Page\Google_Sites_Banner_1600x600.png`

Katalog (sumber embed):
`https://adzcutecreative-cell.github.io/kiacreative-catalog/`

---

## LANGKAH

1. Buka `https://sites.google.com` → **New site** (blank)
2. Judul site: **KIACreative**
3. **Settings → Themes**: pilih warna netral / hitam-putih. Theme custom nggak bisa pakai kode, jadi biarkan sederhana.
4. Klik area **banner** → **Change image** → upload `Google_Sites_Banner_1600x600.png`
5. Tambah bagian/konten sesuai copy di bawah
6. **Publish** → copy URL Google Sites

---

## HALAMAN 1 — HOME (copy-paste)

### Bagian A — Headline
```
Digital products for people who build small businesses.
```
Sub-teks:
```
Templates, web apps, printables and AI skills — instant download, no subscription.
```

### Bagian B — Tombol (pakai Insert → Buttons)
- **Shop Etsy** → `https://kiacreative.etsy.com`
- **Shop Gumroad** → `https://adzcute.gumroad.com`
- **View catalog** → link ke bagian "Catalog" di halaman yang sama

### Bagian C — Katalog (embed)
**Insert → Embed → By URL**, tempel:
```
https://adzcutecreative-cell.github.io/kiacreative-catalog/
```
- Width: **100%**
- Height: **1800 px** (biar semua card kelihatan tanpa scroll dobel)
- Centang **"Allow embedding"** kalau ada opsi

### Bagian D — Kenapa KIACreative
```
✅ Instant download — no physical shipping
✅ Commercial use on selected products
✅ Made for Etsy sellers, freelancers and small shops
✅ New products added every week
```

### Bagian E — About (pendek)
```
KIACreative makes practical digital tools for Etsy sellers, freelancers and small business owners. Every product is designed to save time — from spreadsheets and web apps to printables and AI skill bundles.
```

### Bagian F — Contact
```
Questions? Message me on Etsy — I usually reply within 24 hours.
https://kiacreative.etsy.com
```

---

## HALAMAN 2 — SHOP (opsional)
Bisa bikin halaman khusus kalau mau lebih rapi:

### Judul
```
Shop
```

### 3 kolom kartu (Insert → Columns)
| Kolom | Judul | Link |
|---|---|---|
| 1 | **Etsy shop** — 35+ digital products | `https://kiacreative.etsy.com` |
| 2 | **Gumroad** — AI skills & VAT app | `https://adzcute.gumroad.com` |
| 3 | **Free catalog** — all products in one page | `https://adzcutecreative-cell.github.io/kiacreative-catalog/` |

---

## PENGATURAN PENTING

| Setting | Nilai |
|---|---|
| Sharing | **Anyone with the link can view** (public) |
| SEO | Judul site = `KIACreative — Digital Products` |
| Custom domain | Settings → Custom domains (butuh domain + verifikasi) |
| Mobile preview | Cek di HP — iframe kadang perlu tinggi disesuaikan |
| Search engine | Google Sites otomatis index; GitHub Pages tetap jadi sumber kanonical |

---

## CATATAN
- Google Sites **tidak bisa menjalankan file JS/CSS** lewat "Embed code". Satu-satunya cara nampilin katalog yang interaktif ya lewat **Embed → By URL** (iframe).
- Jangan hapus GitHub Pages — kalau mati, embed di Google Sites juga kosong.
- Link checkout Etsy/Gumroad pakai `target="_blank"`, jadi tetap kebuka dari dalam iframe.
