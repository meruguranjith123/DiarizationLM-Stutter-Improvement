# Training script for DiarizationLM (optional, uses pyAudioAnalysis)
from pyAudioAnalysis import audioTrainTest as aT
import sys

def train_diarization_model(audio_dir, model_name="diarization_model"):
	# Train speaker recognition model
	aT.extract_features_and_train(audio_dir, "wav", model_name, "svm")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python train_diarizationlm.py <audio_dir>")
		sys.exit(1)
	audio_dir = sys.argv[1]
	train_diarization_model(audio_dir)
