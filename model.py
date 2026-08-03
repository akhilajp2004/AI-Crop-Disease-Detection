from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

# Create CNN model
model = Sequential()

# First Convolution Layer
model.add(
    Conv2D(
        32,
        (3,3),
        activation="relu",
        input_shape=(128,128,3)
    )
)

# Pooling Layer
model.add(
    MaxPooling2D(pool_size=(2,2))
)

# Second Convolution Layer
model.add(
    Conv2D(
        64,
        (3,3),
        activation="relu"
    )
)

# Pooling Layer
model.add(
    MaxPooling2D(pool_size=(2,2))
)

# Flatten Layer
model.add(
    Flatten()
)

# Hidden Layer
model.add(
    Dense(
        128,
        activation="relu"
    )
)

# Output Layer
model.add(
    Dense(
        5,
        activation="softmax"
    )
)

print(model.summary())