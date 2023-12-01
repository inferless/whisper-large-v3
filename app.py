import json
import numpy as np
import torch
from transformers import pipeline

class InferlessPythonModel:
        
    def initialize(self):
        self.generator = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-large-v3", chunk_length_s=30, batch_size=8,
            torch_dtype=torch.float16,
            device_map="cuda:0",
        )

    def infer(self, inputs):
        audio_url = inputs["audio_url"]
        pipeline_output = self.generator(audio_url, )
        return {"transcribed_output": pipeline_output["text"] }

    def finalize(self):
        self.generator = None