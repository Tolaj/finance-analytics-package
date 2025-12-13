from setuptools import setup, find_packages

setup(
    name="finalytics",
    version="0.1.0",
    description="Financial Calculations Package: TVM, cash flows, loans, depreciation, bonds, and visualization.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
)
