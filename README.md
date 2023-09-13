# About this project

This research project was developed during my studies in Cartographic Engineering at the Military Institute of Engineering.

The main objective was to implement UNet for the semantic segmentation of deforestation areas in satellite images.

Initially, we obtained satellite images from Sentinel-2A with 4 bands (R, G, B, and NIR) using the Google Earth Engine API.

The obtained images correspond to a region in the Amazon Rainforest in the Kayapó Area, Piauí, Brazil.

Next, we created ground truth masks for deforestation areas in these images based on geospatial files available at http://terrabrasilis.dpi.inpe.br/downloads/, which correspond to the study area.

The following steps involved adapting an application of a convolutional neural network for performing semantic segmentation of deforestation areas.

For this purpose, we adapted an application from https://github.com/StephenTaylor1998/tif-UNet-master to obtain the model definition of UNet and perform training and prediction.

All the code is written in Python using the PyTorch framework.






