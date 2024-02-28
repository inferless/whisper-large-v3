from faster_whisper import WhisperModel

class InferlessPythonModel:
        
    def initialize(self):
        model_size = "large-v3"
        self.model = WhisperModel(model_size, device="cuda", compute_type="float16")

    def infer(self, inputs):
        
        audio_url = inputs["audio_url"]
        segments, info = self.model.transcribe(audio_url, beam_size=5)
        text = ''.join([segment.text for segment in segments])
        
        return {"transcribed_output":text}

    def finalize(self):
        pass
