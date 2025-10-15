# Test script for stutter voice improvement pipeline
import os
from main import process_audio

def test_pipeline():
	sample_audio = "sample.wav"  # Place a sample audio file in the project root
	output_dir = "output_test"
	if not os.path.exists(sample_audio):
		print(f"Sample audio file '{sample_audio}' not found.")
		return
	process_audio(sample_audio, output_dir)
	print(f"Transcripts saved to {output_dir}/transcripts.txt")

if __name__ == "__main__":
	test_pipeline()
