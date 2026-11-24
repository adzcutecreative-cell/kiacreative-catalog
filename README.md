# KIACreative — Product Catalog Landing Page

Static landing page yang menampilkan semua produk Etsy KIACreative dalam satu tempat. Checkout tetap di Etsy.

## Update produk

Edit `products.js` — tiap entry:

```js
{ id:"...", title:"...", price:"9.99", category:"Spreadsheet",
  image:"assets/products/<id>.jpg", url:"https://www.etsy.com/listing/<id>" }
```

Lalu:
```bash
git add . && git commit -m "Update catalog" && git push
```

GitHub Pages otomatis rebuild ~30 detik.

## Regenerate dari Etsy

`_build_catalog.py` berisi daftar produk + path gambar lokal. Jalankan:
```bash
python _build_catalog.py
```
untuk regenerate `products.js` dan thumbnail `assets/products/`.

## Hosting

GitHub Pages, branch `main`, root folder.
