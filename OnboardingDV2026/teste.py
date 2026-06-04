import cv2
import mediapipe as mp
import numpy as np

MARGIN = 10
FONT_SIZE = 1
FONT_THICKNESS = 1
COLOR = (39, 127, 255)

def main():
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
    
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
                    lado = classificacao.label

                    # Escrver se é mão esquerda ou direita.
                    height, width, _ = frame_rgb.shape
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