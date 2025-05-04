import cv2
import time

webcam = cv2.VideoCapture(0)
counter = 1

print("--- Instrucciones ---")
print("Presiona 's' para guardar una foto.")
print("Presiona 'q' para salir.")

while True:
    try:
        check, frame = webcam.read()
        if not check:
            print("No se pudo capturar el frame.")
            break
        
        cv2.imshow("Capturando (Presiona 's' para guardar, 'q' para salir)", frame)
        
        key = cv2.waitKey(1)
        
        if key == ord('1'): 
            filename = f"piedra_{counter}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Foto guardada como: {filename}")
            counter += 1
        
        elif key == ord('2'):
            print("Apagando cámara...")
            webcam.release()
            cv2.destroyAllWindows()
            print("Programa terminado.")
            break
    
    except KeyboardInterrupt:
        print("\nApagando cámara...")
        webcam.release()
        cv2.destroyAllWindows()
        print("Programa terminado.")
        break