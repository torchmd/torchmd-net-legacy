import setuptools
import subprocess
import os

try:
    version = (
        subprocess.check_output(["git", "describe", "--abbrev=0", "--tags"])
        .strip()
        .decode("utf-8")
    )
except Exception as e:
    print("Could not get version tag. Defaulting to version 0")
    version = "0"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

if __name__ == "__main__":
    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="torchmdnet",
        version=version,
        author="Acellera",
        author_email="info@acellera.com",
        description="TorchMD-net. Training Schnet with pytorch lighthing",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/torchmd/torchmd-net/",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX :: Linux",
            "License :: OSI Approved :: MIT License",
        ],
        packages=setuptools.find_packages(include=["torchmdnet*"], exclude=[]),
        # package_data={"torchmdnet": ["config.ini", "logging.ini"],},
        install_requires=requirements,
    )
