# Onboarding DV 2026 — Unicamp E-Racing

Exemplos práticos de Visão Computacional com foco em processamento de vídeo em tempo real, desenvolvidos para o onboarding da Divisão Driverless da Unicamp E-Racing.

---

## Instalação

### Pré-requisitos

**Linux:** Python já vem instalado nativamente. Instale o pip e o venv:

```bash
sudo apt install python3-pip python3-venv
```

**Windows:** pip e venv já vêm junto com o Python. Nenhum passo extra necessário.

---

### Ambiente Virtual

Recomendamos fortemente o uso de um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outras bibliotecas instaladas na sua máquina.

**1. Crie o ambiente virtual dentro da pasta do projeto:**

```bash
python3 -m venv venv
```

**2. Ative o ambiente virtual:**

```bash
# Linux / macOS
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

---

## Dependências

| Biblioteca | Versão | Uso |
|---|---|---|
| `mediapipe` | 0.10.9 | Detecção de mãos e rosto |
| `opencv-python` | 4.9.0.80 | Captura e exibição de vídeo |
| `numpy` | 1.26.4 | Processamento de arrays e transformações |
| `pyautogui` | 0.9.54 | Controle do mouse |
| `simpleaudio` | 1.0.4 | Síntese e reprodução de áudio |

---

Divisão Driverless — Unicamp E-Racing
