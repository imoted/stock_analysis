# dockerとデータ

* データの在処: https://signate.jp/competitions/423/data
* 環境変数STOCK_DATA_DIRにデータ入れたディレクトリのパスを設定しておく
* /data_dirにマウントされる
* Dockerコンテナのメモリ割り当て少ないとファイルによってはこける(4GBなら大丈夫だった
