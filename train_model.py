import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense


train_datagen = ImageDataGenerator(

    rescale=1./255,

    validation_split=0.2,

    rotation_range=20,

    zoom_range=0.2,

    horizontal_flip=True
)


train_generator = train_datagen.flow_from_directory(

    "dataset",

    target_size=(128,128),

    batch_size=32,

    class_mode="categorical",

    subset="training",

    shuffle=True
)


validation_generator = train_datagen.flow_from_directory(

    "dataset",

    target_size=(128,128),

    batch_size=32,

    class_mode="categorical",

    subset="validation",

    shuffle=False
)


# Print the mapping of disease names to numbers
print(train_generator.class_indices)

model = Sequential()

model.add(

    Conv2D(

        32,

        (3,3),

        activation="relu",

        input_shape=(128,128,3)

    )

)

model.add(

    MaxPooling2D(

        pool_size=(2,2)

    )

)

model.add(

    Conv2D(

        64,

        (3,3),

        activation="relu"

    )

)

model.add(

    MaxPooling2D(

        pool_size=(2,2)

    )

)

model.add(Flatten())

model.add(

    Dense(

        128,

        activation="relu"

    )

)

model.add(

    Dense(

        5,

        activation="softmax"

    )

)

model.compile(

    optimizer="adam",

    loss="categorical_crossentropy",

    metrics=["accuracy"]

)

model.fit(

    train_generator,

    validation_data=validation_generator,

    epochs=10

)

model.save(

    "models/crop_model.keras"

)

print("Model Saved Successfully")