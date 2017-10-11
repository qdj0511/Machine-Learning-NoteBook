# -*- coding:utf-8 -*-

from __future__ import print_function

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline


#生成数据
train_x = np.linspace(-1, 1 , 200)
train_y = 2* train_x + np.random.randn(*train_x.shape)*0.2

#线性回归参数
learning_rate = 0.01
training_epochs = 1000
display_step = 50

n_sample = train_x.shape[0]


#定义模型的输入输出
X = tf.placeholder("float")
#X = tf.placeholder('float')
Y = tf.placeholder('float')

#定义模型变量

W = tf.Variable(np.random.randn() , name='weight')
b = tf.Variable(np.random.randn() , name='bias')


#定义模型

pred = tf.add(tf.multiply(X,W) , b )

#定义损失函数

cost = tf.reduce_sum(tf.pow(pred - Y , 2))/(2*n_sample)

#创建优化项

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)


init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_x, train_y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch + 1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_x, Y: train_y})
            print("Epoch:", '%04d' % (epoch + 1), "cost=", "{:.9f}".format(c), \
                  "W=", sess.run(W), "b=", sess.run(b))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_x, Y: train_y})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')

    # Graphic display
    plt.plot(train_x, train_y, 'ro', label='Original data')
    plt.plot(train_x, sess.run(W) * train_y + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

    # Generate the test data
    test_X = np.linspace(-1, 1, 100)
    test_Y = 2 * test_X + np.random.randn(*test_X.shape) * 0.2

    print("Testing... (Mean square loss Comparison)")
    testing_cost = sess.run(
        tf.reduce_sum(tf.pow(pred - Y, 2)) / (2 * test_X.shape[0]),
        feed_dict={X: test_X, Y: test_Y})  # same function as cost above
    print("Testing cost=", testing_cost)
    print("Absolute mean square loss difference:", abs(
        training_cost - testing_cost))

    plt.plot(test_X, test_Y, 'bo', label='Testing data')
    plt.plot(train_x, sess.run(W) * train_x + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()


# print (train_x , train_y)
# plt.plot(train_x , train_y , color='r')
# plt.title("Training Data")
# plt.xlim([-1.5 , 1.5])
#
# plt.show()
