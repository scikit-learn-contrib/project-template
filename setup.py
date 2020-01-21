import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hqc", # Replace with your own username
    version="0.0.3",
    author="Leo Chow",
    author_email="leo_ckl@hotmail.com",
    description="A package for the Helstrom Quantum Centroid classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leockl/helstrom-quantum-centroid-classifier",
    keyword=["machine learning", "classification", "classifier", "Helstrom", "helstrom", "Quantum", "quantum", "Quantum-inspired", "quantum-inspired"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
