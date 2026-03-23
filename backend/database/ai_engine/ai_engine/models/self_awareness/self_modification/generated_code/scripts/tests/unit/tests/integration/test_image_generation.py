import unittest
import os
from PIL import Image
import tempfile
from ai_engine.ai_engine import AIEngine

class TestImageGenerationIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Skip if not explicitly enabled
        if not os.getenv('RUN_INTEGRATION_TESTS'):
            raise unittest.SkipTest('Integration tests disabled')

        # Load a minimal config (assumes real model and GPU)
        cls.config = {
            'diffusion_model': 'SG161222/Realistic_Vision_V5.1_noVAE',
            'device': 'cuda',
            'memory_optimizations': True,
            'llm': {
                'api_key': os.getenv('DEEPSEEK_API_KEY', ''),
                'endpoint': 'https://api.deepseek.com/v1/chat/completions',
                'model': 'deepseek-chat',
                'max_tokens': 200
            }
        }

    def test_image_generation(self):
        """Generate an image from a prompt and verify output."""
        engine = AIEngine(self.config)
        engine.initialize()
        prompt = "A beautiful cyberpunk cityscape at night"
        image = engine.generate_image(prompt)
        self.assertIsInstance(image, Image.Image)
        # Save to a temporary file
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            image.save(f.name)
            self.assertGreater(os.path.getsize(f.name), 0)
        os.unlink(f.name)

    def test_upscaling(self):
        """Test upscaling of a generated image."""
        engine = AIEngine(self.config)
        engine.initialize()
        prompt = "A portrait of a futuristic warrior"
        image = engine.generate_image(prompt)
        upscaled = engine.upscale_image(image)
        self.assertIsInstance(upscaled, Image.Image)
        self.assertTrue(upscaled.size[0] >= image.size[0])
