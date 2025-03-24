---
title: Speech_To_Speech_Chatbot
app_file: app.py
sdk: gradio
sdk_version: 4.14.0
---


# Speech-to-Speech & Text Pipeline

A Flask-based web application that allows users to record or upload an audio file and receive a natural language response from a Large Language Model (LLM). The application processes speech input (converting it to text), sends it to the LLM, and then converts the LLM’s text answer back to speech.

## Features

- **Audio Input:** Users can record their voice or upload an audio file.
- **Speech-to-Text Processing:** Converts the audio into text.
- **LLM Interaction:** Sends the transcribed text to an LLM for processing and response generation.
- **Text-to-Speech Output:** Converts the LLM's response into audio for playback.
- **Web Interface:** User-friendly UI built with Flask for seamless interaction.

## Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/)
- [virtualenv](https://virtualenv.pypa.io/) (recommended)
- FFmpeg installed on your system (for audio processing)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
    ```
2. **Create a virtual environment and activate it:**

   ```bash
      python3 -m venv venv
      source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```
## **Install dependencies:**

   ```bash
      pip install -r requirements.txt
   ```

## Set up environment variables:

Create a .env file in the root directory and add below configuration variables.
 
**For example:**

   ```code
   GEMINI_API_KEY=<KEY>
   HF_TOKEN=<KEY>
   COHERE_TOKEN=<KEY>
   ```
## Build & Run Instructions

### How to Use?

1. In CMD run below command
  ```code
      gradio app.py
  ```

2. Access the Web Interface:
- Open your web browser and navigate to http://127.0.0.1:7860/.

- Record or Upload Audio:

- Use the built-in recorder to capture speech.

- Alternatively, click the "Upload" button to select an existing audio file.

3. Process the Input:
- Once an audio file is recorded or uploaded, click "Submit." The application will:

- Convert speech to text.

- Send the text to the LLM API.

- Retrieve the text response.

- Convert the text response to audio.

4. Listen to the Response:
- The application will display the text response and provide an audio playback option for the LLM's answer.


## Contact

For questions or feedback, please contact janakmandavgade27@gmail.com.