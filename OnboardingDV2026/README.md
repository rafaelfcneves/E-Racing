# Onboarding DV 2026 — Unicamp E-Racing 🐜⚡🔶

Tutorial de como rodar o Volante Virtual no Windows desenvolvido para o Onboarding 2026 da Unicamp E-Racing.

---

## Instalação do Python

**Versão do Python:** A versão do Python utilizada foi a 3.11.9 e pode ser baixada na [página oficial do Python](https://www.python.org/)

---

## Pré-requisitos

**Windows:** pip e venv já vêm junto com o Python. Nenhum passo extra necessário.

---

## Ambiente Virtual e Execução

Segue-se os passos para criar uma pasta venv, ativar o ambiente virtual e executar o programa no terminal cmd:

**1. Crie o ambiente virtual dentro da pasta do arquivo:**

```bash
# Windows (CMD)
python3 -m venv venv
```

**2. Ative o ambiente virtual:**

```bash
# Windows (CMD)
venv\Scripts\activate.bat
```

**3. Instale as dependências:**

```bash
# Windows (CMD)
pip install -r requirements.txt
```

**4. Executando o programa:**

```bash
# Windows (CMD)
python volante_virtualV1.py
```

---

## Dependências

| Biblioteca | Versão | Uso |
|---|---|---|
| `mediapipe` | 0.10.9 | Detecção de mãos |
| `opencv-python` | 4.9.0.80 | Captura e exibição de vídeo |
| `numpy` | 1.26.4 | Cálculo do ângulo entre as mãos |
| `pydirectinput` | 0.9.54 | Controle do teclado |

---

Onboarding Divisão Driverless 2026 — Unicamp E-Racing
