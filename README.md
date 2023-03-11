[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/face-fast-accurate-and-context-aware-audio/environmental-sound-classification-on)](https://paperswithcode.com/sota/environmental-sound-classification-on?p=face-fast-accurate-and-context-aware-audio)
# FACE
Feature extraction, Feature selection, Audio Event Labeling, and Sound Classification on the UrbanSound8K dataset.


If you enjoy reading papers, full details are available at https://arxiv.org/abs/2303.03666

## Abstract
This paper presents a context-aware framework for feature selection and classification procedures to realize a fast and accurate audio event annotation and classification. The context-aware design starts with exploring feature extraction techniques to find an appropriate combination to select a set resulting in remarkable classification accuracy with minimal computational effort. The exploration for feature selection also embraces an investigation of audio Tempo representation, an advantageous feature extraction method missed by previous works in the environmental audio classification research scope. The proposed annotation method considers outlier, inlier, and hard-to-predict data samples to realize context-aware Active Learning, leading to the average accuracy of 90% when only 15% of data possess initial annotation. Our proposed algorithm for sound classification obtained average prediction accuracy of 98.05% on the UrbanSound8K dataset.


This is how we do things:
1- The file entitled "Feature_Extraction_Before_Feature_Selection.py" contains the feature extraction codes used by our heuristic algorithm for the feature selection.
2- The file entitled "Feature_Extraction_After_Feature_Selection.py" contains the codes for feature extraction methods selected by our feature selection algorithm.
3- We utilize the output file of the second stage in further stages. We didn't upload the mentioned file because it was too large! Nevertheless, generating that file is easy: just put "Feature_Extraction_After_Feature_Selection.py" next to the US8K dataset's audio fold files and run it!
