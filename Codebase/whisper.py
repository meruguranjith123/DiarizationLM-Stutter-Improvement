# Whisper transcription for stutter improvement
import os
try:
	import whisper
except ImportError:
	print("whisper not installed. Install with: pip install openai-whisper")

def transcribe_with_whisper(audio_path, model_size="base"):
	# Load pretrained Whisper model
	model = whisper.load_model(model_size)
	result = model.transcribe(audio_path)
	return result["text"]
