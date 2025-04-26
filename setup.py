from setuptools import find_packages,setup

setup(name="e-commerce-bot",
      version="0.0.1",
      author="shilpa",
      author_email="shilpa.ingole@gmail.com",
      packages=find_packages(),
      install_requires=["langchain_astradb","langchain"])