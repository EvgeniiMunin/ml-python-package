from setuptools import find_packages, setup


setup(
    name="ml_python_package_evgenii",
    packages=find_packages(),
    version="0.1.3",
    description="Training stuff",
    author="Evgenii",
    install_requires=["scikit-learn==0.24.1", "pandas==1.1.5",],
    license="MIT",
)
