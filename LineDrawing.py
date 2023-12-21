#グレースケール画像と線画画像の生成
import numpy as np
import cv2
import glob
import os
"""
①画像をグレーにする
②それを膨張処理する
→8近傍、つまり点の周り8箇所に対して膨張するというもの
③グレーと膨張画像の差分を取る
④差分画像を白黒反転する
"""
#グレースケール画像と線画画像の保存先フォルダの作成
keywords = ['Grayscale', 'LineDrawing']
path = "testimg/test" #任意のフォルダを指定
for keyword in keywords :
    new_path = path + "_" + keyword
    os.makedirs(new_path, exist_ok=True)

# 8近傍の定義
neiborhood8 = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]],
                            np.uint8)

#線画化
for f in glob.glob(path + '/*'):
    img = cv2.imread(f, 0) # 0なしでカラー
    cv2.imwrite(os.path.dirname(f) + '_Grayscale/' + os.path.basename(f), img)

    #膨張。iterations回数を増やすとより太い線が得られる
    img_dilate = cv2.dilate(img, neiborhood8, iterations=1) #膨張

    #差異を取る。この段階では背景黒、エッジが白の画像が得られる。
    img_diff = cv2.absdiff(img, img_dilate) #差分

    #白黒反転する。これによって背景白、線が黒の線画画像を得られる
    img_diff_not = cv2.bitwise_not(img_diff) #白黒反転
    cv2.imwrite(os.path.dirname(f) + '_LineDrawing/' + os.path.basename(f), img_diff_not)
