# Image-Manipulation-Detection
Classifies a given image as authentic or tampered by doing two levels of analysis. <br>
Level 1 - Metadata analysis, to find any software signatures in the metadata of the image. <br>
Level 2 - Feature Engineering(Error Level Analysis) and CNNs for classification. [Error Level Analysis(ELA)](http://fotoforensics.com/tutorial-ela.php) is a compression method for finding the region which is tampared. This output is given as input to the CNN for classification. <br>
The model is trained and validated on CASIA dataset. It has JPEG images of **copy-move** and **spliced** tampared images.

## How To Run
**Flags**
> -p or --path: Image pathname (required) <br>

`$ python main.py -p pathname` <br>
