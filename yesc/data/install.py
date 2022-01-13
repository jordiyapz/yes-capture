import enum
from os import PathLike
import gdown
import click
from pathlib import Path
from dotenv import dotenv_values
from pydrive import auth
from pydrive.files import ApiRequestError
import questionary as que
import threading
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from yesc.utils import unzip_all

config = dotenv_values('.config')

data_path = Path(config['DATA_PATH'])
download_path = Path(config['DOWNLOAD_PATH'])
model_path = Path(config['MODEL_PATH'])

drive: GoogleDrive = None
drive_auth_lock = threading.Lock()


def download_unzip(id, filename, target):
    url = f'https://drive.google.com/uc?id={id}'
    filepath = gdown.download(
        url, str(download_path/filename), resume=True, quiet=True)
    unzip_all(filepath, target)


def initialize_gdrive():
    drive_auth_lock.acquire()

    global drive
    if drive:
        return
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    drive_auth_lock.release()


def install_with_auth(id, filename: PathLike, target):
    filepath = download_path/filename
    if not filepath.exists():
        print(f'File {str(filename)} not exists   ')
        initialize_gdrive()
        visualization_file = drive.CreateFile({'id': id})
        try:
            print(f'Downloading to: {filepath}  ')
            visualization_file.GetContentFile(filepath)
        except ApiRequestError as e:
            print(
                f'File {filename} not found. Please ask my developer for file access.')
            return

    print(f'Unzipping {filename} ')
    unzip_all(filepath, target)


def install_processed_data():
    download_unzip(config['PROCESSED_DATA'], 'processed.zip', data_path)


def install_models():
    download_unzip(config['MODELS'], 'models.zip', model_path)


def install_visualizations():
    download_unzip(config['VISUALIZATIONS'], 'visualizations.zip', data_path)


def install_raw_v1():
    install_with_auth(config['RAW_DATA_V1'],
                      'raw_v1.zip', data_path/'raw')


def install_raw_v2():
    install_with_auth(config['RAW_DATA_V2'],
                      'raw_v2.zip', data_path/'raw')


def install_demo():
    install_with_auth(config['DEMO'],
                      'demo.zip', data_path)


def install_many(installer_scripts):
    threads = (threading.Thread(target=script) for script in installer_scripts)
    try:
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print('Installation successful.')
    except Exception as ex:
        print(ex)
        print('Installation failed.')


class Module(enum.Enum):
    DATASET = ('dataset', install_processed_data)
    MODELS = ('models', install_models)
    RAW_V1 = ('raw_v1', install_raw_v1)
    RAW_V2 = ('raw_v2', install_raw_v2)
    VISUALIZATIONS = ('visualizations', install_visualizations)
    DEMO = ('demo', install_demo)


@click.command()
def install():
    '''
    An installation wizard.

    This installation wizard that will guide you to download and install requirements such as dataset, models, raw data, etc.
    '''

    module_choices = [
        que.Choice('Dataset', Module.DATASET),
        que.Choice('Models', Module.MODELS),
        que.Choice('Visualization', Module.VISUALIZATIONS),
        que.Choice('Raw_v1 (requires permission)', Module.RAW_V1),
        que.Choice('Raw_v2 (requires permission)', Module.RAW_V2),
        que.Choice('Demo (requires permission)', Module.DEMO),
    ]

    choose_type = que.select('Choose your installation preference:',
                             choices=[
                                 que.Choice('Essentials (models + dataset)',
                                            [Module.MODELS, Module.DATASET]),
                                 que.Choice('Minimal (models only)',
                                            [Module.MODELS]),
                                 que.Choice('Full (requires permission)', [
                                            e for e in Module]),
                                 que.Choice('Custom', 'custom')
                             ])

    custom_install = que.checkbox('Select which resources you need:',
                                  choices=module_choices)

    installation_preferences = choose_type.ask()

    if not installation_preferences:
        return print('Bye 👋')

    if installation_preferences == 'custom':
        installation_preferences = custom_install.ask()

    install_many([module.value[1] for module in installation_preferences])
