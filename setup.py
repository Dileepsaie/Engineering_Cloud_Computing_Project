import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Engineering_Cloud_Computing_Project"
AUTHOR_USER_NAME = "Dileepsaie"
SRC_REPO = "ECC_Project"
AUTHOR_EMAIL = "dileepsaie@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Dileepsaie/Engineering_Cloud_Computing_Project.git",
    project_urls={
        "Bug Tracker": f"git@github.com:Dileepsaie/Engineering_Cloud_Computing_Project.git/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)