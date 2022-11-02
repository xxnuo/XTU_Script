# coding=utf-8
import subprocess
import sys
import ctypes
import os

def exec(cmd, isStr=True, timeout=1800000):
    try:
        sp = subprocess.Popen(
            cmd,
            shell=isStr,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        sp.wait(timeout=timeout)

        stderr = str(sp.stderr.read().decode("utf-8")).strip()
        stdout = str(sp.stdout.read().decode("utf-8")).strip()
        if stderr.find("denied") > -1:
            raise Exception("无法获取管理员权限，程序退出")
        elif "" != stderr:
            raise Exception(stderr)
    except Exception as e:
        raise e
    print("**** Exec Successful ****")


path_exe = r'"XtuCLI.exe"'

cml_help = "{} -h"
cml_info_all = "{} -i all"
cml_tune = "{} -t -id {} -v {}"
cml_mon = "{} -m -id {}"

tune_id = {
    "Turbo Boost Power Max": 48,
    "Turbo Boost Short Power Max": 47,
    "Turbo Boost Power Time Window": 66
}

tune_v_fix = {
    "Turbo Boost Power Max": 28,
    "Turbo Boost Short Power Max": 70,
    "Turbo Boost Power Time Window": 32
}

tune_v_savepower = {
    "Turbo Boost Power Max": 8,
    "Turbo Boost Short Power Max": 15,
    "Turbo Boost Power Time Window": 24
}

tune_v_default = {
    "Turbo Boost Power Max": 25,
    "Turbo Boost Short Power Max": 60,
    "Turbo Boost Power Time Window": 28
}


def tune_mode(dict_tune_v):
    for name, id in tune_id.items():
        print("\n设置: {} = {}".format(name, dict_tune_v[name]))
        exec(cml_tune.format(path_exe, id, dict_tune_v[name]))

def info():
    exec(cml_info_all.format(path_exe))
    
# main    
path_exe = r'"C:\Program Files (x86)\Intel\Intel(R) Extreme Tuning Utility\Client\XtuCLI.exe"'

if not ctypes.windll.shell32.IsUserAnAdmin():
    # print("请以管理员权限运行程序")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    # exec(cml_info_all.format(path_exe))
    exit(0)


if len(sys.argv) > 1:
    mode = sys.argv[1].strip().lower()
    print("激活配置:{}".format(sys.argv[1]))
    if mode == "save" or mode == "savepower" or mode == "energy":
        tune_mode(tune_v_savepower)
    elif mode == "fix" or mode == "game" or mode == "gaming":
        tune_mode(tune_v_fix)
    elif mode == "info" or mode == "show":
        info()
    else:
        print("模式名称出错，请重新输入")
else:
    print("激活配置:默认")
    tune_mode(tune_v_default)

input()