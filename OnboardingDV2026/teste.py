import cv2

def main():
    # Chamada da WebCam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("A camera nao pode ser aberta.")

    # Loop principal da transmissão de vídeo.
    while True:
        # Captura o frame da transmissão
        ok, frame = cap.read()
        if not ok:
            break

        # Espelha o frame
        frame = cv2.flip(frame, 1)

        # Aplica o filtro preto com contornos brancos
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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