

import cv2
import numpy as np
import simpleaudio as sa
import mediapipe as mp


PALM = 9


FREQ_MIN = 80    
FREQ_MAX = 1200   

SMOOTHING = 0.15


SAMPLE_RATE = 44100
BLOCK_SECONDS = 0.05          
AMPLITUDE = 0.3              
BLOCK_SAMPLES = int(SAMPLE_RATE * BLOCK_SECONDS)


def map_range(value, in_min, in_max, out_min, out_max):
    return out_min + (value - in_min) * (out_max - out_min) / (in_max - in_min)


def make_block(freq, start_phase):


    phase_inc = 2 * np.pi * freq / SAMPLE_RATE
    phases = start_phase + phase_inc * np.arange(BLOCK_SAMPLES)
    wave = np.sin(phases) * AMPLITUDE

    audio = (wave * 32767).astype(np.int16)
    next_phase = (start_phase + phase_inc * BLOCK_SAMPLES) % (2 * np.pi)
    return audio, next_phase


def main():
    freq_smooth = 440.0
    phase = 0.0

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Nao consegui abrir a camera.")

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
                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

                hand_y = hand.landmark[PALM].y


                inverted_y = 1.0 - hand_y
                frequency = map_range(inverted_y, 0.0, 1.0, FREQ_MIN, FREQ_MAX)


                freq_smooth = freq_smooth + SMOOTHING * (frequency - freq_smooth)
                audio, phase = make_block(freq_smooth, phase)
                sa.play_buffer(audio, 1, 2, SAMPLE_RATE)

            cv2.imshow("Theremin Otico", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()