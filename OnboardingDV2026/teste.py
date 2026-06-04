import math
import cv2
import mediapipe as mp
import numpy as np
import pyautogui

MARGIN = 10
FONT_SIZE = 1
FONT_THICKNESS = 1
COLOR = (39, 127, 255)

def obter_coordenadas(frame, dados, mp_hands, mp_draw):
    y_left, y_right, x_left, x_right = None, None, None, None
    if not dados.multi_hand_landmarks:
        return y_left, y_right, x_left, x_right
    height, width, _ = frame.shape
    # Recebe as mãos que estão na tela e as desenha
    for i in range(len(dados.multi_hand_landmarks)):
        hand = dados.multi_hand_landmarks[i]
        # Lista de tuplas com as coordenadas das landmarks
        lm = hand.landmark
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        classificacao = dados.multi_handedness[i].classification[0]
        lado = classificacao.label
        
        if lado == "Left":
            y_left = int(lm[9].y * height)
            x_left = int(lm[9].x * width)
        elif lado == "Right":
            y_right = int(lm[9].y * height)
            x_right = int(lm[9].x * width)

            coordenadas_x = [landmark.x for landmark in lm]
            coordenadas_y = [landmark.y for landmark in lm]
            text_x = int(min(coordenadas_x) * width)    # Coordenada x do texto
            text_y = int(min(coordenadas_y) * height) - MARGIN   # Coordenada y do texto

            cv2.putText(frame,lado,(text_x, text_y),cv2.FONT_HERSHEY_SIMPLEX, 0.8,COLOR,2, cv2.LINE_AA)
    return y_left, y_right, x_left, x_right
def main():
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    x_esquerda, x_direita, y_esquerda, y_direita = None, None, None, None
    comando =""

    # Chamada da WebCam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("A camera nao pode ser aberta.")

    # Evita vazamento de memória caso a aplicação feche
    with mp_hands.Hands(
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
    ) as hands:

    # Loop principal da transmissão de vídeo.
        while True:
            # Captura o frame da transmissão
            ok, frame = cap.read()
            if not ok:
                break

            # Espelha o frame
            frame = cv2.flip(frame, 1)

            # Converte o frame de BGR para RGB, pois MediaPipe só reconhece em RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Retorna um objeto que contém uma lista das mãos que estão na tela (máx 2),
            # Uma tupla que contém as coordenadas dos Landmarks
            dados = hands.process(frame_rgb)

            # Se identificados os Landmarks:
            if dados.multi_hand_landmarks:
                # Recebe as mãos que estão na tela e as desenha
                for i in range(len(dados.multi_hand_landmarks)):
                    hand = dados.multi_hand_landmarks[i]
                    # Lista de tuplas com as coordenadas das landmarks
                    lm = hand.landmark
                    mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

                    # Classificar a mão
                    classificacao = dados.multi_handedness[i].classification[0]
                    lado = classificacao.label  # Retorna strings "Left" ou "Right"

                    # Escrver se é mão esquerda ou direita.
                    height, width, _ = frame_rgb.shape

                    if lado == "Left":
                        y_esquerda = int(lm[9].y * height)
                        x_esquerda = int(lm[9].x * width)
                    elif lado == "Right":
                        y_direita = int(lm[9].y * height)
                        x_direita = int(lm[9].x * width)

                    coordenadas_x = [landmark.x for landmark in lm]
                    coordenadas_y = [landmark.y for landmark in lm]
                    text_x = int(min(coordenadas_x) * width)    # Coordenada x do texto
                    text_y = int(min(coordenadas_y) * height) - MARGIN   # Coordenada y do texto

                    cv2.putText(
                        frame,       # Desenhando na sua tela preta
                        lado,           # O texto "Esquerda" ou "Direita"
                        (text_x, text_y),  # A posição dinâmica que acompanha a mão
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        0.8, 
                        COLOR,       # A cor laranja
                        2, 
                        cv2.LINE_AA
                    )
                if y_esquerda is not None and y_direita is not None and x_esquerda is not None and x_direita is not None:
                    delta_y = y_direita - y_esquerda
                    delta_x = x_direita - x_esquerda
                    tetha = np.arctan2(delta_y, delta_x)

                    if (tetha < 0 and -(math.pi/2) < tetha < -(math.pi/12)):
                        comando = "TURN LEFT"
                        cv2.putText(
                            frame,
                            comando,           # O texto "Left" ou "Right"
                            (int(width/2) - 100, 50),  # A posição dinâmica que acompanha a mão
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.8, 
                            COLOR,       # A cor laranja
                            2, 
                            cv2.LINE_AA
                        )
                    elif (tetha > 0 and math.pi/12 < tetha < math.pi/2):
                        comando = "TURN RIGHT"
                        cv2.putText(
                            frame,
                            comando,           # O texto "Left" ou "Right"
                            (int(width/2) - 100, 50),  # A posição dinâmica que acompanha a mão
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.8, 
                            COLOR,       # A cor laranja
                            2, 
                            cv2.LINE_AA
                        )
                    else:
                        comando = "AHEAD"
                        cv2.putText(
                            frame,
                            comando,           # O texto "Left" ou "Right"
                            (int(width/2) - 100, 50),  # A posição dinâmica que acompanha a mão
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.8, 
                            COLOR,       # A cor laranja
                            2, 
                            cv2.LINE_AA
                        )

            # Função que cria a janela onde será transmitido o vídeo.
            cv2.imshow("Teste de camera", frame)

            # Quebra o loop da transmissão de vídeo ao apertar "q"
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    # Libera a Webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()