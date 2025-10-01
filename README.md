## 🎙️ Voice RAG with VideoSdk Agents SDK

This script demonstrates how to build a voice-enabled Retrieval-Augmented Generation (RAG) system using VideoSdk Agents SDK. The application allows users to commuincate direct to the agent, ask questions, and receive voice responses using VideoSdk Agents SDK capabilities.

### Features

- Creates a voice-enabled RAG system using VideoSdk Agents SDK
- Supports voice processing and chunking(STT --> TTS)
- Uses FAISS as the vector database for efficient similarity search
- Implements real-time text-to-speech with voice options
- Provides a user-friendly interface

### How to get Started?

1. Create and activate a virtual environment with Python 3.12 or higher:
   python3.12 -m venv venv
   source venv/bin/activate

2. Install the required dependencies:
   pip install "videosdk-agents[deepgram,openai,elevenlabs,silero,turn_detector]"

<!-- ```bash
pip install -r requirements.txt
``` -->

3. Set up your API keys:

- Get your [DEEPGRAM_API_KEY] ("https://console.deepgram.com/")
- Get your [OPENAI_API_KEY]("https://platform.openai.com/api-keys")
- Get your [ELEVENLABS_API_KEY]("https://elevenlabs.io/app/settings/api-keys")
- Get your [VIDEOSDK_AUTH_TOKEN]("https://docs.videosdk.live/ai_agents/authentication-and-token")

- Create a `.env` file with your credentials:

```bash
DEEPGRAM_API_KEY = "Your Deepgram API Key"
OPENAI_API_KEY = "Your OpenAI API Key"
ELEVENLABS_API_KEY = "Your ElevenLabs API Key"
VIDEOSDK_AUTH_TOKEN = "VideoSDK Auth token"
```

4. Run the Voice RAG application:

```bash
python main.py
python main.py console
```

5. Open your web browser and navigate to the URL provided in the console output to interact with the Voice RAG system.

1.User Speech Input (STT):

● The user speaks through their microphone.
● Speech is converted to text in real-time using DeepgramSTT.
● Text is passed to the RAG pipeline or fallback LLM for processing.

2.RAG Query Processing:

● The text query is analyzed to find relevant information from local documents stored in the docs/ folder.
● Documents are split into manageable chunks using LangChain’s RecursiveCharacterTextSplitter.
●Each chunk is embedded using HuggingFace Sentence Transformers.
●The nearest neighbor search retrieves the most relevant document chunks.
●If no relevant documents are found, the system falls back to OpenAI GPT-4o for a response.

3.Response Generation:

●The agent generates a coherent response based on RAG context or LLM output.
●Responses are optimized to be spoken-word friendly for audio delivery.

4.Voice Output (TTS):

●Text responses are converted to speech using ElevenLabsTTS.
●Users can hear the response in real-time.
●The system ensures smooth, natural audio playback for interactive conversations.

5.Features:

●End-to-end voice interaction: STT → RAG → TTS.
●Local knowledge retrieval from .txt documents.
●Fallback to GPT-4o for unknown queries.
●Real-time logging of queries, retrieval, and agent responses.
●Seamless conversation flow with entry, user message, and exit handling.
