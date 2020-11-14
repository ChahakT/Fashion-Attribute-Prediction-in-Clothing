# Fashion Attribute Prediction in Clothing

**Introduction and Motivation**

Fashion industry is always evolving and it is important to
keep up with the latest demands. For example, we need to
know where can we buy a particular dress or what attributes
it contains or what is that outfit called. Modeling the rich
semantic information and their dependencies is essential for
image understanding.
We use CNNs for multi-label classification by transforming
into multiple single-label classification problems. But when
data is insufficient , we pretrain on Imagenet database and
then create the last layer n train it on our own data.
The label semantic redundancy can be exploited by joint
image/label embedding by sharing classification parameters
for semantically similar labels.

**Datasets**

We have evaluated different methods on these 2
apparel datasets:

1) Clothing Attribute Dataset, Stanford Digital
Repository

2) Deep Fashion dataset, Multimedia Laboratory,
The Chinese University of Hong Kong 

**Methods and Models**

1) Convolutional Neural Network 

2) GoogLeNet with Fine Tuning

3) CNN-RNN multimodal embedding

**Convolutional Neural Network**

We create a classic CNN consisting of alternatively stacked convolution layers and pooling layers. These are followed by
fully connected layers at the end of CNN to use the features predicted to make a predictions. The convolution layer
extracts local features with a series of convolution filters .The rectified linear unit (ReLU) activation is an optimal choice
using as the activation function f(⋅) for its rapid convergence properties.

**GoogLeNet with Fine Tuning**

The second strategy is to replace and retrain the classifier on top of the ConvNet on the new dataset, but to also fine-tune the
weights of the pretrained network by continuing the backpropagation. GoogleNet/Inception net is a deep CNN used to
predict 1000 categories in the Imagenet database.We pre train it with Imagenet data and then we fine tune LeNet with our
Clothing Attribute Dataset and DeepFashion and change evaluation step for multi-label attribute prediction in Tensorflow.

**CNN-RNN multimodal embedding**

We use Recurrent neural networks to map the
attributes and Convolutional Neural Networks to
map corresponding images in the multimodal
embedding space. The image and attribute’s low
dimensional features are mapped into a common
join embedding Euclidean space such that features
of semantically similar attributes are mapped closer
to each other and similarly attributes and its
corresponding image features are mapped closer to
each other. This embedding captures the semantic
understanding between images and its labels


**Conclusion**

We observe the results of attribute prediction through different methods. Fine-tuning on Imagenet gives better results than
Simple CNN.We propose a CNN-RNN framework for multilabel image classification. This work is inspired by multimodal
embedding used in image captioning. The proposed framework combines the advantages of the joint image/label
embedding by employing CNN and RNN to model the label dependency in a joint image/label embedding space.
Experimental results on several fashion benchmark datasets demonstrate that the proposed approach achieves good
performance in the fashion problem statement and is comparable to the state of the art for multilabel classification of non
apparel images.
