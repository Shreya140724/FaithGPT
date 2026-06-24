import os
import re
from datetime import datetime

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

print("HF_TOKEN =", HF_TOKEN)

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)


def generate_image(prompt):

    try:

        print("Generating image for:", prompt)

        image = client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-schnell"
        )

        os.makedirs(
            "generated_images",
            exist_ok=True
        )

        # Remove invalid filename characters
        safe_prompt = re.sub(
            r'[\\/*?:"<>|]',
            "",
            prompt
        )

        safe_prompt = (
            safe_prompt
            .replace(" ", "_")
            .strip()
        )

        # Add timestamp so every image is unique
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = (
            f"{safe_prompt}_{timestamp}.png"
        )

        path = os.path.join(
            "generated_images",
            filename
        )

        image.save(path)

        print("Image saved:", path)

        return path

    except Exception as e:

        print("IMAGE ERROR:")
        print(repr(e))

        return None