# Prueba simulada de reconocimiento por video (26 nov 2026)

Envíos ficticios generados con `generar_envios.py`:

- **A:** caja de cartón, cinta azul, logo VELOZ EXPRESS, etiqueta blanca, guía 700123456789, "FRÁGIL" a mano, esquina aplastada.
- **B (gemelo engañoso):** igual a A, pero con etiqueta amarilla, guía 700123456788, sin "FRÁGIL" y sin golpe.
- **C:** bolsa plástica blanca, logo MENSAJERÍA ANDINA, guía 700987654321, destino Cali.

Los videos de custodia (15 s) pasaron por el código real de la app (selección de cuadros en Chromium). Claude hizo el papel de la IA de la app: leyó las guías y comparó rasgo por rasgo.

| Prueba | Resultado |
| --- | --- |
| Lectura de guía: A bueno, A movido, A oscuro, B | 4 de 4 correctas |
| A contra admisiones con guía legible | A 92 %, B 8 %, C 6 % |
| A oscuro contra B con guía ilegible, antes | **64 % (falso positivo, confianza media)** |
| Lo mismo después del rasgo "marcas únicas" | 25 % (descartado); A sube de 76 % a 79 % |
| Aviso de video borroso (nitidez 58), antes | no avisaba (umbral 30) |
| Lo mismo después del umbral 100 | avisa; el video movido pero legible (212) no avisa |

Nitidez medida como la mide la app (`medir_calidad.py`): bueno 382, gemelo 319, movido 212, muy borroso 58, oscuro 29 (brillo 26).

Límites: son videos sintéticos y el umbral de nitidez está calibrado con ellos. Hay que validarlo con videos reales de celular.
