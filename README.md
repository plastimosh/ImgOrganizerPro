# 📸 ImgOrganizer Pro

Herramienta de escritorio para **organizar, deduplicar y estructurar imágenes automáticamente** basada en metadata (EXIF) y hashing.

---

## 🚀 Problema que resuelve

La gestión manual de imágenes genera:

* Duplicados innecesarios
* Desorden por fechas inconsistentes
* Archivos sin naming estructurado
* Dificultad para localizar contenido

**ImgOrganizer Pro automatiza todo este proceso.**

---

## ⚙️ Funcionalidades principales

* 🔍 Exploración recursiva de carpetas
* 🧠 Extracción de metadata EXIF (fecha de captura)
* 🔐 Generación de hash para detección de duplicados
* ♻️ Clasificación automática de imágenes duplicadas
* 🗂️ Organización por año y mes
* 🏷️ Renombrado inteligente basado en timestamp
* 📦 Separación de duplicados en carpeta dedicada

---

## 🧱 Arquitectura del sistema

El sistema está dividido en módulos independientes:

```
src/
 ├── scanner/        # Exploración de archivos
 ├── metadata/       # Lectura EXIF
 ├── hashing/        # Generación de hash
 ├── duplicates/     # Detección de duplicados
 ├── organizer/      # Estructuración de carpetas
 ├── renamer/        # Renombrado de archivos
 ├── mover/          # Movimiento/copia
 └── ui/             # Interfaz de usuario
```

---

## 📂 Estructura de salida

```
/organized/
   /YYYY/
      /MM/
         YYYY-MM-DD_HH-MM-SS_hash.ext

/duplicates/
   archivos_duplicados.ext
```

---

## 📊 Flujo del sistema

1. Escaneo de archivos
2. Filtrado por tipo de imagen
3. Extracción de metadata
4. Generación de hash
5. Detección de duplicados
6. Organización estructural
7. Renombrado
8. Movimiento / copia

---

## 🧭 Roadmap del proyecto

El plan completo del proyecto está documentado aquí:

📄 `docs/plan_proyecto_imagenes.pdf`


Incluye:

* Fases completas del desarrollo
* Orden de implementación
* Escalabilidad futura

---

## 🔄 Flujo de desarrollo

El flujo de trabajo del repositorio está definido en:

📄 `docs/flujo_versionado_imgorganizer_pro.pdf`


Resumen:

* `main` → producción
* `dev` → integración
* `feature/*` → desarrollo

Regla clave:

```
git rebase dev
```

---

## 🏷️ Versionado

Se utiliza **versionado semántico (SemVer)**:

```
MAJOR.MINOR.PATCH
```

Ejemplo:

* `v0.1.0` → exploración de archivos
* `v0.2.0` → hashing
* `v1.0.0` → versión estable

---

## 🛠️ Tecnologías

* Python (core del sistema)
* Manejo de imágenes (Pillow)
* EXIF parsing
* Hashing (SHA-256)
* Interfaz gráfica (Tkinter / futura mejora)

---

## ▶️ Ejecución (futuro)

```bash
python src/main.py
```

---

## 📌 Estado del proyecto

🚧 En desarrollo activo basado en roadmap estructurado

---

## 🔮 Próximas mejoras

* Soporte HEIC
* Detección de imágenes similares (pHash)
* UI avanzada
* Indexado con base de datos
* Exportación de reportes

---

## 🤝 Contribución

Actualmente el proyecto está en fase inicial.
Las contribuciones se estructurarán conforme avance el roadmap.

---

## 📄 Licencia

Pendiente de definir

---

## 🧠 Notas técnicas

* La detección de duplicados se basa en hash exacto (no similitud visual)
* La metadata EXIF puede no estar disponible en todas las imágenes
* Se utiliza fallback a fecha del sistema cuando es necesario

---

## 👨‍💻 Autor

Proyecto desarrollado como herramienta escalable para gestión profesional de imágenes.
