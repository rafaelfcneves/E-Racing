import mediapipe as mp
import numpy as np

mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles

def draw_landmarks_on_frame(rgb_image, detection_result):
    """
    desenha os landmarks no frame
    """
    hand_landmarks_list = detection_result.hand_landmarks
    handedness_list = detection_result.handedness
    # Copia a matriz desse frame e atribui a uma nova variável.
    annotated_frame = np.copy(rgb_image)

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