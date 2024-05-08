# Image to Audio Story Converter

This project converts images into audio stories. It utilizes machine learning models for image captioning and story generation, along with text-to-speech capabilities. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x.
- pip (Python package manager).

### Installation

1. Clone the repository to your local machine:

2. Navigate into the project directory:

3. Install the required Python packages:

`pip install -r requirements.txt`

### Setup

Before running the program, you need to set up your environment variables:

1. Create a `.env` file in the root directory of the project.

2. Add your Hugging Face Hub API token to the `.env` file.

3. Add your OpenAI token to the `.env` file.

### Usage

To run the program, execute the following command:

`python app.py`

This will start a Streamlit application where you can upload an image. Once uploaded, the program will generate a text story based on the image and convert it into an audio file.

## Built With

- [Transformers](https://github.com/huggingface/transformers) - State-of-the-art Natural Language Processing for PyTorch and TensorFlow.
- [Langchain](https://github.com/lmullen/langchain) - A framework for chaining language models.
- [Hugging Face Hub](https://huggingface.co/) - A model repository and ecosystem for ML models.

# Image to Audio Story Converter

This project is a web application that allows users to convert images into descriptive audio stories. It utilizes cutting-edge AI models for image captioning and story generation to create engaging narratives based on the content of the uploaded images.

## Features

- **Image Captioning**: Utilizes a state-of-the-art image-to-text model to generate descriptive captions for uploaded images.
- **Story Generation**: Generates audio stories based on the image captions using advanced natural language processing models.
- **Text-to-Speech**: Converts the generated stories into audio format for easy listening.
- **Streamlit Interface**: Provides a user-friendly web interface powered by Streamlit for easy image upload and story playback.

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your environment variables:
   - `HUGGINGFACEHUB_API_TOKEN`: API token for accessing Hugging Face models.
   - `OPENAI_API_KEY`: API key for accessing OpenAI models.
4. Run the application using `streamlit run app.py`.
5. Upload an image using the provided interface.
6. The image will be processed to generate a descriptive caption.
7. Based on the caption, an audio story will be generated.
8. Listen to the generated story in audio format.
9. Enjoy the immersive experience of turning your images into captivating narratives!
