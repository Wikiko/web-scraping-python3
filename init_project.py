import os
import platform

def install_virtualenv(pip_version = ''):
    try:
        result = os.popen('pip{pip_version} install virtualenv'.format(pip_version=pip_version)).read()
        return 'success'.upper() in result.upper() or 'requirement already satisfied'.upper() in result.upper()
    except Exception as e:
        print('Something happen wrong, ', e)
        return False

def create_environment():
    print("Let's create an environment with name: {env}".format(env=env_name))
    try:
        result = os.popen('virtualenv {env_name}'.format(env_name=env_name)).read()
        return 'installing setuptools, pip, wheel...done'.upper() in result.upper()
    except Exception as e:
        print(e)
        return False

def install_env_dependences():
    system_platform = platform.system()
    try:
        if 'windows'.upper() in system_platform.upper():
            result = os.popen('cd ./{env_name}/Scripts && .\acivate.bat && pip install -r requirements.txt')
        else:
    except Exception as e:
        print(e)

def main():
    env_name='scrapingEnv'
    instalation_result = False
    python_version = os.popen('python --version').read()
    if '3' in python_version:
        instalation_result = install_virtualenv()
    elif '2' in python_version:
        another_python_version = os.popen('python3 --version')
        if '3' in another_python_version:
            instalation_result = install_virtualenv('3')
    
    if instalation_result is True:
        print('virtualenv installed...')
        env_creation_result = create_environment()
        if env_creation_result is True:
            print('nv created with sucessfull')

            print('Congratulations all is ready to go aread...')
    else:
        print('Sorry something was wrong.')


main()