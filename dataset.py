import os
import tifffile
import rasterio
from torch.utils.data import Dataset
import numpy as np

class DesflorestDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.images = os.listdir(image_dir)

    def __len__(self): 
        return len(self.images)

    def __getitem__(self, index):
        img_path = os.path.join(self.image_dir, self.images[index])
        mask_path = os.path.join(self.mask_dir, self.images[index].replace(".tif", "_mask.tif"))
        with rasterio.open(img_path) as src:
            image = np.moveaxis(src.read(), 0, -1)
        mask = tifffile.imread(mask_path)
        mask[mask == 255] = 1

        if self.transform is not None:
            augmentations = self.transform(image=image, mask=mask)
            image = augmentations["image"]
            mask = augmentations["mask"]

        return image, mask
