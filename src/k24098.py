import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def k24098():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()
    app.write_img("images/camera_capture_k24098.png") # カメラから画像の撮影

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread("images/camera_capture_k24098.png")

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                cal_x = 0
                cal_y = 0
                if(x >= c_width): cal_x = x - c_width
                if(y >= c_hight): cal_y = y - c_hight
                google_img[y,x] = capture_img[cal_y,cal_x]
    
    # 最終結果の書き込み
    cv2.imwrite("output_images/lecture05_01_k24098.png",google_img)