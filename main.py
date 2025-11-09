from gaze_tracking import GazeTracking
import cv2
import pyautogui

# Initialize gaze tracking and webcam
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

# Get screen size
screen_width, screen_height = pyautogui.size()

while True:
    # Capture frame from webcam
    _, frame = webcam.read()

    # Analyze gaze
    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    text = ""

    # Get gaze position
    if gaze.is_blinking():
        text = "Blinking"
        pyautogui.click()  # Blink to click
    elif gaze.is_right():
        text = "Looking right"
        pyautogui.moveRel(50, 0)  # Move mouse right
    elif gaze.is_left():
        text = "Looking left"
        pyautogui.moveRel(-50, 0)  # Move mouse left
    elif gaze.is_center():
        text = "Looking center"

    # Display status
    cv2.putText(frame, text, (20, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (255, 0, 0), 2)
    cv2.imshow("Gaze Mouse Control", frame)

    # Quit with 'q'
    if cv2.waitKey(1) == ord("q"):
        break

# Cleanup
webcam.release()
cv2.destroyAllWindows()
