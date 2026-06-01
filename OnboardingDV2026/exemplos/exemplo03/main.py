

import cv2
import numpy as np
import mediapipe as mp


LEFT_EYE_OUTER = 33    
RIGHT_EYE_OUTER = 263   
NOSE_TIP = 1           


def load_texture(path="texture.png"):
    """Carrega a textura PNG preservando o canal alpha (4 canais)."""
    texture = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if texture is None:
        raise FileNotFoundError(
            f"Nao encontrei '{path}'. Coloque um PNG transparente nessa pasta."
        )
    if texture.shape[2] != 4:
        raise ValueError("A textura precisa ter canal alpha (PNG transparente, 4 canais).")
    return texture


def main():
    texture = load_texture("texture.png")
    tex_h, tex_w = texture.shape[:2]

    # --- Pontos de origem NA TEXTURA (em pixels da imagem da textura) ---
    # Convencao assumida: textura horizontal, onde a borda esquerda casa
    # com o olho esquerdo, a direita com o olho direito, e o ponto inferior
    # central casa com a regiao do nariz. Ajuste conforme seu PNG.
    src_pts = np.float32([
        [0,         tex_h * 0.5],   # corresponde ao olho esquerdo
        [tex_w,     tex_h * 0.5],   # corresponde ao olho direito
        [tex_w / 2, tex_h],         # corresponde ao nariz
    ])

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Nao consegui abrir a camera (indice 0).")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        frame = cv2.flip(frame, 1)
        frame_h, frame_w = frame.shape[:2]

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            lm = results.multi_face_landmarks[0].landmark

            dst_pts = np.float32([
                [lm[LEFT_EYE_OUTER].x * frame_w,  lm[LEFT_EYE_OUTER].y * frame_h],
                [lm[RIGHT_EYE_OUTER].x * frame_w, lm[RIGHT_EYE_OUTER].y * frame_h],
                [lm[NOSE_TIP].x * frame_w,        lm[NOSE_TIP].y * frame_h],
            ])

            M = cv2.getAffineTransform(src_pts, dst_pts)
            texture_warped = cv2.warpAffine(texture, M, (frame_w, frame_h))

            alpha = texture_warped[:, :, 3] / 255.0
            alpha_3ch = np.stack([alpha, alpha, alpha], axis=2)
            frame_bgr = frame.astype(float) * (1 - alpha_3ch) \
                + texture_warped[:, :, :3].astype(float) * alpha_3ch
            frame = frame_bgr.astype(np.uint8)

        cv2.imshow("Filtro Facial Dinamico", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    face_mesh.close()


if __name__ == "__main__":
    main()