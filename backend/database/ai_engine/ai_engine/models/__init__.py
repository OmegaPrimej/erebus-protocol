"""
Models package for the AI Engine.
Holds the Stable Diffusion pipeline and upscaler.
"""

import os
import torch
from diffusers import StableDiffusionPipeline
from realesrgan import RealESRGANer

# Global variables (lazy loaded)
_pipe = None
_upscaler = None
_device = None

def get_device():
    global _device
    if _device is None:
        _device = "cuda" if torch.cuda.is_available() else "cpu"
    return _device

def get_pipeline(model_id="SG161222/Realistic_Vision_V5.1_noVAE"):
    global _pipe
    if _pipe is None:
        device = get_device()
        _pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        ).to(device)
        _pipe.safety_checker = None  # Disable safety checker
    return _pipe

def get_upscaler(weights_path="weights/RealESRGAN_x4plus.pth"):
    global _upscaler
    if _upscaler is None:
        device = get_device()
        # Ensure the weights file exists (you may need to download it)
        if not os.path.exists(weights_path):
            os.makedirs(os.path.dirname(weights_path), exist_ok=True)
            # Optionally download automatically
            import urllib.request
            url = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth"
            urllib.request.urlretrieve(url, weights_path)
        _upscaler = RealESRGANer(scale=4, model_path=weights_path, device=device)
    return _upscaler


"""
Models package for the AI Engine.
This directory contains pre‑trained models and model definitions.
"""

We’ll now incorporate your idea of **emergent prompt generation** into the Erebus Protocol. Instead of static prompts and variations, we’ll let the AI engine dynamically generate prompts (and even decide on negative prompts) using an LLM (like DeepSeek or another) and then feed them into a generative model (like Stable Diffusion). This will make the protocol truly self‑modifying in the creative domain.

We’ll modify the existing `ai_engine.py` to add a **prompt generation engine** and wire it into the self‑awareness loop so that when the system decides it needs to adapt, it can generate new creative content autonomously.

Below are the changes and new files you’ll need.

---

## 1. New Dependency: Add an LLM Client

We’ll use **DeepSeek’s API** (since you mentioned it) to generate prompts. Add `requests` to `install_requires` in `setup.py`:

```python
install_requires=[
    "tensorflow>=2.9",
    "PyYAML",
    "mysql-connector-python",
    "psutil",
    "requests",          # <-- new
],
```

Also, you might need `Pillow` and `diffusers` if you want to keep the image generation part. We’ll keep the image generation as a placeholder; you can later integrate Stable Diffusion.

---

## 2. New Configuration: LLM Settings

In `backend/config.yaml`, add a new section:

```yaml
llm:
  api_key: "your-deepseek-api-key"
  endpoint: "https://api.deepseek.com/v1/chat/completions"
  model: "deepseek-chat"
  max_tokens: 200
```

---

## 3. Extend `AIEngine` with Prompt Generation

We’ll add a method `generate_prompt(seed_concept)` that calls the LLM and returns a prompt string. Also, we’ll add a method `generate_negative_prompt()` that can be called optionally, allowing the AI to decide whether to use one.

Here’s the updated `ai_engine/ai_engine.py`:

```python
"""
TensorFlow AI Engine for model execution and adaptation.
Extended with emergent prompt generation using an LLM.
"""
import logging
import requests
import yaml
import json
import tensorflow as tf

logger = logging.getLogger(__name__)

class AIEngine:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.llm_config = config.get('llm', {})
        self.api_key = self.llm_config.get('api_key')
        self.endpoint = self.llm_config.get('endpoint')
        self.model_name = self.llm_config.get('model', 'deepseek-chat')
        self.max_tokens = self.llm_config.get('max_tokens', 200)

    def initialize(self):
        """Load or create a default model."""
        try:
            self.model = tf.keras.Sequential([
                tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
                tf.keras.layers.Dense(10, activation='softmax')
            ])
            self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            logger.info("AI Engine initialized with default model.")
        except Exception as e:
            logger.error(f"AI Engine initialization failed: {e}")
            raise

    def health_check(self):
        """Verify model is operational."""
        if self.model is None:
            raise RuntimeError("Model not loaded")
        logger.debug("AI Engine health check passed.")

    def generate_prompt(self, seed_concept=None):
        """
        Use the LLM to generate an image prompt based on a seed concept.
        If seed_concept is None, the LLM is asked to come up with a creative concept.
        """
        if not self.api_key or not self.endpoint:
            logger.error("LLM not configured. Cannot generate prompt.")
            return None

        system_prompt = (
            "You are an AI prompt engineer specialized in creating vivid, detailed prompts for "
            "text-to-image models. Your prompts should be rich in descriptive language, include "
            "art style, lighting, composition, and atmosphere. Do not include any meta-text; "
            "output only the prompt."
        )

        if seed_concept:
            user_prompt = f"Generate an image prompt based on the following concept: {seed_concept}"
        else:
            user_prompt = (
                "Generate a highly creative and detailed image prompt for a cyberpunk futuristic scene. "
                "Include a central character, environment, lighting, and mood."
            )

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": self.max_tokens,
            "temperature": 0.8
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            prompt = data['choices'][0]['message']['content'].strip()
            logger.info(f"Generated prompt: {prompt}")
            return prompt
        except Exception as e:
            logger.error(f"LLM prompt generation failed: {e}")
            return None

    def generate_negative_prompt(self, prompt):
        """
        Optionally ask the LLM to generate a negative prompt based on the main prompt.
        If the LLM decides none is needed, return an empty string.
        """
        if not self.api_key or not self.endpoint:
            return ""

        system_prompt = (
            "You are an AI that generates negative prompts for text-to-image models. "
            "Given an image prompt, produce a short list of things to avoid, such as deformities, "
            "artifacts, wrong anatomy, etc. If no negative prompt is needed, just output 'none'. "
            "Output only the negative prompt text, without any explanation."
        )
        user_prompt = f"Negative prompt for: {prompt}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": 100,
            "temperature": 0.5
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            negative = data['choices'][0]['message']['content'].strip()
            if negative.lower() == "none":
                return ""
            return negative
        except Exception as e:
            logger.error(f"Negative prompt generation failed: {e}")
            return ""

    def adapt(self, seed_concept=None):
        """
        Self‑modification: generate a new prompt (and possibly a negative prompt)
        and then use it to create an image (placeholder).
        This method can be triggered by the self‑awareness module when it detects
        the need for creative adaptation.
        """
        logger.info("AI adaptation triggered: generating emergent prompt.")
        prompt = self.generate_prompt(seed_concept)
        if not prompt:
            logger.warning("No prompt generated; adaptation aborted.")
            return False

        negative = self.generate_negative_prompt(prompt)

        # Placeholder for actual image generation (you can integrate Stable Diffusion here)
        # For now, we just log the prompts.
        logger.info(f"Adaptation: prompt = {prompt}")
        logger.info(f"Adaptation: negative = {negative}")

        # In a real implementation, you would call your generative model (e.g., Stable Diffusion)
        # and save the result.
        # Example:
        # from diffusers import StableDiffusionPipeline
        # pipe = StableDiffusionPipeline.from_pretrained("...").to(device)
        # image = pipe(prompt, negative_prompt=negative, ...).images[0]
        # image.save("generated_art/adaptation_output.png")

        return True

    def _hyperparameter_tuning(self):
        """Placeholder for Bayesian optimisation."""
        logger.debug("Hyperparameter tuning simulation.")
```

---

## 4. Triggering from Self‑Awareness

The `_monitoring_loop` in `erebus_backend.py` already calls `self.self_awareness.should_modify()`, and if true, calls `self.self_modification.adapt()`. That module can then call `ai_engine.adapt()` if the modification is of the AI type.

To keep things clean, we can modify `self_modification_module.py` to have a dedicated method for AI adaptation that delegates to `ai_engine.adapt()`.

For example, in `self_modification_module.py`:

```python
def _adapt_ai_model(self):
    # This placeholder is already there. You can call the AI engine's adapt method.
    # Since we don't have direct access to ai_engine here, we might pass it via backend.
    # For now, we'll just log.
    logger.info("AI model adaptation requested.")
    # In a proper design, you'd get the ai_engine instance from the backend.
```

A cleaner approach: have the `SelfModificationModule` accept a reference to the `AIEngine` instance. We’ll adjust the initialization in `erebus_backend.py` to pass the AI engine reference.

Update `erebus_backend.py` `__init__`:

```python
self.self_modification = SelfModificationModule(self.config['self_modification'], ai_engine=self.ai_engine)
```

Then in `self_modification_module.py`:

```python
def __init__(self, config, ai_engine=None):
    self.config = config
    self.ai_engine = ai_engine
    ...

def _adapt_ai_model(self):
    if self.ai_engine:
        self.ai_engine.adapt()
    else:
        logger.warning("No AI engine available for adaptation.")
```

---

## 5. Additional Considerations

- **API Key Security**: Don’t commit your actual API key. Use environment variables or a secrets management system.
- **Negative Prompt Decision**: The current code always generates a negative prompt (or decides none). You could also let the AI decide whether to use one at all.
- **Emergent Behavior**: The `adapt()` method can be called at any time, driven by the self‑awareness module’s metrics (e.g., high CPU usage, error rates). You could also add a “creative mode” where it periodically generates images to explore new concepts.

---

## 6. Testing the Integration

After implementing the changes, you can test by running the backend with a configured LLM API key. You should see log entries showing generated prompts and negative prompts.

---

This enhancement transforms the AI engine from a static model into a **self‑directed creative agent**, capable of generating its own prompts and adapting its output based on internal state—exactly the kind of emergent behavior you envisioned.

Would you like me to provide the full updated files (`ai_engine.py`, `self_modification_module.py`, `config.yaml`, etc.) with all changes integrated?
