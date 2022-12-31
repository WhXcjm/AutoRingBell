# 自动打铃系统	——by WhXcjm
## 1. 概述
作用：
 - 在网课期间起到重要作用（提醒老师开始上课:p）
 - 可自动校时（根据aliyun的ntp服务器进行校对）（须以管理员身份运行）
 - 通过自定义音频输入输出通道来实现功能
## 注意：须配合[voicemeeter banana](https://vb-audio.com/Voicemeeter/banana.htm)使用
## 2. 使用方式（参考配置，建议先查教程自己学会）
### 2.1. 设置默认音频输出通道（或者在直播软件中设置）
1. 系统默认音频输出

![assets\系统默认音频输出.png](assets\系统默认音频输出.png)

2. 直播软件默认音频输出（以腾讯会议为例）

![assets\软件默认音频输出.png](assets\软件默认音频输出.png)
### 2.2. 配置banana的音频通道
![assets\banana主面板.png](assets\banana主面板.png)

面板详细解析：
1. `HARDWARE INPUT 1`, 会议临时发言用的麦克风 到 banana输入
2. `HARDWARE INPUT 2`, 系统默认麦克风输入 到 banana输入
（同时开微信语音等等用，注意即使实际使用同一麦克风，也要选择新的协议而不能和`HARDWARE INPUT 1`相同）
3. `VoiceMeeter Input`, 铃声输出 到 banana输入
4. `VoiceMeeter Aux Input`, 其他软件声音输出（系统默认输出） 到 banana输入
5. `HARDWARE OUTPUT 1 (A1)`, banana输出 到 系统扬声器
6. `VoiceMeeter Output (B1)`, banana输出 到 直播软件音频输入
7. `VoiceMeeter Aux Output (B2)`, banana输出 到 其他软件音频输入（系统默认输入）
![assets\其他软件音频输入.png](assets\其他软件音频输入.png)
### 2.3. 麦克风快捷按键
![assets\麦克风控制.png](assets\麦克风控制.png)
1. 非锁定式-`F4`（按下说话，抬起停止）

![assets\麦克风控制(F4-非锁定).png](assets\麦克风控制(F4-非锁定).png)

2. 锁定式-`Shift+F4`（点击→按下抬起→说话，再点击→按下抬起→停止）

![assets\麦克风控制(Shift+F4-锁定).png](assets\麦克风控制(Shift+F4-锁定).png)
## 3. 特别鸣谢
 - [voicemeeter banana](https://vb-audio.com/Voicemeeter/banana.htm)，非常好用的模拟声卡软件👍
 - module：pygame，提供轻松的音频输出通道
## 4. 下一步
pygame有亿点卡（开启缓慢），求教是否有其他方便的第三方库以实现特定音频通道输出功能