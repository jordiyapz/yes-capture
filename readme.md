# Yes, Capture!

An application to demonstrate functionality of capturing image using "Y" hand pose according to American Sign Language (ASL) hand sign.

## Presentation

Here is the link to our presentation about this project: https://youtu.be/RfqfMxAONUQ

## Installation

1. Clone this repository to your local: `git clone https://github.com/jordiyapz/yes-capture.git`
2. Change your working directory to the installed folder: `cd yes-capture`
3. Install this repository by running `pip install -e .` (The dot `.` means current directory).
4. Install the modules by running `py yesc/data/cli.py install`
5. Choose either `Minimal` for quick and easy usage or `Essentials` for additional dataset (optional).

## How to run

The main app resides on the directory `notebooks/11_the_app.ipynb`. Just run the notebook inside jupyter notebook or vscode notebook extension.

Other notebooks are the pipeline for rebuilding the app, including the experimentations. If you want to re-run the pipeline, do so by running from notebook `7_create_dataset_v2.ipynb`. The previous numbered notebooks runs the v1 experiments and does not correlate with the v2. Ofcourse you can run every notebook from `1_...` to `11_...`, just make sure you have the additional modules from below.

Full requirements are listed below:

1. `1_hand_pose_demo.ipynb`: Nothing => Nothing
2. `2_create_dataset.ipynb`: `data/raw/v1/*` => `data/processed/v1/Landmark Dataset.csv`
3. `3_dataset_visualization.ipynb`: `data/processed/v1/Landmark Dataset.csv` => `data/visualizations`
4. `4_dataset_split.ipynb`: `data/processed/v1/Landmark Dataset.csv` => `data/processed/v1/*`
5. `5_build_model_v1.ipynb`: `data/processed/v1/*` => `models/landmark-classifier_v1`
6. `6_using_model_v1.ipynb`: `models/landmark-classifier_v1` => Nothing
7. `7_create_dataset_v2.ipynb`: `data/raw/v2/*` => `data/processed/v2/landmark_ds_v2.csv`
8. `8_dataset_split_v2.ipynb`: `data/processed/v2/landmark_ds_v2.csv` => `data/processed/v2/*`
9. `9_build_model_v2.ipynb`: `data/processed/v2/*` => `models/landmark-classifier_v2`
10. `10_using_model_v2.ipynb`: `models/landmark-classifier_v2` => Nothing
11. `11_the_app.ipynb`: `models/landmark-classifier_v2` => Nothing

## Modules

Here are the modules available:

1. `models.zip`
2. `processed.zip`
3. `visualizations.zip`
4. `raw_v1.zip` (requires permission)
5. `raw_v2.zip` (requires permission)
7. `demo.zip` (requires permission)

## Acquiring Additional Modules Installation

Additional modules, i.e. demo and raw data contains creator's personal identity. Therefore, they are restricted to personal and collaborator use only. Those are not required to run the application but if you need to run the whole pipeline to reproduce the app, then raw data is required.

1. Contact me at [jordiyaputra@gmail.com](mailto://jordiyaputra@gmail.com) to request for the permission.
2. Re/run the module installation scripts: `py yesc/data/cli.py install`
3. You will need to click the link in the command line. The link looks like https://accounts.google.com/o/oauth2/auth?...
4. You will be prompted to choose a google account to authenticate. Select the one you were given permission to (from step 1).
5. A warning will be prompted and you will require to trust the application by clicking "Advanced", then click "Open ML Drive (not save)", and then click "Next" button. Nothing will be taken from your GDrive except the required file that is shared to you (You can always check the sourcecode to confirm yourself). If you dont trust this step, see section [Download Manually](https://github.com/jordiyapz/yes-capture#download-manually).

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
