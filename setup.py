import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="collectiondbf",
    version="1.1.0",
    author="Jesse Khorasanee",
    author_email="jessekhorasanee@gmail.com",
    description="Download all files in a Blackfynn collection via command line or gui",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tehsurfer/collectiondbf",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    install_requires=[
         'blackfynn',
         'requests',
        'progressbar2',
        'appdirs'
    ],
    python_requires='>=3.5',
)
