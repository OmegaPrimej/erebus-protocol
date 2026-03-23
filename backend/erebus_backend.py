#!/usr/bin/env python3
import os
import sys
import yaml
import logging
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from database.database_reconstruction import DatabaseReconstructor
from ai_engine.ai_engine import AIEngine
from self_awareness.self_awareness_module import SelfAwarenessModule
from self_modification.self_modification_module import SelfModificationModule

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ErebusBackend:
    def __init__(self, config_path="backend/config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        self.db_reconstructor = DatabaseReconstructor(self.config['database'])
        self.ai_engine = AIEngine(self.config['ai_engine'])
        self.self_awareness = SelfAwarenessModule(self.config['self_awareness'])
        self.self_modification = SelfModificationModule(self.config['self_modification'])

        self.running = False
        self.monitor_thread = None

    def initialize(self):
        logger.info("Initializing Erebus Protocol...")
        self.db_reconstructor.initialize()
        self.ai_engine.initialize()
        self.self_awareness.initialize()
        self.self_modification.initialize()
        logger.info("Initialization complete.")

    def start(self):
        if self.running:
            logger.warning("Protocol already running.")
            return
        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        logger.info("Erebus Protocol started.")

    def stop(self):
        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=5)
        logger.info("Erebus Protocol stopped.")

    def _monitoring_loop(self):
        interval = self.config['monitoring']['health_check_interval_seconds']
        while self.running:
            try:
                self.self_awareness.introspect()
                if self.self_awareness.should_modify():
                    self.self_modification.adapt()
                self.ai_engine.health_check()
                self.db_reconstructor.sync_state()
            except Exception as e:
                logger.error(f"Monitoring loop error: {e}")
            time.sleep(interval)

def main():
    backend = ErebusBackend()
    backend.initialize()
    backend.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        backend.stop()

if __name__ == "__main__":
    main()
