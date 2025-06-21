import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.rcParams["font.family"] = [
    "Hiragino Sans", "Meiryo", "IPAexGothic", "sans-serif",
]

# このスクリプトのあるディレクトリを取得
base_dir = os.path.dirname(__file__)
# データファイルへのパス構築
data_path = os.path.join(base_dir, "..", "data", "spring_data.csv")
# CSV読み込み
df = pd.read_csv(data_path)

# データ (x = 重さ, y = バネの長さ)
x = df["weight"].values
y = df["length"].values

# x, y の平均を求める
x_mean = np.mean(x)
y_mean = np.mean(y)

# 傾き a の計算式(共分散 / 分散) : Σ((x - x̄)(y - ȳ)) / Σ((x - x̄)^2)
a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)

# 切片 b の計算式：b = ȳ - a * x̄
b = y_mean - a * x_mean

# 回帰直線の予測値を計算　(pred = 予測)
y_pred = a * x + b

# 決定係数 R² の計算 (1- (誤差の合計 / 全体の変動量)
ss_total = np.sum((y - y_mean) ** 2)  # 全体のばらつき
ss_residual = np.sum((y - y_pred) ** 2)  # 予測からのズレ(誤差)
r2 = 1 - (ss_residual / ss_total) #「直線でどのくらい説明できたか」の割合

# 結果表示
print(f"回帰式: y = {a:.3f}x + {b:.3f}")
print(f"決定係数 R² = {r2:.3f}")

# グラフ描画
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label="実測値", color="#1f77b4", s=50)
plt.plot(x, y_pred, label=f"回帰直線: y = {a:.2f}x + {b:.2f}", color="#ff7f0e")
plt.xlabel("重さ [g]", fontsize=12)
plt.ylabel("バネの長さ [mm]", fontsize=12)
plt.title(f"重さとバネの長さの関係 （線形回帰）\nR² = {r2:.3f}", fontsize=14)
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
