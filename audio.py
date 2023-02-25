import os
import base64
import pandas as pd
import librosa
import tempfile
import numpy as np
import streamlit as st

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=30)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rmse = librosa.feature.rms(y=y)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    features = {'filename': os.path.basename(file_path),
                'chroma_stft': chroma_stft.mean(),
                'rmse': rmse.mean(),
                'spectral_centroid': spec_cent.mean(),
                'spectral_bandwidth': spec_bw.mean(),
                'rolloff': rolloff.mean(),
                'zero_crossing_rate': zcr.mean()}
    for i, c in enumerate(mfcc):
        features[f'mfcc{i + 1}'] = c.mean()
    return features

def download_csv(data):
    csv_file = data.to_csv(index=False)
    b64 = base64.b64encode(csv_file.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV file</a>'
    return href

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def chart_data(features_df):
    # st.write(features_df.columns)
    
    cols = st.multiselect('select columns:', features_df.columns, default=[])
    
    # st.write('You selected:', cols)

    # show dataframe with the selected columns
    st.write(features_df[cols])

    chart_data = pd.DataFrame(
    features_df,
    # features_df._get_value( features_df[cols]),
    columns=cols)
    
    return st.bar_chart(chart_data)

def main():
    st.title("Audio Feature Extraction App")
    
    # Add a file uploader and folder path input field
    file = st.file_uploader("Upload an audio file (.wav or .mp3)", type=["wav", "mp3"])
    folder = st.text_input("Enter a folder path containing audio files")

    # Check if a file is uploaded or folder path is entered
    if file is not None:
        # Save the file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(file.read())
            file_path = tmp_file.name

        features = extract_features(file_path)
        features_df = pd.DataFrame(features, index=[0])
        st.write(features_df)
        features_df.to_csv('audio_features.csv', index=False)

        # Remove the temporary file
        os.remove(file_path)
    elif folder:
        # Extract features for all audio files in folder
        audio_files = [f for f in os.listdir(folder) if f.endswith('.wav') or f.endswith('.mp3')]
        all_features = []
        for audio_file in audio_files:
            file_path = os.path.join(folder, audio_file)
            features = extract_features(file_path)
            all_features.append(features)
        features_df = pd.DataFrame(all_features)
        st.write(features_df)
       
        chart_data(features_df)

        csv = convert_df(features_df)
        st.download_button(
        label="Download CSV Data",
        data=csv,
        file_name='features_df.csv',
        mime='text/csv',
         )
        # st.markdown(download_csv(features_df), unsafe_allow_html=True)
        features_df.to_csv('audio_features.csv', index=False)
    else:
        st.write("Please upload an audio file or enter a folder path")


if __name__ == '__main__':
    main()
