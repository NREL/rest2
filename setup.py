"""
setup.py
"""
import os
import shlex
from codecs import open
from subprocess import check_call
from warnings import warn

from setuptools import find_packages, setup
from setuptools.command.develop import develop


class PostDevelopCommand(develop):
    """
    Class to run post setup commands
    """

    def run(self):
        """
        Run method that tries to install pre-commit hooks
        """
        try:
            check_call(shlex.split("pre-commit install"))
        except Exception as e:
            warn("Unable to run 'pre-commit install': {}"
                 .format(e))

        develop.run(self)


try:
    from pypandoc import convert_text
except ImportError:
    convert_text = lambda string, *args, **kwargs: string

here = os.path.abspath(os.path.dirname(__file__))

with open("README.rst", encoding="utf-8") as readme_file:
    readme = convert_text(readme_file.read(), "rst", format="rst")

with open("requirements.txt") as f:
    install_requires = f.readlines()

with open(os.path.join(here, "rest2", "version.py"), encoding="utf-8") as f:
    version = f.read()

version = version.split('=')[-1].strip().strip('"').strip("'")

test_requires = ["pytest>=5.2", ]
description = ("REST2 is the High-performance solar radiation model for "
               "cloudless-sky irradiance, illuminance, and "
               "photosynthetically active radiation")

setup(
    name="NREL-rest2",
    version=version,
    description=description,
    long_description=readme,
    author="Grant Buster",
    author_email="grant.buster@nrel.gov",
    url="https://github.com/NREL/",
    packages=find_packages(),
    package_dir={"rest2": "rest2"},
    include_package_data=True,
    zip_safe=False,
    keywords="rest2",
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite="tests",
    install_requires=install_requires,
    extras_require={
        "test": test_requires,
        "dev": test_requires + ["flake8", "pre-commit", "pylint"],
    },
    cmdclass={"develop": PostDevelopCommand},
)
