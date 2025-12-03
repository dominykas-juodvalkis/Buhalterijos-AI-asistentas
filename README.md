# Financial AI Demo

Tai demonstracinis projektas, skirtas finansinių dokumentų apdorojimui naudojant OCR, NLP ir ML klasifikaciją. Projektas skirtas parodyti end-to-end procesą: nuo dokumentų nuskaitymo iki apskaitos įrašų generavimo.

## 📂 Struktūra
Buhalterijos-AI-asistentas/
│
├─ data/ # Demonstraciniai failai (HTML, PDF, Images)
│
├─ notebooks/ # Colab notebook'ai pagal loginius blokus
│ ├─ 00_packages.ipynb
│ ├─ 01_data_parsing.ipynb
│ ├─ 02_gemini_classification.ipynb
│ ├─ 03_ml_classification.ipynb
│ └─ 04_accounting_mapping.ipynb
│
├─ scripts/ # Python moduliai
│ ├─ ocr_utils.py
│ ├─ gemini_utils.py
│ ├─ ml_classifier.py
│ └─ accounting_map.py
│
├─ BuhalterijosAI-DEMO.ipynb
├─ README.md
└─ requirements.txt
