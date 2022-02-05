import platform
import subprocess
import chardet


def ping_info(site):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', site]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in result.stdout:
        result = chardet.detect(line)
        # print('result= ', result)
        line = line.decode(result['encoding'])
        print(line)

ping_info('yandex.ru')
ping_info('youtube.com')
