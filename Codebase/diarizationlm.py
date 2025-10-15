# DiarizationLM: Speaker diarization and cleaning
import os
import tempfile
from pydub import AudioSegment
try:
	from pyAudioAnalysis import audioSegmentation as aS
except ImportError:
	print("pyAudioAnalysis not installed. Install with: pip install pyAudioAnalysis pydub")

def diarize_and_clean(audio_path):
	# Speaker diarization using pyAudioAnalysis (pretrained)
	# Returns list of cleaned segment file paths
	segments = []
	temp_dir = tempfile.mkdtemp()
	# Perform speaker diarization
	segs, classes = aS.speaker_diarization(audio_path, n_speakers=2)
	audio = AudioSegment.from_file(audio_path)
	# Split and save segments
	for i, (start, end) in enumerate(segs):
		seg_audio = audio[start*1000:end*1000]
		seg_path = os.path.join(temp_dir, f"segment_{i}.wav")
		seg_audio.export(seg_path, format="wav")
		segments.append(seg_path)
	return segments
