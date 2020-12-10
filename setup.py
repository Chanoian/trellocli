from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements


setup(
      name="trellocli",
      version="0.0.1",
      author_email="shanoian90@gmail.com",
      packages=find_packages(),
      package_data={},
      install_requires=read_requirements(),
      entry_points={
        'console_scripts': ['trellocli = trellocli.cli:trellocli']
      }
)