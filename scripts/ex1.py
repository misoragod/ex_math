#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
軸に関する鏡映変換
鏡映変換 (反転・折り返し) は基本的な線型変換です。
任意の点をx軸に関して折り返す
"""
# Python_Reflection
# In[1]

import numpy as np
import matplotlib.pyplot as plt

# ここにcoordinate()を実装
# ここにpointer()を実装

# FigureとAxes
fig = plt.figure(figsize = (5, 5))
ax = fig.add_subplot(111)

# FigureとAxes
fig = plt.figure(figsize = (6, 6))
ax = fig.add_subplot(111)

# 座標を準備
coordinate(ax, [-6, 6], [-6, 6])

# 鏡映行列aを定義
a = np.array([[1,  0],
              [0, -1]])

# 変換前の点
p0 = np.array([3, 3])

# 変換後の点
p1 = np.dot(a, p0)

# 変換前の点p0をプロット
pointer(ax, p0[0], p0[1], "P0",
        pcolor = "red", textsize = 15)

# 変換前の後の点p1をプロット
pointer(ax, p1[0], p1[1], "P1",
        pcolor = "blue", textsize = 15)

plt.show()