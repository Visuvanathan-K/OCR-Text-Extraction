import pandas as pd
import numpy as np

from glob import glob
import matplotlib.pyplot as plt
from PIL import Image

# Load data
annot = pd.read_parquet('annot.parquet')
imgs = pd.read_parquet('img.parquet')
img_fns = glob('train_val_images/*.jpg')

# Show image
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(plt.imread(img_fns[0]))
ax.axis('off')
plt.show()