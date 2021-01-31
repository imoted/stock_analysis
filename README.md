# stock_analysis

## リンク

* チャレンジ https://signate.jp/competitions/423
* チュートリアル https://japanexchangegroup.github.io/J-Quants-Tutorial/

## 提出方法メモ
* dockerイメージ: `continuumio/anaconda3:2019.03`
* Dockerfile等を通してプログラムをインストールすることはできない。
* ライブラリ追加するにはpipでインストールできるモジュールか提出物(src以下)に含める

# dockerとデータ

* データの在処: https://signate.jp/competitions/423/data
* 環境変数STOCK_DATA_DIRにデータ入れたディレクトリのパスを設定しておくと/data_dirにマウントされる
* docker/build-image.shしてイメージ作っておく必要ある
* Dockerコンテナのメモリ割り当て少ないとファイルによってはこける(4GBなら大丈夫だった
