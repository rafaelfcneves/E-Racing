"""
Mouse Fantasma — Controle do cursor por rastreamento de mao
============================================================
Unicamp E-Racing — Divisao Driverless | Onboarding 2026

Pipeline de percepcao:
    Captura (OpenCV) -> Deteccao (MediaPipe Hands) -> Extracao de
    coordenadas -> Mapeamento camera->tela -> Acao (PyAutoGUI)

Regras seguidas (do enunciado):
  - NADA de coordenadas de pixel hardcoded. A resolucao da tela e
    obtida dinamicamente com pyautogui.size().
  - O clique usa a distancia euclidiana entre o polegar (landmark 4)
    e o indicador (landmark 8) em coordenadas NORMALIZADAS.

Sair: pressione 'q' com a janela da camera em foco.
"""

import math

import cv2
import mediapipe as mp
import pyautogui

THUMB_TIP = 4
INDEX_TIP = 8

CLICK_THRESHOLD = 0.05

pyautogui.FAILSAFE = False


def main():
    screen_w, screen_h = pyautogui.size()

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("A camera nao pode ser aberta.")

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
    ) as hands:

        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1)


            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]
                lm = hand.landmark


                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

                index_tip = lm[INDEX_TIP]
                screen_x = int(index_tip.x * screen_w)
                screen_y = int(index_tip.y * screen_h)
                pyautogui.moveTo(screen_x, screen_y)

                thumb_tip = lm[THUMB_TIP]
                dist = math.dist(
                    (thumb_tip.x, thumb_tip.y),
                    (index_tip.x, index_tip.y),
                )
                if dist < CLICK_THRESHOLD:
                    pyautogui.click()

            cv2.imshow("Exemplo 01 - Mouse Fantasma", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()