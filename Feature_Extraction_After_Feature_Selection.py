import pandas as pd
import librosa
import numpy as np
from scipy.ndimage import gaussian_filter1d

# get filenames
df = pd.read_csv('./UrbanSound8K.csv', usecols=['slice_file_name', 'fold', 'classID'],
                 dtype={'slice_file_name': str, 'fold': str, 'classID': int})
address_fields = df.to_numpy()

features = np.zeros(shape=(8732, 810), dtype=np.float64)


def pack_features(extracted_feature):
    delta = gaussian_filter1d(extracted_feature, sigma=1, order=1, mode='nearest')
    delta_delta = gaussian_filter1d(extracted_feature, sigma=1, order=2, mode='nearest')
    mean_vector = np.concatenate(
        (np.mean(extracted_feature, axis=1), np.mean(delta, axis=1), np.mean(delta_delta, axis=1)))
    var_vector = np.concatenate((np.var(extracted_feature, axis=1), np.var(delta, axis=1), np.var(delta_delta, axis=1)))
    feature_vector = np.concatenate((mean_vector, var_vector))
    return feature_vector


# load audio samples from filenames and extract their features
for index, item in enumerate(address_fields):
    # show the progress
    print(index)
    # determine the sample's filename
    path = ".//fold" + item[1] + '//' + item[0]
    # load the sample
    audio, sample_rate = librosa.load(path)

    # feature extraction
    # mfcc
    mfc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=128, n_fft=1024)
    # spectral contrast
    cnt = librosa.feature.spectral_contrast(y=audio, sr=sample_rate)

    features[index, 0:768] = pack_features(mfc)
    features[index, 768:810] = pack_features(cnt)

# save the dataset
np.save("dataset.npy", features, allow_pickle=True)
