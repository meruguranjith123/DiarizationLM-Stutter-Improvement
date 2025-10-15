# Main pipeline for stutter voice improvement
from diarizationlm import diarize_and_clean
from whisper import transcribe_with_whisper
import sys
import os

def process_audio(audio_path, output_dir):
	# Step 1: Diarization and cleaning
	cleaned_segments = diarize_and_clean(audio_path)
	transcripts = []
	for i, segment_path in enumerate(cleaned_segments):
		# Step 2: Whisper transcription
		transcript = transcribe_with_whisper(segment_path)
		transcripts.append((segment_path, transcript))
		print(f"Segment {i}: {transcript}")
	# Save transcripts
	os.makedirs(output_dir, exist_ok=True)
	with open(os.path.join(output_dir, "transcripts.txt"), "w") as f:
		for segment_path, transcript in transcripts:
			f.write(f"{segment_path}: {transcript}\n")

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: python main.py <audio_path> <output_dir>")
		sys.exit(1)
	audio_path = sys.argv[1]
	output_dir = sys.argv[2]
	process_audio(audio_path, output_dir)
