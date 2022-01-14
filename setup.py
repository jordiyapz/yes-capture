from setuptools import setup

setup(
    name='yes_capture',
    version='1.0.0',
    author='Jordi Yaputra',
    packages=['yesc'],
    install_requires=['tensorflow', 'pandas', 'matplotlib', 'click', 'pydrive', 'ipykernel', 
                      'questionary', 'gdown', 'opencv-python', 'mediapipe', 'python-dotenv'],
    dependency_links=[
        'https://github.com/jordiyapz/myutils-python/releases/download/v0.1.0/myutils_python-0.1.0-py3-none-any.whl'],
)
