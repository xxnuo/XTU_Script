# coding=utf-8
import subprocess
import sys
import ctypes

# 是否显示命令行窗口。1显示，0不显示则看不到窗口和输出
ShowCmd = 1
# 执行完后是否直接退出。0保留窗口，1直接退出。当 ShowCmd = 1 时该配置有效
DirectExit = 0
# 如果你的安装位置不同，在这里修改，一般不需要修改
path_exe = r'"C:\Program Files (x86)\Intel\Intel(R) Extreme Tuning Utility\Client\XtuCLI.exe"' 


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


# 各种命令对应的命令行，第一个{}默认对应path_exe
cml_help = "{} -h"
cml_info_all = "{} -i all"
cml_tune = "{} -t -id {} -v {}"
cml_mon = "{} -m -id {}"

# 配置项对应的ID，不能修改和删除
# 可以添加你需要的其他项：在执行了info之后在`C:\XTU_xmlFiles\Tuning.txt`内找到其他条目
tune_id = {
    "Turbo Boost Power Max": 48,
    "Turbo Boost Short Power Max": 47,
    "Turbo Boost Power Time Window": 66
}

# 各种模式对应的项目的数值，可以根据需要修改
# 下面是我提供的供我的笔记本电脑使用的配置数值
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


if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, ShowCmd)
    exit(0)


if len(sys.argv) > 1:
    mode = sys.argv[1].strip().lower()
    print("激活配置:{}".format(sys.argv[1]))
    
    # 可以自己仿造在下面添加配置
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

if ShowCmd and (not DirectExit):
    input()