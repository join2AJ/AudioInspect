# AudioInspect
AudioInspect is an app that allows users to extract audio features from uploaded audio files or audio files in a specified folder. The app provides insights into the characteristics of the audio, such as chroma, root-mean-square energy, spectral centroid, spectral bandwidth, spectral rolloff, zero-crossing rate, and mel-frequency cepstral coefficients.

## Installation
  To use AudioInspect, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running pip install -r requirements.txt.
3. Run the app using streamlit run app.py.

## Usage
  Once you have the app running, follow these steps to extract audio features:

1. Upload an audio file by clicking the "Upload an audio file" button, or enter a folder path containing audio files in the text input field.
2. Wait for the app to extract the audio features and display them in a table.
3. Download a CSV file containing the extracted audio features by clicking the "Download CSV Data" button.

## Dependencies
  AudioInspect was built using the following dependencies:

1. os
2. base64
3. pandas
4. librosa
5. tempfile
6. numpy
7. streamlit

## Acknowledgements
This app was inspired by the Audio Feature Extraction in Python tutorial on Towards Data Science.

## License
AudioInspect is released under the MIT License. See LICENSE for more information.

## Contributing
Contributions to AudioInspect are welcome! Please see CONTRIBUTING.md for more information on how to contribute.

**I hope this helps you get started on creating a README.md file for your AudioInspect app! Let me know if you have any other questions.**
