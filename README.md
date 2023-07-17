# Devoir 2 : Calcul de profondeur et synthèse d'image

En utilisant les outils logiciels de la suite MPEG MIV, IVDE (https://gitlab.com/mpeg-i-visual/ivde) et RVS (https://gitlab.com/mpeg-i-visual/rvs/-/tree/master) générer les images de profondeur et les images de synthèse pour une des séquences de test de MPEG-I, Painter ou Frog (https://mpeg-miv.org/index.php/content-database-2/). Le test devrait être fait pour 10 trames et 4 caméras seulement.

Pour Painter, utiliser les caméras V0, V2, V5, V7 pour calculer la profondeur et synthétiser l’image de la caméra V1.

Pour Frog, utiliser les caméras V1, V4, V7, V10 pour calculer la profondeur et synthétiser l’image de la caméra V5.   

Tâches :
1. Télécharger la base de données des images (Painter ou Frog)
2. Sélectionner les dix premières trames des séquences à utiliser (suggestion : FFMPEG)

    ffmpeg -f rawvideo -framerate 25 -s 2048x1088 -pixel_format yuv420p16le -i v0_depth_2048x1088_yuv420p16le.yuv -c copy -vframes 10 v0_depth_10f.yuv

3. Installer le logiciel IVDE à partir du Git.
4. Générer les images de profondeur pour la séquence choisie. Seulement pour les 4 caméras sélectionnées
5. Évaluer la qualité des images de profondeur an utilisant la métrique PSNR (Matlab, OpenCV, FFMPEG, etc.).
6. Installer le logiciel RVS à partir du Git.
7. En utilisant les données de profondeur originaux de la séquence, générez les premières 3 trames de la séquence virtuelle (V1 pour Painter ou V5 pour Frog).
8. Comparez les résultats avec les vraies images de texture dans la base de données en utilisant la métrique PSNR.

Livrables :
1. Rapport avec la procédure et les résultats
2. Code utilisé pour arriver aux résultats (script)
