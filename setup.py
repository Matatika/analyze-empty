from setuptools import setup, find_packages

setup(
    name="analyze-empty",
    version="0.1.0",
    description="Meltano project empty file bundle",
    packages=find_packages(),
    package_data={
        "bundle": [
        ]
    },
)
