＜実験環境＞
・OS : Ubuntu 20.04 LTS
・CPU : Intel Core i7-9700F  3.00 GHz
・メモリ (CPU) : 16.00 GB
・GPU : NVIDIA GeForce RTX 2070 SUPER
・メモリ (GPU) : 9.00 GB

＊利用ライブラリ、パッケージ一覧とバージョン情報はenvironment.ymlを参照

＜内容について＞
●フォルダ
・datasetsフォルダ...学習データ、テストデータを用意しています。（A...インテリアスタイル画像、B...線画orグレースケール画像）
・checkpointsフォルダ...学習済モデルをそれぞれ格納しています（latest_net_G.pth）
・testimgフォルダ...テスト画像（カラー画像、グレースケール画像、線画画像）を格納しています。
（testimgフォルダ内のグレースケール画像、線画画像はdatasetsフォルダのtestBにあたります。）
・resultsフォルダ...test.pyを実行した際に変換画像が保存されます。
基本的には、↑の4つのフォルダを用います。

●コード
・CycleGAN.ipynb...上から順に実行すると学習からテストまで実行できます。（詳しくはファイル内にコメントしています）
→学習済モデル（既にcheckpoints内に格納しているlatest_net_G.pth）を使ってテストする場合は、CycleGAN.ipynbの #テスト 部分から実行すると動くと思います。
→新たにデータセットを作成する場合は、datasetsフォルダにデータを用意してからCycleGAN.ipynbを上から順に実行してください。

・LineDrawing.py...カラー画像を線画画像に変換する際に使用します。
→例として、testimg/testを指定してプログラムを実行すると、testimgフォルダ内にtest_GrayScale, test_LinDrawingフォルダが生成され、それぞれ画像が保存されます。
→新たにテストデータを追加する場合、もしくはデータセットを生成する場合はまずLineDrawing.pyによって線画画像、グレースケール画像を作成し、datasetsフォルダにセットしてください。


＜補足＞
●datasetsフォルダについて
・vintage2LineDrawing...ビンテージ画像と線画画像間での学習
・testA, testB, trainA, trainBの構造は守る必要がありますが、testAフォルダに関しては空で問題ありません
→testBに変換対象となる画像のグレースケールor線画画像を格納しています
→trainAはvintageなどのインテリア画像を格納しています（カラー）
→trainBはグレースケールもしくは線画画像を格納しています（trainimgフォルダにカラー画像も格納しています）


