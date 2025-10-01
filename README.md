# 🎙️ Voice RAG with VideoSDK Agents SDK

This project demonstrates how to build a voice-enabled **Retrieval-Augmented Generation (RAG) system** using **VideoSDK Agents SDK**. Users can communicate directly with the agent, ask questions, and receive voice responses.

## Features

- Voice-enabled RAG system using VideoSDK Agents SDK
- Supports end-to-end voice processing: **STT → RAG → TTS**
- Uses **FAISS** for efficient document similarity search
- Real-time text-to-speech with multiple voice options
- Provides a user-friendly interaction flow

## Getting Started

## 🎯 System Flowchart
```mermaid
graph TD
    A[👤 User] -->|Voice or Text| B{Input Type?}
    B -->|🎤 Voice| C[🔊 Deepgram STT]
    B -->|⌨️ Text| D[Direct Query]
    C --> E[📝 Text Query]
    D --> E
    E --> F[🔍 Generate Embedding<br/>sentence-transformers]
    F --> G[📚 FAISS Vector Search]
    G --> H{Documents<br/>Found?}
    H -->|✅ Yes<br/>Distance < 0.6| I[📄 Retrieve Context]
    H -->|❌ No<br/>Distance > 0.6| J[⚠️ No Context]
    I --> K[🤖 Ollama + Context<br/>Grounded Answer]
    J --> L[🤖 Ollama Base<br/>General Knowledge]
    K --> M[💬 Generated Answer]
    L --> M
    M --> N[🗣️ ElevenLabs TTS]
    N --> O[🎧 Audio Output]
    O --> P[👤 User Hears Response]
    
    style H fill:#f9f,stroke:#333,stroke-width:4px
    style K fill:#bfb,stroke:#333,stroke-width:2px
    style L fill:#fbf,stroke:#333,stroke-width:2px
      
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

### 4. Set up API Keys

Create a `.env` file in the project root with the following:

```env
DEEPGRAM_API_KEY="Your Deepgram API Key"
OPENAI_API_KEY="Your OpenAI API Key"
ELEVENLABS_API_KEY="Your ElevenLabs API Key"
VIDEOSDK_AUTH_TOKEN="Your VideoSDK Auth token"
```

### 5. Run the Application

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
- If no relevant documents are found, **OpenAI GPT-4o** generates the response

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
- Fallback to GPT-4o for unknown queries
- Real-time logging of queries, retrieval, and responses
- Smooth conversation flow with entry, message, and exit handling






