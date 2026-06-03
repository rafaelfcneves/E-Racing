import mediapipe as mp
import numpy as np
import cv2

mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles

MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (255, 127, 39)

def draw_landmarks_on_frame(rgb_frame, detection_result):
    """
    desenha os landmarks no frame
    """
    hand_landmarks_list = detection_result.hand_landmarks
    handedness_list = detection_result.handedness
    # Copia a matriz desse frame e atribui a uma nova variável.
    annotated_frame = np.copy(rgb_frame)

    for i in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[i]
        handedness = handedness_list[i]

        # Função que desenha as landmarks e as conexões entre eles(linhas)
        mp_drawing.draw_landmarks(
        annotated_frame,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_drawing_styles.get_default_hand_landmarks_style(),
        mp_drawing_styles.get_default_hand_connections_style()
        )

        # Obter as coordenadas de onde será escrito a identificação do objeto
        height, width, _ = annotated_frame.shape
        x_coordinates = [landmark.x for landmark in hand_landmarks]
        y_coordinates = [landmark.y for landmark in hand_landmarks]
        text_x = int(min(x_coordinates) * width)
        text_y = int(min(y_coordinates) * height) - MARGIN

        # Escrever na tela se a mão identificada é a esquerda ou a direita
        cv2.putText(annotated_frame, f"{handedness[0].category_name}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    return annotated_frame