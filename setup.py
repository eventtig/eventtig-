import setuptools

setuptools.setup(
    name="EventTig",
    version="0.0.1",
    description="A tool for working with crowd sourced event data in JSON files in a Git repository",
    long_description="A tool for working with crowd sourced event data in JSON files in a Git repository",
    url="https://github.com/eventtig/eventtig-gitengine",
    project_urls={
        "Issues": "https://github.com/eventtig/eventtig-gitengine/issues",
        "Source": "https://github.com/eventtig/eventtig-gitengine",
    },
    packages=setuptools.find_packages(exclude=["test"]),
    package_data={
        "": ["*.html", "*.txt", "*.css", "*.js"],
    },
    classifiers=[],
    install_requires=["pyyaml", "pytz", "Jinja2"],
    python_requires=">=3.6",
)
