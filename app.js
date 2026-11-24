/* KIACreative catalog — filter + search */
const $ = (s)=>document.querySelector(s);
const esc = (s)=>String(s).replace(/[&<>"']/g,(c)=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));

function init(){
  const cats = ["All", ...Array.from(new Set(PRODUCTS.map(p=>p.category))).sort()];
  $("#category").innerHTML = cats.map(c=>`<option value="${esc(c)}">${esc(c)}</option>`).join("");
  render();
  $("#search").addEventListener("input", render);
  $("#category").addEventListener("change", render);
}

function render(){
  const q = $("#search").value.toLowerCase().trim();
  const cat = $("#category").value;
  const list = PRODUCTS.filter(p=>{
    const okCat = cat==="All" || p.category===cat;
    const okQ = !q || p.title.toLowerCase().includes(q) || p.category.toLowerCase().includes(q);
    return okCat && okQ;
  });
  $("#count").textContent = `${list.length} product${list.length===1?"":"s"}`;
  $("#empty").classList.toggle("hidden", list.length>0);
  $("#grid").innerHTML = list.map(p=>`
    <a href="${p.url}" target="_blank" rel="noopener" class="card bg-white rounded-2xl overflow-hidden border border-slate-100 block">
      <div class="aspect-square bg-cream overflow-hidden">
        <img src="${p.image}" alt="${esc(p.title)}" loading="lazy" class="w-full h-full object-cover">
      </div>
      <div class="p-4">
        <div class="text-[10px] font-bold uppercase tracking-wide text-gold mb-2">${esc(p.category)}</div>
        <div class="text-sm font-semibold leading-snug line-clamp-2 h-10">${esc(p.title)}</div>
        <div class="mt-4 flex items-center justify-between">
          <span class="font-extrabold text-lg">$${p.price}</span>
          <span class="text-xs font-bold text-pine bg-gold px-3 py-1.5 rounded-lg">View ↗</span>
        </div>
      </div>
    </a>`).join("");
}

document.addEventListener("DOMContentLoaded", init);
