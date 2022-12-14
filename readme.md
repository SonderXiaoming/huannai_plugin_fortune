# Huannai_plugin_fortune

一个适用hoshinobot的 运势 插件

改自[nonebot_plugin_fortune](https://github.com/MinatoAquaCrews/nonebot_plugin_fortune)的运势插件（仅仅做了hoshino适配）

感谢 [MinatoAquaCrews](https://github.com/MinatoAquaCrews)

插件后续将继续在 github 不定期更新（主要等上游），欢迎提交 isuue 和 request

本插件仅供学习研究使用，插件免费，请勿用于违法商业用途，一切后果自己承担

## 项目地址：

https://github.com/SonderXiaoming/huannai_plugin_fortune

## 说明

1. 随机抽取今日运势，配置多种抽签主题：原神、PCR、Hololive、东方、东方归言录、明日方舟、赛马娘、阴阳师、碧蓝航线、碧蓝幻想、战双帕弥什，galgame主题等……

2. 可指定主题抽签；

3. 每群每人一天限抽签1次，0点刷新（贪心的人是不会有好运的🤗）抽签信息并清除`./resource/out`下生成的图片；

4. 抽签的信息会保存在`./resource/fortune_data.json`内；群抽签设置及指定抽签规则保存在`./resource/fortune_setting.json`内；抽签生成的图片当天会保存在`./resource/out`下；

5. 插件启动时将自动检查抽签主题启用情况，当全部为`false`会抛出错误。
6. 资源缺失自动检查！插件启动时，将自动检查资源是否缺失（除字体与图片资源），会尝试从repo中下载，但不保证成功
7.  原神、PCR、东方具有特殊文案，不要改动他们的底图

## 群友指令

```
一般抽签：运势；
指定主题抽签：[xx抽签]，例如：pcr抽签、holo抽签、碧蓝抽签；
抽签设置：查看当前群抽签主题的配置；
今日运势帮助：显示插件帮助文案；
查看（抽签）主题：显示当前已启用主题；
```

## 狗管理指令

```
- 配置抽签主题：
   - 设置[原神/pcr/东方/vtb/xxx]签：设置群抽签主题；
   - 主题启用xx，例如：主题启用pcr
   - 主题禁用xx，例如：主题禁用pcr
   - 重置（抽签）主题：设置群抽签主题为随机；
```

### 超管指令

```
- 刷新抽签：全局即刻刷新抽签，防止过0点未刷新
```

## 简单食用教程：

1. 下载或git clone本插件：

   在 HoshinoBot\hoshino\modules 目录下使用以下命令拉取本项目

   ```
   git clone https://github.com/SonderXiaoming/huannai_plugin_fortune
   ```
2. 安装依赖`pip3 install pydantic`或`pip install pydantic`

3. 在 HoshinoBot\hoshino\config\ `__bot__.py` 文件的 MODULES_ON 加入 'huannai_plugin_fortune'

   然后重启 HoshinoBot

4. 一些功能可自由配置，具体配置内容见下文

使用[FloatTech-zbpdata/Fortune](https://github.com/FloatTech/zbpdata)全部主题。在`config.py`下设置`xxx_FLAG`以启用或关闭抽签随机主题（默认全部开启），例如：

```
ARKNIGHTS_FLAG=true         # 明日方舟
ASOUL_FLAG=false            # A-SOUL
AZURE_FLAG=true             # 碧蓝航线
GENSHIN_FLAG=true           # 原神
ONMYOJI_FLAG=false          # 阴阳师
PCR_FLAG=true               # 公主连结
TOUHOU_FLAG=true            # 东方
TOUHOU_LOSTWORD_FLAG=true   # 东方归言录
TOUHOU_OLD_FLAG=false       # 东方旧版
HOLOLIVE_FLAG=true          # Hololive
PUNISHING_FLAG=true         # 战双帕弥什
GRANBLUE_FANTASY_FLAG=true  # 碧蓝幻想
PRETTY_DERBY_FLAG=true      # 赛马娘
DC4_FLAG=false              # dc4
EINSTEIN_FLAG=true          # 爱因斯坦携爱敬上
SWEET_ILLUSION_FLAG=true    # 灵感满溢的甜蜜创想
LIQINGGE_FLAG=true          # 李清歌
HOSHIZORA_FLAG=true         # 星空列车与白的旅行
SAKURA_FLAG=true            # 樱色之云绯色之恋
SUMMER_POCKETS_FLAG=true    # 夏日口袋
AMAZING_GRACE_FLAG=true     # 奇异恩典·圣夜的小镇
```

## 更新日志

1.0.0 好的开始

1.1.0 增加分群设置多个主题

1.1.1 修复权限设置，修复小bug，优化代码

## 抽签图片及文案资源

1. [opqqq-plugin](https://github.com/opq-osc/opqqq-plugin)：原神、PCR、Hololive抽签主题；
2. 感谢江樂丝提供东方签底；
3. 东方归言录(Touhou Lostword)：[KafCoppelia](https://github.com/KafCoppelia)；
4. [FloatTech-zbpdata/Fortune](https://github.com/FloatTech/zbpdata)：其余主题签；
5. 新版运势文案资源：[KafCoppelia](https://github.com/KafCoppelia)。`copywriting.json`整合了関係運、全体運、勉強運、金運、仕事運、恋愛運、総合運、大吉、中吉、小吉、吉、半吉、末吉、末小吉、凶、小凶、半凶、末凶、大凶及700+条运势文案！来自于Hololive早安系列2019年第6.10～9.22期，有修改。
