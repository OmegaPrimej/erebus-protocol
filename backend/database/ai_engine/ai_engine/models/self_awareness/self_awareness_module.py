"""
Self‑awareness module: introspection, feedback loops, meta‑cognition.
"""
import logging
import psutil
import time
from collections import deque

logger = logging.getLogger(__name__)

class SelfAwarenessModule:
    def __init__(self, config):
        self.config = config
        self.performance_history = deque(maxlen=100)
        self.error_log = deque(maxlen=100)
        self.feedback_queue = deque(maxlen=50)

    def initialize(self):
        logger.info("Self‑awareness module initialized.")

    def introspect(self):
        """Collect internal state and performance metrics."""
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        self.performance_history.append((time.time(), cpu, mem))
        logger.debug(f"Introspection: CPU={cpu}%, MEM={mem}%")

        if cpu > 90:
            self.error_log.append(("High CPU", time.time()))
            logger.warning("High CPU usage detected.")

        self._meta_cognition()

    def should_modify(self):
        """Determine if self‑modification is needed based on introspection."""
        recent_errors = sum(1 for _, ts in self.error_log if time.time() - ts < 3600)
        if recent_errors > 5:
            logger.info("Self‑modification triggered due to high error rate.")
            return True
        high_cpu_count = sum(1 for _, cpu, _ in self.performance_history if cpu > 95)
        if high_cpu_count > 3:
            logger.info("Self‑modification triggered due to persistent high CPU.")
            return True
        return False

    def _meta_cognition(self):
        """Analyze decision‑making patterns (placeholder)."""
        pass

    def receive_feedback(self, feedback):
        """Incorporate external feedback."""
        self.feedback_queue.append(feedback)
        logger.info(f"Feedback received: {feedback}")
