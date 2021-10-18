# ---------------------------------------------------------------------------
# Description: This is a Quick Check if all necessary libraries are installed.
# Authors:   Julian Ramme, Sigrid Hafner
# Copyright:   Free to use
# Version:   1.0.3
# Maintainer:   Ramme, Hafner
# E-Mail:  ramme.julian@fh-swf.de, hafner.sigrid@fh-swf.de
# Status:  Alpha
# Creation Date:  25-08-2021
# Last Edit:   06-10-2021
# Python-Version:  3.7.9 - 64-bit
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Please hit F5 and Enter.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import initializers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
import pandas as pd
import seaborn as sns
# ---------------------------------------------------------------------------

# diese zeile schreibe ich als test
# Test  Libraries
# ---------------------------------------------------------------------------
# 1. Numpy
arr = np.array([12, 45., 3.], dtype=complex)
print(arr)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 2. Matplotlib in combination with Numpy
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.title("Fig 1: Matplotlib, Numpy successfull, close window to continue")
plt.show()
print("Test Matplotlib successfull")
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 3. Random
arr2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr2)
random.seed(4)
random.shuffle(arr2)
print(arr2)
print("Test for random function successfull")
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 4. Keras
train_data = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [0, 0, 0],
                       [0, 1, 1], [1, 0, 1], [1, 1, 0]])
X = train_data[:, 0:2]
Y = train_data[:, 2]
model = Sequential()
model.add(Dense(2, input_dim=2, activation='tanh', use_bias=True,
                kernel_initializer=initializers.RandomNormal(seed=1)))
model.compile(loss=losses.binary_crossentropy,
              optimizer=optimizers.Adadelta(learning_rate=1,
                                            rho=0.95, epsilon=1e-08),
              metrics=['accuracy'])
history = model.fit(X, Y, validation_split=0.5, epochs=300, batch_size=4,
                    verbose=1)
print("Test for Keras successfull")
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 5. Pandas
s = pd.Series([5, 10, 15, 20, 25])
print(s)
print("Test for Pandas successfull")
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 6. Seaborn and Matplotlib
tips = sns.load_dataset("tips")
sns.violinplot(x="total_bill", data=tips)
plt.title("Fig 2:Seaborn and Matplotlib successfull, close window to continue")
plt.show()
print("All libraries are succesfully installed!")
# ---------------------------------------------------------------------------