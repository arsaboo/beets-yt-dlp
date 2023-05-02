import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beets-yt-dlp",
    description="Download audio from youtube-dl soures and import into beets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arsaboo/beets-yt-dlp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'beets',
        'yt-dlp',
        'pyxdg',
    ]
)
