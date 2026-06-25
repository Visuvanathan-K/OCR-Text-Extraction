import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(['en'])

image_path = "images/1003w-KbiSkqIgYaM.webp"

results = reader.readtext(image_path)

img = cv2.imread(image_path)

for detection in results:
    bbox, text, confidence = detection

    top_left = tuple(map(int, bbox[0]))
    bottom_right = tuple(map(int, bbox[2]))

    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

    cv2.putText(
        img,
        text,
        top_left,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12,8))
plt.imshow(img)
plt.axis("off")
plt.show()