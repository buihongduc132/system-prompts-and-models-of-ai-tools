"""
Setup script for python_utilities package.
"""

from setuptools import setup, find_packages

with open("python_utilities/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-utilities",
    version="1.0.0",
    author="Codegen Bot",
    author_email="codegen@example.com",
    description="A comprehensive Python package providing utility functions for common mathematical operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/buihongduc132/system-prompts-and-models-of-ai-tools",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "coverage>=5.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.800",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

