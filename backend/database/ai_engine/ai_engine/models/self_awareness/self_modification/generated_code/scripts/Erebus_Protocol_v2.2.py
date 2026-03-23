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

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Security: pre‑configured password (replace with your strong password)
EXPECTED_HASH = hashlib.md5(b"ChangeThisStrongPassword").hexdigest()

def verify_password():
    """Prompt for password and verify using MD5 hash."""
    password = getpass.getpass("Enter Erebus backdoor password: ")
    provided_hash = hashlib.md5(password.encode()).hexdigest()
    return provided_hash == EXPECTED_HASH

def sync_with_aurora():
    """Simulate synchronisation with Aurora backup."""
    logger.info("Synchronising with Aurora backup...")
    with open("aurora_sync.log", "a") as f:
        f.write(f"{datetime.now()} - Sync completed\n")
    logger.info("Aurora sync completed.")

def write_access_level():
    """Write emma_access_level.txt."""
    content = f"ACCESS_LEVEL: OVERRIDE\nGRANTED_BY: Erebus_Protocol_v2.2\nTIMESTAMP: {datetime.now()}"
    with open("emma_access_level.txt", "w") as f:
        f.write(content)
    logger.info("Access level written to emma_access_level.txt")

def write_core_keys():
    """Write aria_core_keys.txt."""
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
