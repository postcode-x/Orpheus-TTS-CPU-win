import argparse
from scipy.io.wavfile import write
from orpheus_cpp import OrpheusCpp
import numpy as np
import time
import os

# Parse command-line argument
parser = argparse.ArgumentParser(description="Text-to-speech with OrpheusCpp")
parser.add_argument("--prompt", required=True, help="Text to synthesize")
parser.add_argument(
    "--voice",
    default="zac",
    help='Voice to synthesize ("tara", "leah", "jess", "leo", "dan", "mia", "zac", "zoe")',
)
args = parser.parse_args()

orpheus = OrpheusCpp(verbose=False, lang="en", n_threads=4)

buffer = []
for i, (sr, chunk) in enumerate(
    orpheus.stream_tts_sync(
        args.prompt,
        options={
            "voice_id": args.voice,
            "temperature": 0.75,
            "top_p": 0.92,
            "top_k": 40,
            "min_p": 0.06,
            "max_tokens": 2048,
        }
        # options={
        #   "voice_id": args.voice,
        #   "temperature" : 0.85
        # }
        # options = {
        # "voice_id": args.voice,
        # "temperature": 0.7,
        # "top_p": 0.88,
        # "top_k": 35,
        # "min_p": 0.07,
        # "max_tokens": 2048
        # }
    )
):
    buffer.append(chunk)
    print(f"Generated chunk {i}")

buffer = np.concatenate(buffer, axis=1)

os.makedirs("output", exist_ok=True)

timestamp = int(time.time())
filename = f"output/output_{timestamp}.wav"
write(filename, 24_000, np.concatenate(buffer))
