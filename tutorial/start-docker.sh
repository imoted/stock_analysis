# https://japanexchangegroup.github.io/J-Quants-Tutorial/#_%E5%AE%9F%E8%A1%8C%E7%92%B0%E5%A2%83%E5%8F%8A%E3%81%B3%E5%BF%85%E8%A6%81%E3%81%AA%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA
# ** チュートリアルページからコピペ 
# dockerでjupyter notebookを起動します。(初回実行時は約2GB程度コンテナイメージをダウンロードします。)
# データ配置先のディレクトリを /path/to としてマウントしています。
# 学習済みモデル提出用のディレクトリ (handson/Chapter02/archive) を /opt/ml としてマウントしています。
# jupyter notebook作業用に handson ディレクトリを /notebook としてマウントしています。
# jupyter notebook は port 8888でtokenとpasswordを空にして、vscode のjupyter pluginからアクセスできるように xsrf 対策を無効化しています。

# イメージをビルドしておく
# docker/build-image.sh

# チュートリアル・ディレクトリに移動
CURRENT=$(cd $(dirname $0);pwd)
cd ${CURRENT}
echo "Changed directory to: ${CURRENT}"

# データ: https://signate.jp/competitions/423/data
# データでかいのでマシン上の任意のディレクトリに入れておく
# 環境変数STOCK_DATA_DIRにそのパスを設定しておく
#DATA_DIR=$(pwd)/data_dir 
DATA_DIR=${STOCK_DATA_ROOT}
echo "DATA_DIR: ${STOCK_DATA_ROOT}"

echo "RUN docker container"
docker run --name tutorial -v ${DATA_DIR}:/data_dir -v $(pwd)/Chapter02/archive:/opt/ml -v $(pwd):/notebook -e PYTHONPATH=/opt/ml/src -v $(pwd):/notebook -p8888:8888 --rm -it stock-env jupyter notebook --ip 0.0.0.0 --allow-root --no-browser --no-mathjax --NotebookApp.disable_check_xsrf=True  --NotebookApp.token='' --NotebookApp.password='' /notebook
