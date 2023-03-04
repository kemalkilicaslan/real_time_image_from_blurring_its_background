# Real Time Image From Blurring Its Background
# Arka Planını Bulanıklandırarak Gerçek Zamanlı Görüntü

import cv2

# Let's open the webcam.
# webcam'i açalım.
cap = cv2.VideoCapture(0)

# set the window size.
# pencere boyutunu ayarlayalım.
cap.set(3, 640)
cap.set(4, 480)

while True:
    # Let's take an image from the camera.
    # kameradan görüntü alalım.
    ret, frame = cap.read()

    # convert the image to grayscale.
    # görüntüyü gri tonlamaya çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # let's threshold the image.
    # görüntüyü eşikleyelim.
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Let's blur the background.
    # arkaplanı blurlayalım.
    blurred = cv2.GaussianBlur(frame, (21, 21), 0)

    # convert the blurred image to grayscale.
    # blurlanmış görüntüyü gri tonlamaya çevirelim.
    gray_blur = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    # Let's threshold the blurred image.
    # blurlanmış görüntüyü eşikleyelim.
    _, thresh_blur = cv2.threshold(gray_blur, 100, 255, cv2.THRESH_BINARY)

    # show the thresholded images to the screen.
    # eşiklenmiş görüntüleri ekrana gösterelim.
    cv2.imshow('Original', thresh)
    cv2.imshow('Blurred', thresh_blur)

    # Exit when 'q' key is pressed.
    # 'q' tuşuna basıldığında çıkın.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# let's finish the process.
# işlemi bitirelim.
cap.release()
cv2.destroyAllWindows()