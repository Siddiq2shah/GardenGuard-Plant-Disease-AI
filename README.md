# GardenGuard: Mobile-Optimized Plant Disease Detection

GardenGuard is an AI-powered diagnostic tool designed to help beginner gardeners identify plant diseases quickly and accurately using a smartphone. By leveraging **Transfer Learning** and the **MobileNetV2** architecture, this project achieves high-performance results while remaining lightweight enough for mobile deployment.

## 🚀 Key Achievements
* **High Accuracy:** Achieved a **94.2% accuracy** rate on the final test set.
* **Mobile-First Design:** Selected MobileNetV2 for its **Depthwise Separable Convolutions**, making it **7x smaller** (~14 MB) than standard baselines like ResNet-50 (~98 MB).
* **Robust Data Pipeline:** Implemented **Data Augmentation** (rotations, flips, zooms) to prevent the model from memorizing training images.
* **Efficient Inference:** The model is optimized to run 10x faster than older models like VGG16 without significant accuracy loss.

## 🛠️ Technical Stack
* **Frameworks:** TensorFlow / Keras, Python.
* **Architecture:** MobileNetV2 (Pre-trained on ImageNet).
* **Optimizer:** Adam with Categorical Cross-Entropy loss.
* **Dataset:** PlantVillage via Kaggle (54,000+ images).

## 📊 Performance Analysis
The model was tested across multiple plant types, demonstrating high reliability in distinct structures while identifying biological similarities as a challenge for AI.

| Plant Type | Accuracy | Major Finding |
| :--- | :--- | :--- |
| **Corn** | 98.4% | Distinct linear leaf structure makes identification easy. |
| **Apple** | 97.8% | Highly distinct disease markers. |
| **Tomato** | 91.5% | Occasional confusion with Potato due to biological relation (Solanaceae family). |
| **Potato** | 88.2% | "Early Blight" looks nearly identical on both potato and tomato leaves. |

## 👥 Project Team & Roles
* **Mohammad Shaheer Siddiqi (Project Lead):** Architected the MobileNetV2 implementation and managed the project scope pivot.
* **Abdul Kader:** Lead Implementer for data augmentation and training scripts.
* **Zhouyang Chen:** Implementer focused on the training loop and validation metrics.
* **Daniyal Siddiqui:** Lead Technical Writer and performance analyst.

## 📖 Lessons Learned
* **Accuracy/Efficiency Trade-off:** Choosing MobileNetV2 meant sacrificing 2.3% accuracy for a model that is 7x smaller and mobile-ready.
* **Data Quality:** AI performance is strictly tied to photo quality; factors like "Background Noise" or "Early Stages" of disease can impact confidence.
* **Addressing Class Imbalance:** Noticed lower accuracy in Potato classes due to having significantly fewer training images than Tomato.

---

### How to Run
1. Ensure `TensorFlow`, `Keras`, and `Matplotlib` are installed.
2. Download the **PlantVillage** dataset from Kaggle.
3. Run `train_model.py` to train the CNN and generate the `gardenguard_model.h5` file.
