import cv2 as cv

img = cv.imread('photos/city.jpg')

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

capture = cv.VideoCapture('videos/sea.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale =.2)

    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    # Press 'e' in keyboard to interrupt video
    if cv.waitKey(20) & 0xFF==ord('e'):
        break

capture.release()
cv.destroyAllWindows()