# -*- coding:utf-8 -*-
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (RandomTreesEmbedding, RandomForestClassifier,
                              GradientBoostingClassifier)
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.pipeline import make_pipeline

np.random.seed(100)
n_estimator = 10

X, y = make_classification(n_samples=80000)
#print X.shape
# 切分为测试集和训练集，比例0.3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# 将训练集切分为两部分，一部分用于训练GBDT模型，另一部分输入到训练好的GBDT模型生成GBDT特征，然后作为LR的特征。
# 这样分成两部分是为了防止过拟合。
X_train, X_train_lr, y_train, y_train_lr = train_test_split(X_train, y_train, test_size=0.5)

# 调用GBDT分类模型。
grd = GradientBoostingClassifier(n_estimators=n_estimator)

# 调用one-hot编码。
grd_enc = OneHotEncoder()

# 调用LR分类模型。
grd_lm = LogisticRegression()

'''使用X_train训练GBDT模型，后面用此模型构造特征'''
grd.fit(X_train, y_train)


print grd.apply(X_train)[:, :, 0].shape
grd_enc.fit(grd.apply(X_train)[:, :, 0])

grd_lm.fit(grd_enc.transform(grd.apply(X_train_lr)[:, :, 0]), y_train_lr)
# 用训练好的LR模型多X_test做预测
y_pred_grd_lm = grd_lm.predict_proba(grd_enc.transform(grd.apply(X_test)[:, :, 0]))[:, 1]
# 根据预测结果输出
fpr_grd_lm, tpr_grd_lm, _ = roc_curve(y_test, y_pred_grd_lm)

plt.figure(figsize=(12,8))
plt.subplot(1,2,1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_grd_lm, tpr_grd_lm, label='GBT + LR')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve')
plt.legend(loc='best')


plt.subplot(1,2,2)
plt.xlim(0, 0.2)
plt.ylim(0.8, 1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_grd_lm, tpr_grd_lm, label='GBT + LR')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve (zoomed in at top left)')
plt.legend(loc='best')
plt.show()