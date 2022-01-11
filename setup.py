from setuptools import setup

setup(
    name='yes_capture',
    version='1.0.0',
    author='Jordi Yaputra',
    packages=['yesc'],
    install_requires=['tensorflow', 'pandas',
                      'matplotlib', 'opencv-python', 'mediapipe'],
)
