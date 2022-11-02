# XTU_Script
Intel(R) Extreme Tuning Utility Service Control Script - XTU 自动超频脚本

Use Script to control XTU's functions whitout GUI (PerfTune.exe)

通过脚本控制 XTU 超频，而非官方 GUI，可以减少一个后台常驻应用。

> 虽然官方 GUI 可以在应用了 Profile 之后就退出，也不影响超频设置，但总归不方便。lazy...

Usage:

- Make sure XTU (Intel(R) Extreme Tuning Utility) Service running automatically

> The Service is usually installed with XTU automatically and starts in a while with the system login

- Download and Place `xtu.py` to `C:\XTU_xmlFiles` folder

- Excute the following command:

```bash
# Energe Saving Mode Profile
# 省电模式
python "C:\XTU_xmlFiles\xtu.py" save


# Gaming Mode Profile
# 性能模式
python "C:\XTU_xmlFiles\xtu.py" game

# Show Mode Profile
# 查看当前超频信息
python "C:\XTU_xmlFiles\xtu.py" info

```

你可以根据自己的需求修改脚本使用。
You can modify the script to meet your needs.
![src](./img0.png)

比如文件 `quickCommand.json` 是我的`utools`的插件`快捷命令`的配置,可以让我快速切换模式

![panel](./img1.png)
![use](./img2.png)


Others Content

\n************ Tuning Information *****************\n

48           Turbo Boost Power Max          8.000W     1.000      4095.875   0.125      7994      

47           Turbo Boost Short Power Max    15.000W    1.000      4095.875   0.125      7994      

49           Turbo Boost Short Power Max Enable 1          0          1          1          2         

66           Turbo Boost Power Time Window  24Seconds  0.25       96.0       0.062      35        

110                                         0          0          1          1          2         

80           Overclocking Lock              1          0          1          1          2         

50           Package Turbo Power Lock       0          0          1          1          2         

41           Enhanced Intel® SpeedStep Technology 1          0          1          1          2         

26           Intel® Turbo Boost Technology  1          0          1          1          2         

2            Core Voltage                   0V         0          2.000      0.500      1538      

34           Core Voltage Offset            0mV        -1000      999        1          2048      

102          Processor Core IccMax          64.000A    1.000      255.750    0.250      1020      

81           Processor Graphics Voltage     0V         0          2.000      0.500      1538      

83           Processor Graphics Voltage Offset 0mV        -1000      999        1          2048      

104          Processor Graphics IccMax      31.000A    1.000      255.750    0.250      1020      

77           Cache Voltage                  0V         0          2.000      0.500      1538      

79           Cache Voltage Offset           0mV        -1000      999        1          2048      

106          Cache IccMax                   64.000A    1.000      255.750    0.250      1020      

105          Processor Graphics Unslice IccMax 31.000A    1.000      255.750    0.250      1020      

99           Processor Graphics Media Voltage 0V         0          2.000      0.500      1538      

100          Processor Graphics Media Voltage Offset 0mV        -1000      999        1          2048      

103          System Agent IccMax            6.000A     1.000      255.750    0.250      1020      

114          AVX Ratio Offset               0.0x       0.0        31.0       1.0        32        

29           1 Active Core                  40x        4          40         1          37        

30           2 Active Cores                 40x        4          40         1          37        

31           3 Active Cores                 37x        4          37         1          34        

32           4 Active Cores                 37x        4          37         1          34        

3489660933   Processor Core Ratio           37x        4          37         1          34        

