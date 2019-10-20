import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myce",
    version="0.0.1",
    author="Steve Bradly",
    author_email="stevebradley@gmail.com",
    description="API definitions and client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rotwatsb/myce",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
