from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

# load MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize input and convert to float
x_train, x_test = x_train / 255.0, x_test / 255.0

# build model sequentially
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # flatten 2D(28x28) to 1D
    tf.keras.layers.Dense(128, activation='relu'),  # FC layer, 128 units
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax') # output layer, 10 classification with softmax
])

# compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# train
model.fit(x_train, y_train, epochs=5)

# eval
model.evaluate(x_test, y_test, verbose=2)