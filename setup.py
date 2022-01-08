from setuptools import setup

setup(
    name='yes_capture',
    version='0.1.0',
    author='Jordi Yaputra',
    packages=['yesc'],
    # package_dir={'': 'src', 'utils': 'utils'},
    install_requires=['tensorflow', 'pandas',
                      'matplotlib', 'opencv-python', 'mediapipe'],
)
