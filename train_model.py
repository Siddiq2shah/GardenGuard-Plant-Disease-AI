import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import os

# ==========================================
# GARDENGUARD: PLANT DISEASE DETECTION MODEL
# Authors: Mohammad, Abdul, Daniyal, Zhouyang
# ==========================================

# 1. Configuration
# We use 224x224 because it is the standard input size for MobileNetV2
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
# Replace this with the path to your downloaded PlantVillage dataset
DATASET_DIR = './PlantVillage' 

def train_gardenguard_model():
    """
    Builds and trains the Convolutional Neural Network (CNN)
    using Transfer Learning.
    """
    
    # 2. Data Augmentation
    # We apply rotations and flips to prevent the model from memorizing specific images.
    train_datagen = ImageDataGenerator(
        rescale=1./255,         # Normalize pixel values to 0-1
        rotation_range=20,      # Rotate images randomly
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        validation_split=0.2    # Use 20% of data for testing/validation
    )

    print("Loading Training Data...")
    train_generator = train_datagen.flow_from_directory(
        DATASET_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    print("Loading Validation Data...")
    validation_generator = train_datagen.flow_from_directory(
        DATASET_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    # 3. Model Architecture: Transfer Learning
    # We use MobileNetV2 pre-trained on ImageNet.
    # Why? It is lightweight and faster than VGG16, making it better for our use case.
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,      # Exclude the final classification layer
        input_shape=(224, 224, 3)
    )

    # Freeze the base model layers so we don't destroy the pre-trained features
    base_model.trainable = False

    # Add our custom classification head
    inputs = Input(shape=(224, 224, 3))
    x = base_model(inputs, training=False)
    x = GlobalAveragePooling2D()(x) # Condense feature maps into a single vector
    x = Dropout(0.2)(x)             # Regularization to prevent overfitting
    outputs = Dense(train_generator.num_classes, activation='softmax')(x)

    model = Model(inputs, outputs)

    # 4. Compilation
    model.compile(
        optimizer=Adam(learning_rate=0.0001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    model.summary()

    # 5. Training
    print("Starting Training...")
    history = model.fit(
        train_generator,
        epochs=10, # Lower epochs for demonstration; 20-50 recommended for production
        validation_data=validation_generator
    )

    # 6. Save the Model
    model.save('gardenguard_model.h5')
    print("Model saved as gardenguard_model.h5")

    # 7. Plot Results
    plot_history(history)

def plot_history(history):
    """
    Helper function to visualize accuracy over time.
    """
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    epochs = range(len(acc))

    plt.figure(figsize=(8, 8))
    plt.plot(epochs, acc, label='Training Accuracy')
    plt.plot(epochs, val_acc, label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend(loc='lower right')
    plt.show()

if __name__ == "__main__":
    # Check if data directory exists before running
    if os.path.exists(DATASET_DIR):
        train_gardenguard_model()
    else:
        print(f"Error: Dataset not found at {DATASET_DIR}")
        print("Please download the PlantVillage dataset to run this script.")