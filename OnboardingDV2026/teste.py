import cv2
import mediapipe as mp
import numpy as np

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

            # Converte o frame de BGR para RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Retorna um objeto que contém uma lista das mãos que estão na tela (máx 2),
            # Uma tupla que contém as coordenadas dos Landmarks
            dados = hands.process(frame_rgb)

            # Se identificados os Landmarks:
            if dados.multi_hand_landmarks:
                for i in range(len(dados.multi_hand_landmarks)):
                    hand = dados.multi_hand_landmarks[i]
                    mp_draw.draw_landmarks(frame_rgb, hand, mp_hands.HAND_CONNECTIONS)

            # Aplica o filtro preto com contornos brancos
            gray = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2GRAY)
            edges = cv2.Canny(gray, 100, 200)

            # Função que cria a janela onde será transmitido o vídeo.
            cv2.imshow("Teste de camera", edges)

            # Quebra o loop da transmissão de vídeo ao apertar "q"
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    # Libera a Webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()