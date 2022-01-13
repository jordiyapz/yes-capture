# Yes, Capture!

An application to demonstrate functionality of capturing image using "Y" hand pose according to American Sign Language (ASL) hand sign.

## Installation

1. Clone this repository to your local: `git clone https://github.com/jordiyapz/yes-capture.git`
2. Change your working directory to the installed folder: `cd yes-capture`
3. Install this repository by running `pip install .` (The dot `.` means current directory).
4. Install the modules by running `py yesc/data/cli.py install`
5. Choose either `Minimal` for quick and easy usage or `Essentials` for additional dataset (optional).

## How to

## Acquiring Additional Installation

Additional modules, i.e. demo and raw data contains creator's personal identity. Therefore, they are restricted to personal and collaborator use only. Those are not required to run the application but if you need to run the whole pipeline to reproduce the app, then raw data is required.

1. Contact me at [jordiyaputra@gmail.com](mailto://jordiyaputra@gmail.com) to request for the permission.
2. Re/run the module installation scripts: `py yesc/data/cli.py install`
3. You will need to click the link in the command line. The link looks like https://accounts.google.com/o/oauth2/auth?...
4. You will be prompted to choose a google account to authenticate. Select the one you were given permission to (from step 1).
5. A warning will be prompted and you will require to trust the application by clicking "Advanced", then click "Open ML Drive (not save)", and then click "Next" button. Nothing will be taken from your GDrive except the required file that is shared to you (You can always check the sourcecode to confirm yourself). If you dont trust this step, see section (Download Manually)

### Download Manually

1. Go to your drive and manually download the shared files to the `downloads` folder in this working directory.
2. Arrange the files in the `downloads` folder following this structure:

```
  # yes-capture folder

  data
  downloads
  |- demo.zip
  |- raw_v1.zip
  |- raw_v2.zip
  |- # rest of the previously downloaded modules.
  libraries
  models
  notebooks
  yesc
  # Etc
```

3. Run `py yesc/data/cli.py install`

## Credits

1. Big thanks to Mediapipe for the Hands library.
2. This project is using structure that was highly inspired from [this article](https://towardsdatascience.com/structuring-machine-learning-projects-be473775a1b6).
