# -*- coding: utf-8 -*-

import tensorflow as tf

hello = tf.constant('Hello world')
sess = tf.Session()
print sess.run(hello)

a = tf.constant(3)
b = tf.constant(6)

print sess.run(a+b)
