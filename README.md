# Speaker-identification-using-GMMs

Wishing to learn more about Python and Machine Learning, I did the final project for my "Fractals in Engineering" course on speaker identification using Python and ML.

The base code was written by Abhijeet Kumar. (<a href = "https://github.com/abhijeet3922/Speaker-identification-using-GMMs">Repository here</a>.)

It uses the popular Machine Learning technique Gaussian Mixture Models (GMM) to train speaker identification models.

The original documentation/tutorial can be found <a href="https://appliedmachinelearning.wordpress.com/2017/11/14/spoken-speaker-identification-based-on-gaussian-mixture-models-python-implementation/">here</a>.



## Modifications

This version has been updated to run on Python 3.

Additional code has been added to allow for visualization of the data waveform, spectrogram, and Mel frequency spectorgram.


## Data-set:

The <a href="https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html">Speech Commands Dataset</a> from TensorFlow and Google AIY was used for this project.


6 speakers were randomly selected based on the number of voice clips available.

All voice clips were trimmed to isolate the command word and zero-padded to create 1-second clips using Audacity.

Training data: Up to 11 voice clips/speaker were used, and included the words "yes, no, stop, go, up".

Test data: One unseen voice clip ("no") for the same 6 speakers were tested. 


## Installation

In order to run this code:

1.  Install Anaconda 64-bit Python 3.9 (https://www.anaconda.com/products/distribution)
2.  pip install python_speech_features (for extracting MFCC features)
3.  pip install librosa (for data visualization)

Note : Directory path used for train and test data in code train_models.py and test_speaker.py needs to be properly set depending upon the path where you download the data-set.


## Future Work

Due to the small dataset used, the model was only successful about 2/3 of the time at identifying the speaker. To improve the performance, more voice samples (available in the main Speech Commands Dataset) will likely be needed for training.

Other ML/DL models could be implemented instead / in addition to GMM.

It should also be possible to extend this model to perform speech recognition and speaker verification.
