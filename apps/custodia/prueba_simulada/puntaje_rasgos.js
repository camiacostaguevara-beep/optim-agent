// Puntaje de la app (copiado de index.html) con y sin el rasgo "marcas".
function make(FEAT,caps){return r=>{let pos=0,seen=0;const f={};
  for(const [k,,w] of FEAT){const v=String(r[k]||'nv');f[k]=v;if(v==='si'){pos+=w;seen+=w}else if(v==='no')seen+=w}
  let pct=seen?Math.round(100*pos/(seen+20)):0;if(f.numeros==='si')pct=Math.max(pct,92);if(f.numeros==='no')pct=Math.min(pct,8);
  if(caps.some(k=>f[k]==='no'))pct=Math.min(pct,25);return Math.max(0,Math.min(99,pct))}}
const BASE=[['numeros','',45],['etiquetas','',18],['logos','',15],['empaque','',12],['color','',10],['cinta','',8],['forma','',8],['averias','',4]];
const antes=make(BASE,['logos','etiquetas','empaque']);
const despues=make([...BASE,['marcas','',12]],['logos','etiquetas','empaque','marcas']);
// Juicios hechos mirando los cuadros (custodia de A) contra cada admisión.
const casos={
 'A oscuro vs adm A (guía legible)':{numeros:'si',etiquetas:'si',logos:'si',empaque:'si',color:'nv',cinta:'si',forma:'si',averias:'si',marcas:'si'},
 'A oscuro vs adm B (guía legible)':{numeros:'no',etiquetas:'nv',logos:'si',empaque:'si',color:'nv',cinta:'si',forma:'si',averias:'no',marcas:'no'},
 'A oscuro vs adm C (guía legible)':{numeros:'no',etiquetas:'nv',logos:'no',empaque:'no',color:'no',cinta:'no',forma:'si',averias:'nv',marcas:'no'},
 'A oscuro vs adm A (guía ILEGIBLE)':{numeros:'nv',etiquetas:'si',logos:'si',empaque:'si',color:'nv',cinta:'si',forma:'si',averias:'si',marcas:'si'},
 'A oscuro vs adm B (guía ILEGIBLE)':{numeros:'nv',etiquetas:'nv',logos:'si',empaque:'si',color:'nv',cinta:'si',forma:'si',averias:'no',marcas:'no'},
 'A oscuro vs adm C (guía ILEGIBLE)':{numeros:'nv',etiquetas:'nv',logos:'no',empaque:'no',color:'no',cinta:'no',forma:'si',averias:'nv',marcas:'no'},
};
console.log('caso'.padEnd(36),'antes','después');
for(const [k,r] of Object.entries(casos))console.log(k.padEnd(36),String(antes(r)).padStart(4)+'%',String(despues(r)).padStart(6)+'%');
