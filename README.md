# 🎙️ Voice RAG with VideoSDK Agents SDK

This project demonstrates how to build a voice-enabled **Retrieval-Augmented Generation (RAG) system** using **VideoSDK Agents SDK**. Users can communicate directly with the agent, ask questions, and receive voice responses.

## Features

- Voice-enabled RAG system using VideoSDK Agents SDK
- Supports end-to-end voice processing: **STT → RAG → TTS**
- Uses **FAISS** for efficient document similarity search
- Real-time text-to-speech with multiple voice options
- Provides a user-friendly interaction flow

## Getting Started
## 🎙️ Voice RAG with VideoSDK Agents SDK — Demonstration

This project showcases how to build a **voice-enabled Retrieval-Augmented Generation (RAG) system** using **VideoSDK Agents SDK**.  
Users can interact naturally with the AI agent — ask questions via voice, and receive intelligent **spoken responses** powered by local knowledge and RAG techniques.

🎥 [Watch the Demonstration](https://drive.google.com/file/d/1R6rTu84qz5HyDgXm6jXU9w2NqdOYr7js/view?usp=sharing)

      
## Project Structure

```
VidRag_Ollama/
├── main.py                # Entry point for the voice AI agent
├── rag_pipeline.py       # Local RAG pipeline for document retrieval
├── docs/                      # Your knowledge base (.txt files)
│   ├── videosdk.txt
│   ├── petpooja.txt
├── scripts/                
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```
### 1. Clone the Repository

```bash
git clone https://github.com/parthalathiya03/videosdk_agent.git
cd videosdk_agent
```

### 2. Create and Activate Virtual Environment

```bash
# macOS/Linux
python3.12 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install "videosdk-agents[deepgram,openai,elevenlabs,silero,turn_detector]"
```

Or using `requirements.txt` if available:

```bash
pip install -r requirements.txt
```
### 4. Set up your Local Ollama model 

Ollama enables you to run open-source large language models (LLMs) directly on your machine. Follow these steps to get started:

### 1. Install Ollama

- **macOS**: Use Homebrew:
```bash
brew install ollama

After installation, start the Ollama server:
ollama serve
ollama pull <model-name>
ollama run <model-name>
```
### 5. Set up API Keys

Create a `.env` file in the project root with the following:

```env
DEEPGRAM_API_KEY="Your Deepgram API Key"
OPENAI_API_KEY="Your OpenAI API Key"
ELEVENLABS_API_KEY="Your ElevenLabs API Key"
VIDEOSDK_AUTH_TOKEN="Your VideoSDK Auth token"
```

### 6. Run the Application

```bash
python main.py
# or console mode
python main.py console
```

Open the browser URL displayed in the console to interact with the Voice RAG agent.

## How It Works

### 1. User Speech Input (STT)

- User speaks through their microphone
- **DeepgramSTT** converts speech to text in real-time
- Text is passed to the RAG pipeline or fallback LLM

### 2. RAG Query Processing

- Queries are analyzed against local documents in the `docs/` folder
- Documents are split into chunks using **LangChain RecursiveCharacterTextSplitter**
- Chunks are embedded using **HuggingFace Sentence Transformers**
- **FAISS** retrieves the most relevant document chunks
- If no relevant documents are found, **Ollama** generates the response

### 3. Response Generation

- Agent creates coherent responses from RAG context or LLM output
- Responses are optimized for spoken-word delivery

### 4. Voice Output (TTS)

- Responses are converted to speech using **ElevenLabsTTS**
- Users hear the response in real-time
- Ensures smooth, natural audio playback

### 5. Features

- End-to-end voice interaction: **STT → RAG → TTS**
- Local knowledge retrieval from `.txt` documents
- Fallback to Ollama for unknown queries
- Real-time logging of queries, retrieval, and responses
- Smooth conversation flow with entry, message, and exit handling











