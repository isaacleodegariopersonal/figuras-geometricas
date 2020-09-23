import cv2

image = cv2.imread("FormasGeometricas.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
border = cv2.Canny(gray, 10, 120)
border_figure = cv2.findContours(border, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

for cont in border_figure:
    cv2.drawContours(image, border_figure, -1, (0, 0, 0), 2)
    epsilon = 0.01*cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, epsilon, True)
    cv2.drawContours(image, [approx], -1, (0, 0, 0), 2)
    print("vertices aproximados", len(approx))
    x, y, w, h = cv2.boundingRect(approx)
    if len(approx) == 3:
        cv2.putText(image, 'Triangulo', (x+10, y+80), 3, 1, (0, 0, 0), 2)
    if len(approx) > 10:
        cv2.putText(image, 'Circulo', (x+10, y+80), 4, 1, (0, 0, 0), 2)
    if len(approx) == 4:
        aspect_ratio = float(w)/h
        if aspect_ratio == 1:
            cv2.putText(image, 'Cuadrado', (x+10, y+80), 4, 1, (0, 0, 0), 2)
        else:
            cv2.putText(image, 'Rectangulo', (x+10, y+80), 4, 1, (0, 0, 0), 2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.imshow("border", border)
cv2.imshow("gray", gray)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()