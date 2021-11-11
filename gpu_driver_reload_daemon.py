import subprocess
import time
import logging

logging.basicConfig(level=logging.INFO, filename='reset-gpu.log', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("server started!")

## Need to add 2 lines to docker_start_gpu.sh
#### export PATH=$PATH:$(pwd)
#### sudo -E env "PATH=$PATH" python3 gpu_driver_reload_daemon.py &

def check_gpu_driver():
    result = subprocess.Popen("nvidia-smi", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = result.communicate()
    if output:
        out_msg = output.decode("utf-8")
        if 'version mismatch' in out_msg:
            # print('Trying to reset GPU driver...')
            logging.info('Identified there was a GPU driver upgrade! Trying to reset GPU driver now...')
            output_reset, err_reset = subprocess.Popen("sudo ./reset-gpu.sh", shell=True, stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE).communicate()
            if output_reset:
                # print('GPU driver reset was successful!\n' + output_reset.decode('utf-8'))
                logging.info('GPU driver reset was successful!\n' + output_reset.decode('utf-8'))
            else:
                # print('Failed to reset GPU driver. \n' + err_reset.decode('utf-8'))
                logging.error('Failed to reset GPU driver. \n' + err_reset.decode('utf-8'))
        else:
            logging.info('GPU driver runs properly! No need to do anything.')
    else:
        err_msg = err.decode("utf-8")
        # print('GPU driver fails!\n' + err_msg)
        logging.error('GPU driver fails!\n' + err_msg)
        if 'version mismatch' in err_msg:
            # print('Trying to reset GPU driver...')
            logging.info('Trying to reset GPU driver...')
            output_reset, err_reset = subprocess.Popen("sudo ./reset-gpu.sh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            if output_reset:
                # print('GPU driver reset was successful!\n' + output_reset.decode('utf-8'))
                logging.info('GPU driver reset was successful!\n' + output_reset.decode('utf-8'))
            else:
                # print('Failed to reset GPU driver. \n' + err_reset.decode('utf-8'))
                logging.error('Failed to reset GPU driver. \n' + err_reset.decode('utf-8'))


if __name__ == '__main__':
    while True:
        check_gpu_driver()
        time.sleep(1800)
