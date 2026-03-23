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
        "mysql-connector-python",
        "psutil",
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
