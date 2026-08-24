# Project Overview
This project aims to classify brain synapses into excitatory and inhibitory types using 2D electron microscopy (EM) patches and 3D image cubes extracted from the MICrONS dataset. Our best 2D model was the ResNet-50 model @ 76.89% accuracy. Our best 3D model was...


# Setup
#### 1. Clone the repository (or click download):
```
git clone https://github.com/<your_repo>.git
cd <your_repo>
```

#### 2. Install dependencies (or install manually on Anaconda Prompt)
```
pip install -r requirements.txt
```

# Running the Demos

#### 1. Download the 2D model and 2D dataset and place them in the checkpoints and data folder respectively:

###### Google Drive Links

2D ResNet-50 Model w/ 76.89% Accuracy:
https://drive.google.com/file/d/1CUZ2VUxfnIqTzDNdOPkU1feiZv1Qau1f/view?usp=sharing

2D 256x256 Dataset:
https://drive.google.com/drive/folders/1YyoQjH1dlb3aOVXdFJ3UI226gsIorvmC?usp=sharing

#### 2. Open and run demo2d.ipynb

# Expected Output

After you run demo2d.ipynb, you should see the testing accuracy listed, the example true vs predicted images, and then the confusion matrix + metrics. There are no outputs to the results folder since all the results are within the demo notebook.

# Pre-trained Model Link:

###### Google Drive Links

2D ResNet-50 Model w/ 76.89% Accuracy:
https://drive.google.com/file/d/1CUZ2VUxfnIqTzDNdOPkU1feiZv1Qau1f/view?usp=sharing

# Acknowledgements:
Thank you to MICrONS and the Allen Institute. 


# Reproducibility (and more)

## About the src Folder...

### You will find several notebooks:

#### TeamProjectResnetModelTrain.ipynb
This notebook trains a ResNet model (either ResNet-18 or Resnet-50) on the 2D image datset (either 128x128 or 256x256) and saves the model. You can see example training and validation accuracy of the trained model in the notebook.

For this notebook you can currently find in the /src folder, we trained the network for 30 epochs with a batch size of 32 and an initial learning rate of 0.0005. We used the Adam optimizer along with a cross-entropy loss function, which is standard for two-class classification tasks. To improve convergence, we applied a cosine annealing learning-rate scheduler with $T_{max} = 30$, which gradually reduces the learning rate over the course of training. All training was performed end-to-end using ImageNet-pretrained ResNet backbones, with inputs resized to 256×256 and normalized using ImageNet mean and standard deviation. We also applied several data augmentation strategies—including horizontal and vertical flips, small rotations, Gaussian blur, and color jitter—to improve generalization. To ensure reproducibility, a fixed random seed of 42 was used for Python, NumPy, and PyTorch.

#### TeamProjectExtractImages.ipynb
This notebook utilizes MICrONS tools to extract a dataset of 2D images of excitatory and inhibitory matrix. The train, val, and test set all have their unique neurons and synapses to avoid data leakage. This notebook took 1+ hour to run.

#### TeamProjectCNNModelTrain.ipynb
This notebook trains a custom CNN model (either on 128x128 or 256x256 data) and saves it. You can see example training and validation accuracy of the trained model in the notebook.

For this notebook you can currently find in the /src folder, the custom CNN is trained on 256×256 EM patches, we used a batch size of 32 and trained the model for 30 epochs. The learning rate was set to 0.00025, and optimization was performed using the Adam optimizer. As with the ResNet experiments, we used cross-entropy loss for the binary excitatory vs. inhibitory classification task. No learning-rate scheduler was used for this architecture, allowing the model to train with a fixed learning rate throughout all epochs. All reproducibility controls, including setting the random seed, were kept consistent like the ResNet notebook.

# 3-D Notebooks

Add information here
