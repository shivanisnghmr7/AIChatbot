Welcome to the “**AI Girlfriend Chatbot**” project! 
This project allows you to interact with an AI chatbot designed to simulate natural and engaging conversations. The AI is built to respond playfully, intelligently, and empathetically, providing a conversational experience that feels personal and interactive. You can change the message and make ir chat like Any AI ChatBot.

**How It Works**

This AI chatbot is powered by LLMs that simulate realistic conversations.The AI uses advanced NLP to generate responses that feel like you’re talking to a real person. 
AI Chatbot is capable to respond in Text and audio.
This AI can be customized for various applications, from casual conversations to more specific domains, and is flexible enough to be integrated into different types of projects.

**Tech Used**
1. OpenAI GPT-3 (or GPT-3.5) or Hugging Face Transformers (Optional)
2. Text-to-Speech (TTS): ElevenLabs API
3. Flask

**Installation**

**Prerequisites**

Before you begin, make sure you have the following installed:
•	Python 3.x
•	Pip3 (Python package installer)

1. Clone the repository
   
   ```git clone x```
   
   ```cd AIChatbot```
2. Install the dependencies
   
   ```pip3 install -r requirements.txt```
3. Set up your environment
   
   Create an .env file to store your API keys securely:
   
   ```touch .env```
   
   Add the following environment variables (replace the placeholders with your actual API keys):
   ```
   OPENAI_API_KEY=your_openai_api_key
   ELEVEN_LABS_KEY=your_elevenlabs_api_key
   
4. Run the Flask Application
   Start the Flask server:
   
   ```python AI_Chatbot_implementation.py```

**Usage**
1.	Once the application is running, open your browser and go to http://127.0.0.1:5000/.
2.	Type a message to start a conversation with your AI chatbot.
3.	The AI will respond to your message in text and, if enabled, will also speak the message aloud.

**Acknowledgements**

1. OpenAI for providing the GPT-3 API.
2. Hugging Face for their pre-trained models and NLP resources.
3. ElevenLabs for their speech-to-text conversion capabilities.
4. Flask for the web framework.