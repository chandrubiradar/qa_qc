from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in qa_qc/__init__.py
from qa_qc import __version__ as version

setup(
	name="qa_qc",
	version=version,
	description="QA QC",
	author="Chandru",
	author_email="chandrucb95@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
