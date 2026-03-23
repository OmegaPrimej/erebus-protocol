import unittest
import yaml
import tempfile
import os
from unittest.mock import MagicMock, patch
from ai_engine.ai_engine import AIEngine

class TestAIEngine(unittest.TestCase):
    def setUp(self):
        # Create a minimal config for testing
        self.config = {
            'diffusion_model': 'test/model',
            'device': 'cpu',
            'memory_optimizations': False,
            'llm': {
                'api_key': 'test_key',
                'endpoint': 'https://api.test.com',
                'model': 'test-model',
                'max_tokens': 100
            }
        }

    def test_initialization_without_loading(self):
        """Test that AIEngine can be instantiated without loading models."""
        engine = AIEngine(self.config)
        self.assertIsNotNone(engine)
        self.assertEqual(engine.device, 'cpu')

    @patch('ai_engine.ai_engine.StableDiffusionPipeline')
    @patch('ai_engine.ai_engine.RealESRGANer')
    def test_initialize_loads_pipeline_and_upscaler(self, mock_upscaler, mock_pipe):
        """Test that initialize() loads the diffusion pipeline and upscaler."""
        mock_pipe.from_pretrained.return_value = MagicMock()
        engine = AIEngine(self.config)
        engine.initialize()
        mock_pipe.from_pretrained.assert_called_once()
        mock_upscaler.assert_called_once()

    @patch('ai_engine.ai_engine.requests.post')
    def test_generate_prompt_success(self, mock_post):
        """Test prompt generation with a mock LLM response."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'choices': [{'message': {'content': 'A beautiful landscape with mountains.'}}]
        }
        mock_post.return_value = mock_response
        engine = AIEngine(self.config)
        prompt = engine.generate_prompt('mountain')
        self.assertEqual(prompt, 'A beautiful landscape with mountains.')
        mock_post.assert_called_once()

    @patch('ai_engine.ai_engine.requests.post')
    def test_generate_prompt_failure(self, mock_post):
        """Test prompt generation when LLM call fails."""
        mock_post.side_effect = Exception('API error')
        engine = AIEngine(self.config)
        prompt = engine.generate_prompt()
        self.assertIsNone(prompt)

    def test_generate_prompt_no_llm_config(self):
        """Test prompt generation when LLM not configured."""
        config_no_llm = self.config.copy()
        config_no_llm.pop('llm')
        engine = AIEngine(config_no_llm)
        prompt = engine.generate_prompt()
        self.assertIsNone(prompt)
