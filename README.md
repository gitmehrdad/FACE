[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/face-fast-accurate-and-context-aware-audio/environmental-sound-classification-on)](https://paperswithcode.com/sota/environmental-sound-classification-on?p=face-fast-accurate-and-context-aware-audio)

# FACE: Fast, Accurate and Context-Aware Audio Annotation and Classification

## Abstract
This paper presents a context-aware framework for feature selection and classification procedures to realize a fast and accurate audio event annotation and classification. The context-aware design starts with exploring feature extraction techniques to find an appropriate combination to select a set resulting in remarkable classification accuracy with minimal computational effort. The exploration for feature selection also embraces an investigation of audio Tempo representation, an advantageous feature extraction method missed by previous works in the environmental audio classification research scope. The proposed annotation method considers outlier, inlier, and hard-to-predict data samples to realize context-aware Active Learning, leading to the average accuracy of 90% when only 15% of data possess initial annotation. Our proposed algorithm for sound classification obtained average prediction accuracy of 98.05% on the UrbanSound8K dataset.

## How to reach the paper explaining everything?
Full details are available at https://arxiv.org/abs/2303.03666

## Quick explanation
- "Feature_Extraction_Before_Feature_Selection.py" implements various audio feature extraction methods. After feature extraction, we use our heuristic algorithm for the feature selection.
- "Feature_Extraction_After_Feature_Selection.py" implements feature extraction methods selected by our feature selection algorithm. In this step, we generate the "dataset_US.npy" file, the input of our audio annotation and audio classification methods. We didn't upload the mentioned file because it was too large!


## Citation

```
@misc{face,
  doi = {10.48550/ARXIV.2303.03666}, 
  url = {https://arxiv.org/abs/2303.03666}, 
  author = {Morsali, M. Mehrdad and Mohammadzade, Hoda and Shouraki, Saeed Bagheri},  
  title = {Face: Fast, Accurate and Context-Aware Audio Annotation and Classification}, 
  publisher = {arXiv},  
  year = {2023},
}
```



