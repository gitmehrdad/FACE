[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/face-fast-accurate-and-context-aware-audio/environmental-sound-classification-on)](https://paperswithcode.com/sota/environmental-sound-classification-on?p=face-fast-accurate-and-context-aware-audio)
# FACE
Urban Sound Annotation and Classification
Full details are available at https://arxiv.org/abs/2303.03666


Feature extraction, Feature selection, Audio Event Labeling, and Sound Classification on the UrbanSound8K dataset.

This is how we do things:
1- The file entitled "Feature_Extraction_Before_Feature_Selection.py" contains the feature extraction codes used by our heuristic algorithm for the feature selection.
2- The file entitled "Feature_Extraction_After_Feature_Selection.py" contains the codes for feature extraction methods selected by our feature selection algorithm.
3- We utilize the output file of the second stage in further stages. We didn't upload the mentioned file because it was too large! Nevertheless, generating that file is easy: just put "Feature_Extraction_After_Feature_Selection.py" next to the US8K dataset's audio fold files and run it!
