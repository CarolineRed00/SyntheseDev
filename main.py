import cv2 as cv
from math import *
import numpy as np
import yuvio
import skimage

# Tâche 5 / 8 : évaluation de la qualité des images
# Lecture des fichiers ".yuv"
# Implémentation du calcul de la métrique PSNR

def PSNR2Img(img_1,img_2, R):
    mse = np.mean((img_1-img_2)**2)
    if(mse==0):
        return 100

    psnr = 20 * log10(R) - 10*log10(mse)
    return psnr

def read_yuv_depth(height,width,path_to_yuv1,path_to_yuv2):
    yuv_stream1 = open(path_to_yuv1, 'rb')
    yuv_stream2 = open(path_to_yuv2, 'rb')

    psnr=[]
    psnr2=[]
    while True:
        # Lire une trame YUV
        yuv_frame1 = yuv_stream1.read(width * height * 3)
        yuv_frame2 = yuv_stream2.read(width * height * 3)

        if not yuv_frame1 or not yuv_frame2:
            break

        # Convertir la trame YUV en image BGR
        yuv_frame_np1 = np.frombuffer(yuv_frame1, dtype=np.uint16).reshape((int(height * 1.5), width))
        yuv_frame_np2 = np.frombuffer(yuv_frame2, dtype=np.uint16).reshape((int(height * 1.5), width))

        yuv_frame_np1 = (yuv_frame_np1 / 256).astype(np.uint8)  # Convert 8-bit
        yuv_frame_np2 = (yuv_frame_np2 / 256).astype(np.uint8)

        bgr_frame1 = cv.cvtColor(yuv_frame_np1, cv.COLOR_YUV2BGR_NV12)
        bgr_frame2 = cv.cvtColor(yuv_frame_np2, cv.COLOR_YUV2BGR_NV12)

        bgr1_resized = cv.resize(bgr_frame1,(int(width * 0.2), int(height * 0.2)))
        bgr2_resized = cv.resize(bgr_frame1, (int(width * 0.2), int(height * 0.2)))

        # Afficher l'image BGR
        cv.imshow('YUV Viewer 1', bgr1_resized)
        cv.imshow('YUV Viewer 2', bgr2_resized)

        psnr.append(PSNR2Img(bgr_frame1, bgr_frame2, 255))
        psnr2.append(skimage.metrics.peak_signal_noise_ratio(bgr_frame1, bgr_frame2, data_range=255))

        # Attendre l'appui sur la touche 'q' pour quitter
        if cv.waitKey(500) & 0xFF == ord('q'):
            break

    print("read_yuv_depth",psnr)
    print("read_yuv_depth2", psnr2)
    # Fermer la fenêtre d'affichage et le flux vidéo
    cv.destroyAllWindows()
    yuv_stream1.close()
    yuv_stream2.close()

#read_yuv_depth(1088,2048,r"C:\Users\carol\Downloads\ETS_Cours\VIDEO\Dev2\painter\v7_depth_10f.yuv",r"C:\Users\carol\Downloads\ETS_Cours\VIDEO\Dev2\painter\v7_depthmap.yuv")

def read_yuv_texture(height,width,path_to_yuv1,path_to_yuv2):
    yuv_stream1 = open(path_to_yuv1, 'rb')
    yuv_stream2 = open(path_to_yuv2, 'rb')

    psnr=[]
    psnr2=[]
    while True:
        # Lire une trame YUV
        yuv_frame1 = yuv_stream1.read(width * height * 3)
        yuv_frame2 = yuv_stream2.read(width * height * 3)

        if not yuv_frame1 or not yuv_frame2:
            break

        # Convertir la trame YUV en image BGR
        yuv_frame_np1 = np.frombuffer(yuv_frame1, dtype=np.uint16).reshape((int(height * 1.5), width))
        yuv_frame_np2 = np.frombuffer(yuv_frame2, dtype=np.uint16).reshape((int(height * 1.5), width))

        yuv_frame_np1 = (yuv_frame_np1 *64/256).astype(np.uint8)  # Convert
        yuv_frame_np2 = (yuv_frame_np2 *64/256).astype(np.uint8)

        bgr_frame1 = cv.cvtColor(yuv_frame_np1, cv.COLOR_YUV2BGR_I420) #_NV21 12 I420
        bgr_frame2 = cv.cvtColor(yuv_frame_np2, cv.COLOR_YUV2BGR_I420)

        bgr1_resized = cv.resize(bgr_frame1,(int(width * 0.2), int(height * 0.2)))
        bgr2_resized = cv.resize(bgr_frame1, (int(width * 0.2), int(height * 0.2)))

        # Afficher l'image BGR
        cv.imshow('YUV Viewer 1', bgr1_resized)
        cv.imshow('YUV Viewer 2', bgr2_resized)

        psnr.append(PSNR2Img(bgr_frame1, bgr_frame2,255))
        psnr2.append(skimage.metrics.peak_signal_noise_ratio(bgr_frame1, bgr_frame2, data_range=255))

        # Attendre l'appui sur la touche 'q' pour quitter
        if cv.waitKey(500) & 0xFF == ord('q'):
            break

    print("read_yuv_texture",psnr)
    print("read_yuv_texture2", psnr2)
    # Fermer la fenêtre d'affichage et le flux vidéo
    cv.destroyAllWindows()
    yuv_stream1.close()
    yuv_stream2.close()

read_yuv_texture(1088,2048,r"C:\Users\carol\Downloads\ETS_Cours\VIDEO\Dev2\painter\v1_from_v0_v2_v5_v7.yuv",r"C:\Users\carol\Downloads\ETS_Cours\VIDEO\Dev2\painter\v1_texture_2048x1088_yuv420p10le.yuv")


# Utilisation de YUVIO pour lire les vidéos de profondeur

def read_yuv_yuvio(height,width,path_to_yuv1, path_to_yuv2):
    # depth 16le
    #yuv_frames_1 = yuvio.mimread(path_to_yuv1,width,height,"yuv420p16le")
    #yuv_frames_2 = yuvio.mimread(path_to_yuv2, width, height, "yuv420p16le")
    # texture 10le
    yuv_frames_1 = yuvio.mimread(path_to_yuv1, width, height, "yuv420p10le")
    yuv_frames_2 = yuvio.mimread(path_to_yuv2, width, height, "yuv420p10le")

    psnr_y=[]
    psnr_u=[]
    psnr_v=[]

    for i in range(len(yuv_frames_1)):
        frame1 = yuv_frames_1[i]
        frame2 = yuv_frames_2[i]
        #psnr_y.append(skimage.metrics.peak_signal_noise_ratio(frame1.y, frame2.y, data_range=1023))
        #psnr_u.append(skimage.metrics.peak_signal_noise_ratio(frame1.u, frame2.u, data_range=1023))
        #psnr_v.append(skimage.metrics.peak_signal_noise_ratio(frame1.v, frame2.v, data_range=1023))
        psnr_y.append(PSNR2Img(frame1.y, frame2.y, 1023))
        psnr_u.append(PSNR2Img(frame1.u, frame2.u, 1023))
        psnr_v.append(PSNR2Img(frame1.v, frame2.v, 1023))

    print("read_yuv_yuvio_y",psnr_y)
    print("read_yuv_yuvio_u",psnr_u)
    print("read_yuv_yuvio_v",psnr_v)

    return psnr_y

#read_yuv(1088,2048,r"C:\Users\carol\Downloads\ETS_Cours\VIDEO\Dev2\painter\v7_depth_10f.yuv", r"C:\Users\carol\Downloads\ETS_Cours\VIDEO\Dev2\painter\v7_depthmap.yuv")
#read_yuv_yuvio(1088,2048,r"C:\Users\carol\Downloads\ETS_Cours\VIDEO\Dev2\painter\v1_from_v0_v2_v5_v7.yuv",r"C:\Users\carol\Downloads\ETS_Cours\VIDEO\Dev2\painter\v1_texture_2048x1088_yuv420p10le.yuv")

