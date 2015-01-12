from setuptools import setup

setup(
    name="Yumpy",
    version="3.4.3",
    url="http://github.com/onlynone/yumpy",
    license="GNU General Public License v2 (GPLv2)",
    author="Steven Willis",
    install_requires=[],
    author_email="onlynone@gmail.com",
    description="Python package for yum extracted from the yum source",
    packages=["yum"],
    include_package_data=True,
    platforms="any",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        ],
)
