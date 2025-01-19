from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import torchaudio

# Load pre-trained Wav2Vec2 model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

def speech_to_text(audio_path):
    """
    Convert speech to text using Wav2Vec2.
    Args:
        audio_path (str): Path to the .wav file.
    Returns:
        str: Transcribed text.
    """
    try:
        # Load the audio file
        waveform, rate = torchaudio.load(audio_path)
        
        # Resample to 16kHz (required for Wav2Vec2)
        resampler = torchaudio.transforms.Resample(orig_freq=rate, new_freq=16000)
        waveform = resampler(waveform).squeeze(0)

        # Process the audio
        input_values = processor(waveform, sampling_rate=16000, return_tensors="pt").input_values

        # Perform inference
        logits = model(input_values).logits

        # Decode the predicted IDs to text
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.decode(predicted_ids[0])
        return transcription
    except Exception as e:
        return {"error": str(e)}
