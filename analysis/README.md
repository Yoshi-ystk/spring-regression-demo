# 📊 analysis フォルダ

このフォルダには、線形回帰分析を行う Python スクリプトおよび出力されたグラフ画像が含まれています。

## 内容

- `regression_plot.py`  
  線形回帰による回帰係数（a, b）の算出、決定係数 R² の計算、回帰直線と実測値の可視化を行います。
  入力データは `../data/spring_data.csv` から読み込みます。

- `regression_plot.png`  
  上記スクリプトの出力結果として生成される散布図＋回帰直線のグラフ画像です。

## 実行方法

```bash
python regression_plot.py
