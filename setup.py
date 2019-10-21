import setuptools
import setupextras

packages = setupextras.get_packages()
requirements = setupextras.get_requirements()
readme = setupextras.get_readme()

setuptools.setup(
    name="myce",
    version="0.0.1",
    author="Steve Bradley",
    author_email="stevebradley@gmail.com",
    description="API definitions and client",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rotwatsb/myce",
    packages=packages,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
