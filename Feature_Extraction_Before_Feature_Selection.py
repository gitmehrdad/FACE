import pandas as pd
import librosa
import numpy as np
from scipy.ndimage import gaussian_filter1d
from sklearn.preprocessing import QuantileTransformer

# get filenames
df = pd.read_csv('./UrbanSound8K.csv', usecols=['slice_file_name', 'fold', 'classID'],
                 dtype={'slice_file_name': str, 'fold': str, 'classID': int})
address_fields = df.to_numpy()

features = np.zeros(shape=(8732, 1998), dtype=np.float64)


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
    # polynomial fitting
    ply = librosa.feature.poly_features(y=audio, sr=sample_rate, order=5)
    # spectral contrast
    cnt = librosa.feature.spectral_contrast(y=audio, sr=sample_rate)
    # chroma
    chm = librosa.feature.chroma_stft(y=audio, sr=sample_rate)
    # tonnetz
    tnz = librosa.feature.tonnetz(y=audio, sr=sample_rate, bins_per_octave=72)

    # tempogram
    tmp = librosa.feature.tempogram(y=audio, sr=sample_rate, win_length=172)
    # rms
    rms = librosa.feature.rms(y=audio)
    # zero crossing rate
    zcr = librosa.feature.zero_crossing_rate(y=audio, frame_length=2048)

    features[index, 0:768] = pack_features(mfc)
    features[index, 768:804] = pack_features(ply)
    features[index, 804:846] = pack_features(cnt)
    features[index, 846:918] = pack_features(chm)
    features[index, 918:954] = pack_features(tnz)
    features[index, 954:1986] = pack_features(tmp)
    features[index, 1986:1992] = pack_features(rms)
    features[index, 1992:1998] = pack_features(zcr)

features[:, 0:768] = QuantileTransformer(n_quantiles=5000).fit_transform(features[:, 0:768])
features[:, 768:804] = QuantileTransformer(n_quantiles=5000).fit_transform(features[:, 768:804])
features[:, 804:846] = QuantileTransformer(n_quantiles=5000).fit_transform(features[:, 804:846])
features[:, 846:918] = QuantileTransformer(n_quantiles=5000).fit_transform(features[:, 846:918])
features[:, 918:954] = QuantileTransformer(n_quantiles=5000).fit_transform(features[:, 918:954])
features[:, 954:1986] = QuantileTransformer(n_quantiles=5000).fit_transform(features[:, 954:1986])
features[:, 1986:1992] = QuantileTransformer(n_quantiles=5000).fit_transform(features[:, 1986:1992])
features[:, 1992:1998] = QuantileTransformer(n_quantiles=5000).fit_transform(features[:, 1992:1998])

# save the dataset
np.save("dataset.npy", features, allow_pickle=True)
