import cv2

input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
quality = int(input("Enter the compression quality (0-100): "))

img = cv2.imread(input_file)
params = [cv2.IMWRITE_JPEG_QUALITY, quality]
cv2.imwrite(output_file, img, params)
