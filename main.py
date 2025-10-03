import asyncio
import logging
from videosdk.agents import Agent, AgentSession, CascadingPipeline, WorkerJob, ConversationFlow, JobContext, RoomOptions
from videosdk.plugins.deepgram import DeepgramSTT
from videosdk.plugins.elevenlabs import ElevenLabsTTS
from videosdk.plugins.silero import SileroVAD
from videosdk.plugins.turn_detector import TurnDetector
from rag_pipeline import query_rag


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

class VoiceAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful voice AI assistant that uses local knowledge if available.")

    async def on_enter(self):
        await self.session.say("Hey! I'm ready to help you with your local knowledge.")
        logger.info("Agent has entered the session.")

    async def on_user_message(self, message: str):
        logger.info(f"🗣️ User: {message}")
        response = query_rag(message)
        logger.info(f"💬 Response: {response}")
        await self.session.say(response)

    async def on_exit(self):
        await self.session.say("Goodbye!")
        logger.info("Agent has exited the session.")

async def entrypoint(ctx: JobContext):
    agent = VoiceAgent()
    pipeline = CascadingPipeline(
        stt=DeepgramSTT(),
        tts=ElevenLabsTTS(),
        vad=SileroVAD(),
        turn_detector=TurnDetector()
    )
    session = AgentSession(agent=agent, pipeline=pipeline, conversation_flow=ConversationFlow(agent))
    try:
        await ctx.connect()
        logger.info("Connected to JobContext. Waiting for participant...")
        await ctx.room.wait_for_participant()
        await session.start()
        await asyncio.Event().wait()
    finally:
        await session.close()
        await ctx.shutdown()
        logger.info("Session closed and context shutdown.")

def make_context():
    return JobContext(room_options=RoomOptions(room_id="uurl-c21l-k7ih", playground=True))

if __name__ == "__main__":
    job = WorkerJob(entrypoint=entrypoint, jobctx=make_context())
    logger.info("Starting WorkerJob...")
    job.start()
