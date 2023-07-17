import telnetlib
import ctypes
import time

def main():
    while True:
        try:
            tn = telnetlib.Telnet('127.0.0.1', 2121)
            info_save = list()
            while True:
                data = tn.read_until(b"\n").decode("utf-8").replace('\n', '')
                data2 = data
                if 'Damage Given to' in data:
                    data = data.replace("Damage Given to ", "").replace('"', '').split(' in')[0].split('- ')
                    if int(data[-1]) < 100:
                        if data2 not in info_save:
                            info_save.append(data2)
                            data = data[0] + '-' + data[-1] + ' hp'
                            tn.write(f'say_team {data} \n'.encode('utf-8'))
                            time.sleep(1)
                        else:
                            info_save.remove(data2)
        except:
            print(f"failed to connect to csgo (game not open? -netconport 2121 not set?)")
            time.sleep(1)

if __name__ == '__main__':
    ctypes.windll.msvcrt.system(ctypes.c_char_p('cls'.encode())) # clear console

    print('''
█░█ █▀█   █ █▄░█ █▀▄ █ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█
█▀█ █▀▀   █ █░▀█ █▄▀ █ █▄▄ █▀█ ░█░ █▄█ █▀▄

█▄▄ █▄█   █▀▀ █▀▄▀█ █▀█ █▀█ █▀█ █▄█
█▄█ ░█░   ██▄ █░▀░█ █▀▀ █▄█ █▀▄ ░█░
https://github.com/emp0ry/''')
    main()
