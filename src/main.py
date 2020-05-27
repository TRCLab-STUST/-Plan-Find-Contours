import cv2
import os
import json

ROOT_DIR = os.path.join("../")
IMG_DIR = os.path.join(ROOT_DIR, "Images")
JSON_DIR = os.path.join(ROOT_DIR, "Json")
TH_OUT = os.path.join(ROOT_DIR, "th_out")


def find_c(image, filename):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imwrite(os.path.join(TH_OUT, filename), image)
    return image, contours


def main():
    image_list = os.listdir(IMG_DIR)

    jsonfilename = image_list[0].strip(".jpg") + "to" + image_list[len(image_list) - 1].strip(".jpg") + ".json"

    json_open = open(os.path.join(JSON_DIR, jsonfilename), 'w')
    json_open.write("{\n}")
    json_open.close()
    json_file = open(os.path.join(JSON_DIR, jsonfilename), 'r')
    json_file_data = json_file.read()
    data = json.loads(json_file_data)

    for file in image_list:
        img = cv2.imread(os.path.join(IMG_DIR, file))
        img, contours = find_c(img, file)

        for n in range(0, len(contours)):
            list_x = []
            list_y = []
            for point in contours[n]:
                for x, y in point:
                    list_x.append(x)
                    list_y.append(y)
        data[file] = {}
        data[file]['all_points_x'] = list_x
        data[file]['all_points_y'] = list_y

    with open(os.path.join(JSON_DIR, jsonfilename), "w") as file_write:
        json.dump(data, file_write, default=int)


if __name__ == '__main__':
    main()
