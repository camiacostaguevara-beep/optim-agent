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

# Prueba con video real (26 nov 2026)

Video de celular de 12 s, 1920×1080, en HEVC (H.265) y 22,5 MB: una caja de tensiómetro aneroide sin guía de envío, girada en la mano. El video no se guarda en el repositorio.

| Prueba | Resultado |
| --- | --- |
| Abrir el video original en el navegador | **Falla:** el navegador no decodifica HEVC y el mensaje decía "pruebe con otro formato (MP4)", aunque el archivo es MP4 |
| Corrección | La app detecta HEVC y explica cómo desactivar los videos de alta eficiencia en Samsung y iPhone; el error queda visible bajo el video |
| Video convertido a H.264/VP8 | Nitidez 317, brillo 103, sin avisos; 8 cuadros de rasgos y 4 de lectura que cubren todas las caras |
| Lectura de guía | No hay guía: correcto, la app debe responder "no se leyó número de guía" |
| Rasgos visibles | Caja impresa blanca, azul marino y gris; texto "ANEROID SPHYGMOMANOMETER"; plástico transparente que la envuelve; una esquina superior rota y bordes gastados |

Conclusión: sin guía, la identificación depende solo de la apariencia, con un máximo de ~81 %. Como es una caja de fábrica que existe en muchas unidades iguales, lo que distingue este envío son las marcas únicas (el plástico y la esquina rota), no la impresión.
