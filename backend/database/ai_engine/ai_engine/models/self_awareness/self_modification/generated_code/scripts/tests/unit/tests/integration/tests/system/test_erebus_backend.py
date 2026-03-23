import unittest
import yaml
import tempfile
import threading
import time
from unittest.mock import MagicMock, patch
from backend.erebus_backend import ErebusBackend

class TestErebusBackend(unittest.TestCase):
    def setUp(self):
        # Create a minimal config file
        self.config_data = {
            'database': {
                'host': 'localhost',
                'port': 3306,
                'user': 'test',
                'password': 'test',
                'database': 'test'
            },
            'ai_engine': {
                'device': 'cpu',
                'memory_optimizations': False
            },
            'self_awareness': {
                'introspection_interval_seconds': 60,
                'log_retention_days': 7
            },
            'self_modification': {
                'enable_dynamic_code': False,
                'safety_constraints': True
            },
            'monitoring': {
                'daemon_enabled': True,
                'health_check_interval_seconds': 0.1  # Fast loop for testing
            }
        }
        self.config_file = tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False)
        yaml.dump(self.config_data, self.config_file)
        self.config_file.close()

    def tearDown(self):
        os.unlink(self.config_file.name)

    @patch('backend.erebus_backend.DatabaseReconstructor')
    @patch('backend.erebus_backend.AIEngine')
    @patch('backend.erebus_backend.SelfAwarenessModule')
    @patch('backend.erebus_backend.SelfModificationModule')
    def test_backend_lifecycle(self, mock_self_mod, mock_self_aware, mock_ai, mock_db):
        """Test that backend can initialize, start, and stop without errors."""
        # Create mock instances
        mock_db.return_value = MagicMock()
        mock_ai.return_value = MagicMock()
        mock_self_aware.return_value = MagicMock()
        mock_self_mod.return_value = MagicMock()

        backend = ErebusBackend(self.config_file.name)
        backend.initialize()
        backend.start()

        # Let it run for a few cycles
        time.sleep(0.5)
        backend.stop()

        # Verify that initialization was called on each module
        mock_db.return_value.initialize.assert_called_once()
        mock_ai.return_value.initialize.assert_called_once()
        mock_self_aware.return_value.initialize.assert_called_once()
        mock_self_mod.return_value.initialize.assert_called_once()

        # Verify the monitoring loop ran (should have called introspect at least once)
        self.assertGreater(mock_self_aware.return_value.introspect.call_count, 0)

    def test_config_loading(self):
        """Test that config is loaded correctly from YAML."""
        backend = ErebusBackend(self.config_file.name)
        self.assertIsNotNone(backend.config)
        self.assertEqual(backend.config['database']['host'], 'localhost')
        self.assertEqual(backend.config['monitoring']['health_check_interval_seconds'], 0.1)
