import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split

IMG_SIZE = 24
DATA_DIR = "dataset"

data = []
labels = []

for label, folder in enumerate(["closed", "open"]):
    folder_path = os.path.join(DATA_DIR, folder)
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img = img / 255.0

        data.append(img)
        labels.append(label)

X = np.array(data).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

np.save("X_train.npy", X_train)
np.save("X_test.npy", X_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy", y_test)

print("Preprocessing done.")
print("Train samples:", len(X_train))
print("Test samples:", len(X_test))
