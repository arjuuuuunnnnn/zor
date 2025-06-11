from setuptools import setup, find_packages

setup(
    name="zor",
    version="0.0.5",
    description="An Open-Source Claude Code like tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Hemanth",
    author_email="arjunbanur27@gmail.com",
    license="MIT",
    license_file="LICENSE",
    python_requires=">=3.9",
    packages=find_packages(include=["zor"]),
    install_requires=[
        "google-generativeai==0.8.4",
        "python-dotenv==1.1.0",
        "typer==0.15.2",
        "rich==14.0.0",
        "pygments==2.19.1",
        "tqdm==4.67.1",
    ],
    keywords=["ai", "code", "assistant", "gemini", "development"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    entry_points={
        "console_scripts": ["zor=zor.main:app"],
    },
    project_urls={
        "Homepage": "https://github.com/arjuuuuunnnnn/zor",
        "Bug Tracker": "https://github.com/arjuuuuunnnnn/zor/issues",
    },
    include_package_data=True,
)
