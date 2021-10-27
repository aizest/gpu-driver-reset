import subprocess

def run_command():
    # result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE)
    # try:
    #     result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     print(type(result.stdout.decode('utf-8')))
    # except subprocess.CalledProcessError as e:
    #     result = e.output
    #     print(result)
    result = subprocess.Popen("nvidia-smi", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = result.communicate()
    if output:
        print('GPU driver runs properly! No need to do anything.\n' + output.decode("utf-8"))
    else:
        err_msg = err.decode("utf-8")
        print('GPU driver fails!\n' + err_msg)
        if 'version mismatch' in err_msg:
            print('Trying to reset GPU driver...')
            output_reset, err_reset = subprocess.Popen("nvidia-smi", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if output_reset:
                print('GPU driver reset was successful!\n' + output_reset.decode('utf-8'))
            else:
                print('Failed to reset GPU driver. \n' + err_reset.decode('utf-8'))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_command()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
