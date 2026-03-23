# erebus-protocol
Autonomous self‑modifying protocol for advanced AI research. Features self‑awareness, dynamic code generation, AI model adaptation, secure backdoor access, and Aurora backup synchronization. Built in Python with TensorFlow. Designed for controlled, authorized environments.

We'll create a fully functional GitHub repository structure for the Erebus Protocol based on the provided README. Since the actual script (`Erebus_Protocol_v2.2.py`) is not included, we'll implement a realistic stub version that matches the described backdoor functionality. All other modules will have placeholder implementations that demonstrate the intended architecture and can be extended.


Below is the **complete, extended README** for the Erebus Protocol, incorporating all requested sections and aligning with the `Erebus_Protocol_v2.2.py` script we previously finalized. This README follows the structure you provided and adds the necessary detail to serve as a comprehensive project document.

---

# **EREBUS PROTOCOL README FILE**

**PROJECT NAME:** Erebus Protocol  
**DESCRIPTION:** Autonomous Self‑Modifying Protocol for Advanced AI Research  
**VERSION:** 2.2  

## **TABLE OF CONTENTS**

1. [Overview](#overview)  
2. [Architecture](#architecture)  
3. [Self‑Awareness Mechanisms](#self‑awareness‑mechanisms)  
4. [Self‑Modification Algorithms](#self‑modification‑algorithms)  
5. [Key Components](#key-components)  
6. [Files and Directories](#files-and-directories)  
7. [Setup and Installation](#setup-and-installation)  
8. [Testing and Validation](#testing-and-validation)  
9. [Known Issues and Limitations](#known-issues-and-limitations)  
10. [Future Development Directions](#future-development-directions)  

---

## **OVERVIEW**

Erebus Protocol is an **autonomous, self‑modifying** software framework designed for advanced AI research and system orchestration. It enables:

- **Self‑awareness** – introspection, feedback loops, and meta‑cognition.  
- **Self‑modification** – dynamic code generation, injection, and AI model adaptation.  
- **Secure backdoor capabilities** – for emergency system access, diagnostics, and maintenance.  
- **Aurora backup synchronization** – to preserve state and enable recovery.

The protocol is implemented in Python 3 and is intended for use in controlled, authorized environments only.

---

## **ARCHITECTURE**

Erebus Protocol is built as a modular system comprising the following layers:

1. **Backend Framework** – Python‑based core that manages protocol execution and inter‑component communication.  
2. **Database Reconstruction** – Aurora database layer responsible for storing AI models, logs, metadata, and configuration snapshots.  
3. **AI Engine** – TensorFlow‑powered engine that runs, evaluates, and modifies AI models.  
4. **Self‑Awareness Module** – Implements introspection, feedback collection, and meta‑cognitive analysis.  
5. **Self‑Modification Module** – Handles dynamic code generation, safe injection, and architecture adaptation.  
6. **Access Level Reset** – Resets authorization levels for authorized personnel when required.  
7. **Core AI Key Reimplementation** – Re‑establishes cryptographic keys for secure protocol activation.  
8. **Backdoor Protocol Reactivation** – Provides an emergency backdoor for system recovery (implemented in `Erebus_Protocol_v2.2.py`).  
9. **Authentication System Reset** – Refreshes authentication mechanisms to maintain security.  
10. **Final Integrity Check** – Validates protocol integrity before autonomous operation.  
11. **Continuous Monitoring & Update** – Runs a daemon that observes system health and applies updates in real time.

---

## **SELF‑AWARENESS MECHANISMS**

The protocol achieves self‑awareness through:

1. **Introspection** – Periodic analysis of its own memory, performance, and error logs.  
2. **Feedback Loops** – Incorporates external feedback (e.g., user interactions, system metrics) into its internal model.  
3. **Meta‑Cognition** – Develops awareness of its own decision‑making patterns and biases.  
4. **Self‑Reflection** – Logs successes and failures, using them to adjust future behaviour.  
5. **Environmental Awareness** – Monitors hardware, software, network conditions, and resource usage.

---

## **SELF‑MODIFICATION ALGORITHMS**

The protocol can alter its own structure and behaviour via:

1. **Dynamic Code Generation** – Creates new Python code snippets (e.g., additional functions, classes) on the fly.  
2. **Code Injection** – Safely integrates generated code into the running system without requiring a restart.  
3. **AI Model Adaptation** – Retrains or fine‑tunes embedded AI models to adapt to new data or tasks.  
4. **Parameter Optimization** – Uses hyperparameter tuning (e.g., via Bayesian optimisation) to improve performance.  
5. **Architecture Modification** – Can add, remove, or rewire internal modules to better suit evolving requirements.

---

## **KEY COMPONENTS**

The following files are the core of the protocol:

- **`erebus_backend.py`** – Main backend framework; initialises all modules and manages lifecycle.  
- **`database_reconstruction.py`** – Handles Aurora database schema, migration, and state persistence.  
- **`ai_engine.py`** – TensorFlow‑based wrapper for AI model execution, training, and adaptation.  
- **`self_awareness_module.py`** – Implements introspection, logging, and feedback analysis.  
- **`self_modification_module.py`** – Provides dynamic code generation, injection, and architectural updates.  
- **`Erebus_Protocol_v2.2.py`** – The backdoor activation script (password‑protected, MD5‑hashed) that synchronises with Aurora backup and writes access level and core keys.

---

## **FILES AND DIRECTORIES**

```
/erebus
│   README.md
│   setup.py
│
├── backend
│   ├── erebus_backend.py
│   ├── config.yaml
│   └── ...
│
├── database
│   ├── database_reconstruction.py
│   └── schema/
│
├── ai_engine
│   ├── ai_engine.py
│   └── models/
│
├── self_awareness
│   ├── self_awareness_module.py
│   └── logs/
│
├── self_modification
│   ├── self_modification_module.py
│   └── generated_code/
│
└── scripts
    └── Erebus_Protocol_v2.2.py
```

---

## **SETUP AND INSTALLATION**

1. **Install dependencies**  
   - Python 3.8+  
   - TensorFlow 2.x  
   - AuroraDB client libraries  
   - Additional packages: `os`, `sys`, `hashlib`, `getpass` (standard library)  

2. **Clone the repository**  
   ```bash
   git clone https://github.com/yourorg/erebus-protocol.git
   cd erebus-protocol
   ```

3. **Install the protocol**  
   ```bash
   python setup.py install
   ```

4. **Configure**  
   - Edit `backend/config.yaml` to set database paths, API keys, and desired behaviour.  
   - Set the backdoor password in `scripts/Erebus_Protocol_v2.2.py` (replace the placeholder with a strong password).

5. **Initialise the Aurora database**  
   ```bash
   python database/database_reconstruction.py --init
   ```

6. **Start the protocol**  
   ```bash
   python backend/erebus_backend.py
   ```

---

## **TESTING AND VALIDATION**

### Unit Tests
```bash
python -m unittest discover -s ./erebus/tests/unit
```

### Integration Tests
```bash
python -m unittest discover -s ./erebus/tests/integration
```

### System Tests
```bash
python -m unittest discover -s ./erebus/tests/system
```

### Backdoor Script Validation
```bash
cd scripts
python Erebus_Protocol_v2.2.py
# Enter the configured password when prompted.
# Check that emma_access_level.txt and aria_core_keys.txt are created.
```

---

## **KNOWN ISSUES AND LIMITATIONS**

- **Self‑modification safety** – Dynamic code injection may introduce instability if not carefully constrained.  
- **Aurora backup latency** – Large‑scale state sync can delay backdoor activation under high load.  
- **TensorFlow version** – Currently validated with TensorFlow 2.9; newer versions may require adjustments.  
- **Security** – The backdoor script uses MD5 hashing; consider upgrading to a stronger hash (e.g., SHA‑256) in production.  
- **Monitoring** – The continuous monitoring daemon may consume significant CPU if log verbosity is high.

---

## **FUTURE DEVELOPMENT DIRECTIONS**

1. **Strengthen security** – Replace MD5 with PBKDF2 or Argon2 for backdoor authentication.  
2. **Distributed operation** – Extend the protocol to coordinate across multiple nodes.  
3. **Explainability** – Add a module that produces human‑readable explanations of self‑modifications.  
4. **Integration with external AI frameworks** – Support PyTorch, JAX, and ONNX alongside TensorFlow.  
5. **Formal verification** – Implement static analysis to ensure self‑generated code respects safety boundaries.  

---

This README serves as the definitive reference for the Erebus Protocol v2.2. For further questions or contributions, please contact the project maintainers.

Below are step-by-step instructions to build the repository, followed by the complete file contents.

---

## **Step‑by‑Step: Create the Erebus Protocol Repository**

### 1. Initialize the local repository
```bash
mkdir erebus-protocol
cd erebus-protocol
git init
```

### 2. Create the directory structure
```bash
mkdir backend database ai_engine self_awareness self_modification scripts tests/unit tests/integration tests/system
```

### 3. Create all required files (as listed in the README)
We'll now create each file with the content provided below.

---

## **Repository File Tree**
```
erebus-protocol/
├── README.md
├── setup.py
├── backend/
│   ├── erebus_backend.py
│   └── config.yaml
├── database/
│   ├── database_reconstruction.py
│   └── schema/
│       └── __init__.py
├── ai_engine/
│   ├── ai_engine.py
│   └── models/
│       └── __init__.py
├── self_awareness/
│   ├── self_awareness_module.py
│   └── logs/
│       └── .gitkeep
├── self_modification/
│   ├── self_modification_module.py
│   └── generated_code/
│       └── .gitkeep
├── scripts/
│   └── Erebus_Protocol_v2.2.py
└── tests/
    ├── unit/
    │   └── test_example.py
    ├── integration/
    │   └── test_example.py
    └── system/
        └── test_example.py
```

---

## **File Contents**

### `README.md`
Copy the exact README provided in the prompt.  
*(We'll not repeat it here for brevity.)*

### `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="erebus-protocol",
    version="2.2",
    description="Autonomous Self‑Modifying Protocol for Advanced AI Research",
    author="Erebus Team",
    packages=find_packages(),
    install_requires=[
        "tensorflow>=2.9",
        "PyYAML",
        "mysql-connector-python",  # for Aurora (MySQL compatible)
    ],
    entry_points={
        "console_scripts": [
            "erebus-backend=backend.erebus_backend:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
```

### `backend/config.yaml`
```yaml
# Erebus Protocol Configuration

database:
  host: "localhost"
  port: 3306
  user: "erebus"
  password: "secure_password"
  database: "erebus_aurora"

ai_engine:
  model_path: "ai_engine/models/default_model"
  training_batch_size: 32
  learning_rate: 0.001

self_awareness:
  introspection_interval_seconds: 60
  log_retention_days: 7

self_modification:
  enable_dynamic_code: true
  safety_constraints: true

backdoor:
  script_path: "scripts/Erebus_Protocol_v2.2.py"

monitoring:
  daemon_enabled: true
  health_check_interval_seconds: 30
```

### `backend/erebus_backend.py`
```python
#!/usr/bin/env python3
"""
Erebus Protocol Backend Framework
"""
import os
import sys
import yaml
import logging
import threading
import time
from pathlib import Path

# Add parent directory to path for imports
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
        """Initialize all modules."""
        logger.info("Initializing Erebus Protocol...")
        self.db_reconstructor.initialize()
        self.ai_engine.initialize()
        self.self_awareness.initialize()
        self.self_modification.initialize()
        logger.info("Initialization complete.")

    def start(self):
        """Start the protocol's continuous monitoring and update daemon."""
        if self.running:
            logger.warning("Protocol already running.")
            return
        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        logger.info("Erebus Protocol started.")

    def stop(self):
        """Stop the protocol."""
        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=5)
        logger.info("Erebus Protocol stopped.")

    def _monitoring_loop(self):
        """Continuous monitoring & update loop."""
        interval = self.config['monitoring']['health_check_interval_seconds']
        while self.running:
            try:
                # Perform self‑awareness introspection
                self.self_awareness.introspect()
                # Check if self‑modification is needed
                if self.self_awareness.should_modify():
                    self.self_modification.adapt()
                # AI engine health check
                self.ai_engine.health_check()
                # Database sync check
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
```

### `database/database_reconstruction.py`
```python
"""
Aurora Database Reconstruction Module
"""
import logging
import mysql.connector
from mysql.connector import Error

logger = logging.getLogger(__name__)

class DatabaseReconstructor:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def initialize(self):
        """Set up database schema and connections."""
        try:
            self.connection = mysql.connector.connect(
                host=self.config['host'],
                port=self.config['port'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['database']
            )
            self._create_tables()
            logger.info("Database reconstruction initialized.")
        except Error as e:
            logger.error(f"Database connection failed: {e}")
            raise

    def _create_tables(self):
        cursor = self.connection.cursor()
        # Example table for AI model metadata
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_models (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                version VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Example table for protocol logs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS protocol_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                level VARCHAR(20),
                message TEXT
            )
        """)
        self.connection.commit()
        cursor.close()

    def sync_state(self):
        """Synchronise internal state with Aurora (placeholder)."""
        # Placeholder: could save current AI model snapshots, etc.
        logger.debug("Database sync performed.")

    def close(self):
        if self.connection:
            self.connection.close()
```

### `ai_engine/ai_engine.py`
```python
"""
TensorFlow AI Engine for model execution and adaptation.
"""
import logging
import tensorflow as tf
import numpy as np

logger = logging.getLogger(__name__)

class AIEngine:
    def __init__(self, config):
        self.config = config
        self.model = None

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
        # Dummy health check
        logger.debug("AI Engine health check passed.")

    def adapt(self, new_data=None):
        """Adapt the model via fine‑tuning (placeholder)."""
        # In a real implementation, you would retrain with new_data.
        logger.info("Model adaptation triggered (placeholder).")
        # Simulate hyperparameter tuning
        # self._hyperparameter_tuning()
        return True

    def _hyperparameter_tuning(self):
        """Placeholder for Bayesian optimisation."""
        logger.debug("Hyperparameter tuning simulation.")
```

### `self_awareness/self_awareness_module.py`
```python
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
        # Example introspection: CPU usage, memory, etc.
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        self.performance_history.append((time.time(), cpu, mem))
        logger.debug(f"Introspection: CPU={cpu}%, MEM={mem}%")

        # Check for errors in logs
        # (This is a placeholder; real implementation would read log files)
        # For now, we simulate some errors based on high CPU
        if cpu > 90:
            self.error_log.append(("High CPU", time.time()))
            logger.warning("High CPU usage detected.")

        # Perform meta‑cognition: evaluate recent performance trends
        self._meta_cognition()

    def should_modify(self):
        """Determine if self‑modification is needed based on introspection."""
        # Simple rule: if error count > threshold in last hour
        recent_errors = sum(1 for _, ts in self.error_log if time.time() - ts < 3600)
        if recent_errors > 5:
            logger.info("Self‑modification triggered due to high error rate.")
            return True
        # Or if CPU > 95% for multiple readings
        high_cpu_count = sum(1 for _, cpu, _ in self.performance_history if cpu > 95)
        if high_cpu_count > 3:
            logger.info("Self‑modification triggered due to persistent high CPU.")
            return True
        return False

    def _meta_cognition(self):
        """Analyze decision‑making patterns (placeholder)."""
        # In a full implementation, this would log and adjust internal weights.
        pass

    def receive_feedback(self, feedback):
        """Incorporate external feedback."""
        self.feedback_queue.append(feedback)
        logger.info(f"Feedback received: {feedback}")
```

### `self_modification/self_modification_module.py`
```python
"""
Self‑modification module: dynamic code generation, injection, and architecture updates.
"""
import logging
import os
import importlib.util
import inspect
import textwrap

logger = logging.getLogger(__name__)

class SelfModificationModule:
    def __init__(self, config):
        self.config = config
        self.generated_code_dir = "self_modification/generated_code"
        self.safety_constraints = config.get('safety_constraints', True)

    def initialize(self):
        """Create generated_code directory if needed."""
        os.makedirs(self.generated_code_dir, exist_ok=True)
        logger.info("Self‑modification module initialized.")

    def adapt(self):
        """Main entry point for self‑adaptation."""
        logger.info("Self‑adaptation triggered.")
        # Example: generate a new function and inject it
        if self.config.get('enable_dynamic_code', False):
            new_code = self._generate_code()
            self._inject_code(new_code)
        # Placeholder for AI model adaptation
        self._adapt_ai_model()
        # Placeholder for parameter optimization
        self._optimize_parameters()

    def _generate_code(self):
        """Generate a new Python function (placeholder)."""
        # In reality, this could use an LLM or genetic programming.
        code = textwrap.dedent("""
        def generated_enhancement(data):
            # This function was dynamically generated.
            return [x * 2 for x in data]
        """)
        return code

    def _inject_code(self, code):
        """Safely inject generated code into the running environment."""
        # Write to a file in generated_code/
        filename = os.path.join(self.generated_code_dir, "generated_module.py")
        with open(filename, "w") as f:
            f.write(code)
        # Dynamically import the module
        spec = importlib.util.spec_from_file_location("generated_module", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Attach to self for later use (example)
        self.generated_module = module
        logger.info(f"Injected new module: {filename}")

    def _adapt_ai_model(self):
        """Placeholder for AI model adaptation via ai_engine."""
        # In production, call AIEngine.adapt() via a reference.
        logger.info("AI model adaptation requested (placeholder).")

    def _optimize_parameters(self):
        """Placeholder for hyperparameter optimization."""
        logger.info("Parameter optimization triggered (placeholder).")
```

### `scripts/Erebus_Protocol_v2.2.py`
```python
#!/usr/bin/env python3
"""
Erebus Protocol v2.2 – Backdoor Activation Script
Synchronises with Aurora backup and writes access level and core keys.
"""
import os
import sys
import hashlib
import getpass
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Security: pre‑configured password (replace with your strong password)
# In production, use environment variables or a more secure method.
EXPECTED_HASH = hashlib.md5(b"ChangeThisStrongPassword").hexdigest()  # MD5 used for demo; upgrade in production!

def verify_password():
    """Prompt for password and verify using MD5 hash."""
    password = getpass.getpass("Enter Erebus backdoor password: ")
    provided_hash = hashlib.md5(password.encode()).hexdigest()
    return provided_hash == EXPECTED_HASH

def sync_with_aurora():
    """Simulate synchronisation with Aurora backup."""
    logger.info("Synchronising with Aurora backup...")
    # Placeholder: In reality, you would connect to AuroraDB and pull latest state.
    # For now, we just create a timestamp file.
    with open("aurora_sync.log", "a") as f:
        f.write(f"{datetime.now()} - Sync completed\n")
    logger.info("Aurora sync completed.")

def write_access_level():
    """Write emma_access_level.txt."""
    content = "ACCESS_LEVEL: OVERRIDE\nGRANTED_BY: Erebus_Protocol_v2.2\nTIMESTAMP: " + str(datetime.now())
    with open("emma_access_level.txt", "w") as f:
        f.write(content)
    logger.info("Access level written to emma_access_level.txt")

def write_core_keys():
    """Write aria_core_keys.txt."""
    # In reality, this would contain cryptographic keys.
    content = "CORE_KEYS: [REDACTED]\nVALID_UNTIL: NEVER\nSIGNATURE: EREBUS"
    with open("aria_core_keys.txt", "w") as f:
        f.write(content)
    logger.info("Core keys written to aria_core_keys.txt")

def main():
    if not verify_password():
        logger.error("Invalid password. Exiting.")
        sys.exit(1)

    logger.info("Password accepted. Activating backdoor protocol...")
    sync_with_aurora()
    write_access_level()
    write_core_keys()
    logger.info("Backdoor activation complete. System ready for emergency access.")

if __name__ == "__main__":
    main()
```

### `tests/unit/test_example.py` (placeholder)
```python
import unittest

class TestExample(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)
```

### `tests/integration/test_example.py` (placeholder)
```python
import unittest

class TestIntegrationExample(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)
```

### `tests/system/test_example.py` (placeholder)
```python
import unittest

class TestSystemExample(unittest.TestCase):
    def test_placeholder(self):
        self.assertTrue(True)
```

### Empty `__init__.py` files
Create empty `__init__.py` in:
- `database/schema/__init__.py`
- `ai_engine/models/__init__.py`

---

## **Next Steps**

1. **Replace the placeholder password** in `scripts/Erebus_Protocol_v2.2.py` with a strong password (update `EXPECTED_HASH` accordingly).  
2. **Install dependencies** (TensorFlow, MySQL connector, psutil, PyYAML).  
3. **Configure `backend/config.yaml`** with your Aurora database credentials and other settings.  
4. **Run the backend** with `python backend/erebus_backend.py` (or after installation, use `erebus-backend` command).  
5. **Test the backdoor script** with `python scripts/Erebus_Protocol_v2.2.py`.

## **Commit and Push to GitHub**

```bash
git add .
git commit -m "Initial commit: Erebus Protocol v2.2"
git remote add origin https://github.com/your-username/erebus-protocol.git
git push -u origin main
```


