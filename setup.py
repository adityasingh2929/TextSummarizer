import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"
REPO_NAME = "textsummarizer"
AUTHOR_USER_NAME = "adityasingh_2929"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "2022aditya29@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarizer tool using BERT model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/" + AUTHOR_USER_NAME + "/" + SRC_REPO + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "transformers",
        "torch",
        "nltk"
    ],
    python_requires=">=3.6"
)
