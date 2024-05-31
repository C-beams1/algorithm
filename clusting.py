# 导入所需要的库，绘图库，numpy库，sklearn机器学习库内的数据集，聚类，划分数据集方法
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()  # 导入鸢尾花数据集
X = iris.data[:, 0:2]  ##表示我们只取特征空间中的后两个维度
y = iris.target  # 将鸢尾花的标签赋值给y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # 划分鸢尾花数据集，其中训练集占70%，测试集占30%
# 绘制数据分布图
plt.scatter(X[:, 0], X[:, 1], c="red", marker='o', label='iris')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()
estimator = KMeans(n_clusters=3)  # 构造聚类器，将样本聚于3类
estimator.fit(X_train)  # 开始聚类
label_pred = estimator.labels_  # 获取聚类标签
print(estimator.cluster_centers_)  # 获取聚类中心点
# 绘制k-means结果，将训练集聚类后的结果绘图展示，三种颜色表示三类，红色表示第一类，绿色表示第二类，蓝色表示第三类
x0 = X_train[label_pred == 0]
x1 = X_train[label_pred == 1]
x2 = X_train[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')
plt.xlabel('petal length')  # 坐标轴属性
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()
print(estimator.predict(X_test))  # 使用训练出的KMeans模型预测测试集中的数据属于哪一类
# 绘制k-means预测结果，将测试集集聚类后的结果绘图展示，三种颜色表示三类，橘色表示第一类，天蓝色表示第二类，蓝绿色表示第三类。
predict_0 = X_test[estimator.predict(X_test) == 0]
predict_1 = X_test[estimator.predict(X_test) == 1]
predict_2 = X_test[estimator.predict(X_test) == 2]
plt.scatter(predict_0[:, 0], predict_0[:, 1], c="tomato", marker='o', label='predict0')
plt.scatter(predict_1[:, 0], predict_1[:, 1], c="skyblue", marker='*', label='predict1')
plt.scatter(predict_2[:, 0], predict_2[:, 1], c="greenyellow", marker='+', label='predict2')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()
