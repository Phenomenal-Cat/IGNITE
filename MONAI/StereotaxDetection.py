


import os
import torch
import monai
import nibabel as nib
import numpy as np
from torch.utils.data import DataLoader, Dataset
from monai.transforms import (Compose, LoadImage, AddChannel, Resized, ToTensor)
from monai.networks.nets import UNet
from monai.losses import MSELoss
from monai.optimizers import Novograd
from sklearn.model_selection import train_test_split




# Define a custom Dataset class for loading MRI images and landmarks
class MRILandmarkDataset(Dataset):
    def __init__(self, image_paths, landmark_coords, transform=None):
        """
        :param image_paths: List of paths to the MRI images (NIfTI files).
        :param landmark_coords: Corresponding landmark coordinates (Nx3 for 3D).
        :param transform: Transformations to apply to the data.
        """
        self.image_paths = image_paths
        self.landmark_coords = landmark_coords
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        landmark = self.landmark_coords[idx]
        
        # Load the MRI image
        img = nib.load(image_path).get_fdata()
        img = np.expand_dims(img, axis=0)  # Add a channel dimension
        
        sample = {"image": img, "landmarks": landmark}
        
        if self.transform:
            sample = self.transform(sample)
        
        return sample


transform = Compose([
    LoadImage(image_only=True),  # Load the image as a 3D array
    AddChannel(),  # Add a channel dimension (needed for CNNs)
    Resized(spatial_size=(64, 64, 64)),  # Resize to a fixed size (e.g., 64x64x64)
    ToTensor(),  # Convert to tensor format
])

class LandmarkDetectionModel(monai.networks.nets.UNet):
    def __init__(self, spatial_dims=3, in_channels=1, out_channels=3, **kwargs):
        super().__init__(spatial_dims=spatial_dims, in_channels=in_channels, out_channels=out_channels, **kwargs)
    
    def forward(self, x):
        # Forward pass using the UNet architecture
        return super().forward(x)


# Loss function: MSELoss for regression
loss_function = MSELoss()

# Optimizer: Novograd or Adam
optimizer = Novograd(model.parameters(), lr=1e-4)


# Prepare training and validation datasets
image_paths = ['path_to_mri_image_1.nii', 'path_to_mri_image_2.nii', ...]  # List of image paths
landmark_coords = np.array([[x1, y1, z1], [x2, y2, z2], ...])  # List of 3D landmark coordinates

# Split into training and validation sets
train_image_paths, val_image_paths, train_landmark_coords, val_landmark_coords = train_test_split(image_paths, landmark_coords, test_size=0.2, random_state=42)

train_dataset = MRILandmarkDataset(train_image_paths, train_landmark_coords, transform=transform)
val_dataset = MRILandmarkDataset(val_image_paths, val_landmark_coords, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=4, shuffle=False)

# Initialize the model
model = LandmarkDetectionModel(spatial_dims=3, in_channels=1, out_channels=3)

# Training loop
num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for batch in train_loader:
        images = batch['image'].float().cuda()  # Load data to GPU
        landmarks = batch['landmarks'].float().cuda()

        # Zero gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(images)

        # Compute loss
        loss = loss_function(outputs, landmarks)
        
        # Backpropagation
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    avg_train_loss = running_loss / len(train_loader)
    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {avg_train_loss:.4f}')

    # Validation loop (optional)
    model.eval()
    with torch.no_grad():
        val_loss = 0.0
        for batch in val_loader:
            images = batch['image'].float().cuda()
            landmarks = batch['landmarks'].float().cuda()

            outputs = model(images)
            val_loss += loss_function(outputs, landmarks).item()

        avg_val_loss = val_loss / len(val_loader)
        print(f'Validation Loss: {avg_val_loss:.4f}')



# Evaluate the model on a sample
model.eval()
with torch.no_grad():
    sample = val_dataset[0]  # Use an example from the validation dataset
    image = sample['image'].unsqueeze(0).float().cuda()  # Add batch dimension and move to GPU
    true_landmarks = sample['landmarks']

    # Predict landmarks
    predicted_landmarks = model(image)

    print(f"True Landmarks: {true_landmarks}")
    print(f"Predicted Landmarks: {predicted_landmarks.cpu().numpy()}")
