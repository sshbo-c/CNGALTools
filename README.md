### 国产/官中代理Galgame工具 Chinese Galgame/Visual Novel Tools

### 游戏分析笔记 [点此处](https://github.com/YeLikesss/CNGALReverseNote)

#### 1.NVL(国G程序收费外包商)(Navila Software Japan)

* BKEngine (加密资源 加密文本)

    &emsp;BKEngineExtract (Ver2.0) (静态提取资源)

    &emsp;&emsp;解包.bkarc封包

    &emsp;&emsp;游戏测试

    &emsp;&emsp;&emsp;V2.0

    &emsp;&emsp;&emsp;&emsp;官网封包版本

    &emsp;&emsp;&emsp;V2.1(V2.0 HashVer)

    &emsp;&emsp;&emsp;&emsp;《十二色季节》

    &emsp;&emsp;&emsp;&emsp;《灭魂·误佳期》

    &emsp;&emsp;&emsp;V4.0

    &emsp;&emsp;&emsp;&emsp;《遥望彼方》

    &emsp;&emsp;&emsp;&emsp;《五等分的抢婚 三玖篇》

    &emsp;&emsp;&emsp;&emsp;《某一种青春》

    &emsp;&emsp;&emsp;&emsp;《他人世界末》

    &emsp;&emsp;依赖库

    &emsp;&emsp;&emsp;NuGet

    &emsp;&emsp;&emsp;&emsp;ICSharpCode.SharpZipLib

    &emsp;&emsp;&emsp;&emsp;Zstd.Net

    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

    &emsp;BKEFileNameDumper  (Dump V21Hash文件名)

    &emsp;&emsp;游戏测试

    &emsp;&emsp;&emsp;V2.1(V2.0 HashVer)

    &emsp;&emsp;&emsp;&emsp;《十二色季节》

    &emsp;&emsp;编译环境
    
    &emsp;&emsp;&emsp;MSVC2022 x86

    &emsp;状态说明

    &emsp;&emsp;1.Ver2.0已经算是最终版, 仅仅解密除文本外的所有资源

    &emsp;&emsp;2.游戏质量垃圾, 文本解密打不算研究

    &emsp;&emsp;3.该引擎官方已弃用, 转为NVLUnity

* NVLKRKR(内部定制收费版本) (加密资源 明文文本)

    &emsp;NVLKR2Extract (静态提取)

    &emsp;&emsp;静态解包NVLKR2封包  

    &emsp;&emsp;游戏测试

    &emsp;&emsp;&emsp;《橘子班短篇合集》

    &emsp;&emsp;&emsp;《高考恋爱100天》

    &emsp;&emsp;&emsp;《虹色旋律》

    &emsp;&emsp;&emsp;《祈风》

    &emsp;&emsp;&emsp;《雾之本境S》

    &emsp;&emsp;&emsp;《真恋寄语枫秋》

    &emsp;&emsp;&emsp;《余香》

    &emsp;&emsp;&emsp;《茸雪》

    &emsp;&emsp;&emsp;《回忆忘却之匣》

    &emsp;&emsp;&emsp;《花落冬阳》

    &emsp;&emsp;&emsp;《雪之本境S》

    &emsp;&emsp;&emsp;《丑小鸭的天鹅湖》

    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

    &emsp;NVLKrkrDump (动态提取) (Dump资源 Hash文件名)

    &emsp;&emsp;技术参考

    &emsp;&emsp;&emsp;项目引用[KrkrDump](https://github.com/crskycode/KrkrDump)

    &emsp;&emsp;&emsp;技术支持[crsky](https://github.com/crskycode)   [Dir-A](https://github.com/Dir-A)

    &emsp;&emsp;依赖库

    &emsp;&emsp;&emsp;[Detours](https://github.com/microsoft/Detours)

    &emsp;&emsp;使用方法

    &emsp;&emsp;&emsp;将`NVLKrkrDumpLoader.exe`与`NVLKrkrDump.dll`置于游戏目录下, 将游戏exe拖到`NVLKrkrDumpLoader.exe`运行即可, `游戏路径/Extract`为导出资源, `NVLKrkrDump.log`为运行日志, `FullPath.lst`为资源全路径列表, `RelativePath.lst`为资源相对路径列表,`AutoPath.lst`为游戏自动路径列表,可搭配hash算法进行碰撞还原

    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;MSVC2022 x86

    &emsp;NVLKR2 Hash Decoder (爆破hash文件名)

    &emsp;&emsp;使用方法

    &emsp;&emsp;&emsp;1."选择目标文件夹" -> 你要还原的资源文件名路径

    &emsp;&emsp;&emsp;2."加载自动路径" -> NVLKrkrDump出来的AutoPath.lst (UTF-8)

    &emsp;&emsp;&emsp;3."加载Dump的文件名还原" -> NVLKrkrDump出来的RelativePath.lst (UTF-8)

    &emsp;&emsp;&emsp;4."使用本地路径还原" -> 选择本地路径用于遍历还原(比如相同厂商的游戏)

    &emsp;&emsp;&emsp;5."使用本地路径还原(AutoPath)" -> 选择本地路径用于遍历还原(自动添加AutoPath路径) 
    (比如使用NVLKrkrDump的Extract文件夹还原)

    &emsp;&emsp;&emsp;6.左侧为字符串生成器  自己找规律生成爆破

    &emsp;&emsp;注意

    &emsp;&emsp;&emsp;1.该Hash算法碰撞率极高  不建议一次性加载太多AutoPath

    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

    &emsp;状态说明

    &emsp;&emsp;1.该引擎官方已弃用, 转为NVLUnity

 * NVLUnity (加密资源 VM文本)

    &emsp;NVLUnityDecryptor (Ver2.0) (静态解密)
   
    &emsp;&emsp;用于解密.nvldata封包    解密完毕请使用[AssetStudio](https://github.com/Perfare/AssetStudio)解包
   
    &emsp;&emsp;游戏测试
    
    &emsp;&emsp;&emsp;《梦末》
    
    &emsp;&emsp;&emsp;《昙花》
    
    &emsp;&emsp;&emsp;《小白兔电商》
    
    &emsp;&emsp;&emsp;《雪中花》
    
    &emsp;&emsp;&emsp;《女装少年短发妹》
    
    &emsp;&emsp;&emsp;《流浪小猫单身狗》
    
    &emsp;&emsp;&emsp;《重启》
    
    &emsp;&emsp;&emsp;《茸雪》
    
    &emsp;&emsp;&emsp;《山茶列车》
    
    &emsp;&emsp;&emsp;《青羽》
    
    &emsp;&emsp;&emsp;《死亡直播间》

    &emsp;&emsp;&emsp;《贝果爱情故事》

    &emsp;&emsp;&emsp;《写真偶像》

    &emsp;&emsp;&emsp;《梦见雪花》

    &emsp;&emsp;&emsp;《泡芙爱情故事》
    
    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

    &emsp;NVLUnityScriptDumper (动态解析脚本)

    &emsp;&emsp;将bytecode脚本还原为AST JSON格式

    &emsp;&emsp;游戏测试
    
    &emsp;&emsp;&emsp;《梦末》

    &emsp;&emsp;&emsp;《昙花》

    &emsp;&emsp;&emsp;《小白兔电商》

    &emsp;&emsp;&emsp;《雪中花》

    &emsp;&emsp;&emsp;《重启》

    &emsp;&emsp;&emsp;《茸雪》

    &emsp;&emsp;&emsp;《山茶列车》

    &emsp;&emsp;使用方法

    &emsp;&emsp;&emsp; 保证`Loader.exe`与`ScriptDumper.dll`与`DumperGUI.dll`在同一路径下, 将游戏exe拖到`Loader.exe`运行即可, 打开debugview观察log输出, 脚本拖拽到指定位置即可解出, 使用vscode去转义格式化json即可

    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;MSVC2022 x86

    &emsp;状态说明

    &emsp;&emsp;1.NVL目前主要使用该引擎

 * NVLWebCloud (加密资源 明文文本)

    &emsp;NVLWeb (静态提取)

    &emsp;&emsp;用于解密修改过的asar封包 图像AES加密
   
    &emsp;&emsp;游戏测试
    
    &emsp;&emsp;&emsp;《我和她的世界末日》
    
    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

    &emsp;状态说明

    &emsp;&emsp;1.官方已弃用 转为NVLUnity

#### 2.Strrationalism/弦语蝶梦

* Snowing (加密资源 明文文本)

    &emsp;SnowingExtract  (静态提取)

    &emsp;&emsp;静态解密游戏加密资源
    
    &emsp;&emsp;游戏测试
    
    &emsp;&emsp;&emsp;《空梦》
    
    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

    &emsp;状态说明

    &emsp;&emsp;1.游戏质量垃圾, 代码不再更新或重构

    &emsp;&emsp;2.官方只做了一作就弃用

#### 3.蓝天使/BlueAngel

* 魔改KrkrZ V1 (定制加密+VMProtect 3.x) (加密资源 明文文本) (静态提取)

    &emsp;提取魔改XP3封包

    &emsp;游戏测试

    &emsp;&emsp;《亿万年的星光》 Steam
    
    &emsp;依赖库
    
    &emsp;&emsp;NuGet
    
    &emsp;&emsp;&emsp;K4os.Compression.LZ4
    
    &emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

* 魔改Krkr2 V1 (少量修改封包+Packman)

    &emsp;TheCardinalMemoryNotch 适配《绯色的记忆之痕》 V2.01

    &emsp;&emsp;动态提取壳VFS资源(ProtectorFileDumper)

    &emsp;&emsp;静态解包(SPKExtractor)

    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;MSVC2022 x86

    &emsp;&emsp;&emsp;.Net 6.x


* 状态说明
  
    &emsp;1.《亿万年的星光》不打算继续维护(游戏质量一般)

    &emsp;2.《刻痕0》系列没人放流, 有放流再看看

#### 4.Fontainebleau/枫丹白露

* 自研引擎加密coco2dx-V1 (加密资源 明文文本)

    &emsp;MeetInParisDumper (动态提取)

    &emsp;&emsp;提取《花都之恋》CG资源 (本人无最新版资源  仅适配Steam 2022.5.1版本)

    &emsp;&emsp;使用方法

    &emsp;&emsp;&emsp;在游戏运行时, 使用DLL注入器注入到目标游戏进程, 即可提取所有CG资源

    &emsp;&emsp;&emsp;使用`TexturePacker`转换`.pvr`资源为`.png`

    &emsp;&emsp;编译环境 
    
    &emsp;&emsp;&emsp;MSVC2022 x86

* 状态说明
  
    &emsp;1.官方已放弃自研 改为Unity

#### 5.ZixSolution(国G程序收费外包商)

* ZedraxloRenpy加密插件V1.0  (Renpy 7.x --- Python2.7) 魔改`.rpa` `.rpyc`封包  (静态提取)

    解密编译后的`.pyc`文件, 位于`游戏目录/renpy`

    &emsp;使用方法

    &emsp;&emsp;解密后自行使用[python-uncompyle6](https://github.com/rocky/python-uncompyle6) 反编译`.pyc`

    &emsp;&emsp;阅读反编译后的python代码修改或编写程序解包`.rpa` `.rpyc`资源

    &emsp;游戏测试

    &emsp;&emsp;《时间碎片 奇迹》  (Renpy 7.x --- Python2.7)

    &emsp;依赖库
    
    &emsp;&emsp;NuGet
    
    &emsp;&emsp;&emsp;Razorvine.Pickle
    
    &emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

    &emsp;注意

    &emsp;&emsp;官方已全面弃用Renpy7 转为Renpy8版本 代码仅做备份保留

* ZedraxloRenpy加密插件V1.1  (Renpy 8.x --- Python3.9) 魔改`.rpa` 封包  (静态提取)

    解密编译后的`.pye`文件, 位于`游戏目录/renpy`

    &emsp;使用方法

    &emsp;&emsp;(uncompyle6暂时不支持Python 3.9反编译)

    &emsp;游戏测试 (未测试:手上没有这个游戏)

    &emsp;&emsp;《山的桃源乡 海的乌托邦》

    &emsp;&emsp;《王牌社团》 (未测试)

    &emsp;&emsp;《忆夏之铃》

    &emsp;&emsp;《夏空的蒲公英》

    &emsp;&emsp;《时间碎片 奇迹》 (未测试)

    &emsp;&emsp;《东73 洋红色童话》 (未测试)

    &emsp;&emsp;《百曲》 (未测试)

    &emsp;&emsp;《Blood Code》 (未测试)

    &emsp;依赖库

    &emsp;&emsp;NuGet

    &emsp;&emsp;&emsp;Razorvine.Pickle

    &emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

* 状态说明
  
    &emsp;1.官方已不做Gal外包

#### 6.iFAction (国G程序收费框架商)

* 自研引擎封包V1 (静态提取)

    &emsp;解包iFCon文件

    &emsp;游戏测试

    &emsp;&emsp;《荧火微光》

    &emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

* 状态说明
  
    &emsp;1.可能不再会跟进或重构

    &emsp;&emsp;原因

    &emsp;&emsp;&emsp;1.这个引擎做RPG为主

    &emsp;&emsp;&emsp;2.Galgame部分游戏少且垃圾

#### 7.AsicxArt

* Unity+代码混淆+WxSQLite AES128加密数据库 V1 (加密资源 明文文本) (静态提取)

    &emsp;提取数据库游戏资源

    &emsp;游戏测试

    &emsp;&emsp;《茸茸便利店》

    &emsp;&emsp;《吸血鬼旋律》

    &emsp;&emsp;《吸血鬼旋律 2》

    &emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

    &emsp;注意事项
    
    &emsp;&emsp;如需查看文本或其他资源  可以使用SQLiteStudio等工具浏览  加密选项选择WxSQLite3 AES128

* 状态说明
  
    &emsp;1.游戏质量较高, 出新作会第一时间跟进


#### 8.心愿游戏

* 《十二刻度的月计时》  激活码KeyGen

    &emsp;编译环境 
    
    &emsp;&emsp;&emsp;.Net 6.x

* 《蔚蓝月下的回忆~SAPPHIRE MOON-FOREVER MEMORIES》   解包代码  (Unity自带的AssetBundle加密)

    &emsp;可以使用[CNStudio](https://github.com/RazTools/Studio)提取 

    &emsp;游戏Key : 41394A3542384D4A50554D3539464B57

#### 9.SoraPlayer

* 修改了Sign的Krkr2封包  (未加密)

    &emsp;游戏测试

    &emsp;&emsp;《夏花的轨迹 That Summer Of Eternal Eden》

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 10.UniversalXP3DecFilter

* 通用XP3加密接口 XP3ArchiveExtractionFilter

    &emsp;游戏测试

    &emsp;&emsp;注:部分游戏使用molebox打包 请先使用demoleition解包

    &emsp;&emsp;《彼岸花葬》

    &emsp;&emsp;《翡翠月》

    &emsp;&emsp;《雪之本境》 光盘版(2010)

    &emsp;&emsp;《雪之本境解境篇》 光盘版

    &emsp;&emsp;《雪之本境EX》 光盘版

    &emsp;&emsp;《雾之本境》 光盘版

    &emsp;&emsp;《雨港基隆》 Steam

    &emsp;&emsp;《鸑鷟 镜花水月》

    &emsp;&emsp;《鸑鷟 橘子传》

    &emsp;&emsp;《叶之离别:若叶归尘》

    &emsp;&emsp;《雨夜》

    &emsp;&emsp;《吉祥铃》

    &emsp;&emsp;《水滴里的夏天》

    &emsp;&emsp;《宛若朝阳》

    &emsp;&emsp;《遗忘花园》 光盘版

    &emsp;&emsp;《紫罗兰-里: 水中倒影》

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 11.Irregulars

* Irregulars Engine

    &emsp;游戏测试

    &emsp;&emsp;《MOBIUS BAND*》

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 12.Visual Novel Maker

* XorFilter

    &emsp;游戏测试

    &emsp;&emsp;《执谕者：坠月之兆》

    &emsp;&emsp;《爱与命的彼端》

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

    &emsp;注意

    &emsp;1. 不是所有资源都进行了加密, 资源是否加密需要自行判断

#### 13.哥布林软件

* Game Creator

    &emsp;游戏测试

    &emsp;&emsp;《令和罕见物语》

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 14.橙汁工作室

*  Lover (情人节:不见不散)

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 15.SeparateHearts

*   SeparateHearts Engine(Hac解包/Tex解码/Hgp解码)

    &emsp;游戏测试

    &emsp;&emsp;《夏梦夜话》

    &emsp;&emsp;《红楼梦》

    &emsp;&emsp;《红楼梦: 林黛玉与北静王》

    &emsp;&emsp;《楼兰: 轮回之轨迹》

    &emsp;依赖库

    &emsp;&emsp;Nuget

    &emsp;&emsp;&emsp;ICSharpCode.SharpZipLib

    &emsp;&emsp;&emsp;LZMA-SDK

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 16.NekoNovel

*   NekoNovel Package

    &emsp;游戏测试

    &emsp;&emsp;《Lucy -The Eternity She Wished For-》

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 17.Ourshow Games

*   AGP封包

    &emsp;游戏测试

    &emsp;&emsp;《李雷和韩梅梅:与你同在》

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 995.Chatte Noire

* Nie no Hakoniwa(贄の匣庭)

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 996.LightVN

* LightVN Engine

    &emsp;游戏测试

    &emsp;&emsp;《U-ena 空焰火少女》

    &emsp;&emsp;《プトリカ 1st.cut》

    &emsp;编译环境

    &emsp;&emsp;.Net 7.x

#### 997.SyawaseWorks (官中发行商)

* HamidashiCreative (Cracker/Dumper/Extractor)

    &emsp;游戏测试

    &emsp;&emsp;《ハミダシクリエイティブ》 Chs Release

    &emsp;依赖库

    &emsp;&emsp;[Detours](https://github.com/microsoft/Detours)

    &emsp;编译环境 
    
    &emsp;&emsp;MSVC2022 x86 (破解/Dump)

    &emsp;&emsp;.Net 7.x (静态解包)

* HappyLiveShowUp (Cracker)

    &emsp;游戏测试

    &emsp;&emsp;《ハッピーライヴ ショウアップ！》 Chs Release

    &emsp;依赖库

    &emsp;&emsp;[Detours](https://github.com/microsoft/Detours)

    &emsp;编译环境 
    
    &emsp;&emsp;MSVC2022 x86

#### 998.HikariField (官中发行商)

* HFUnityV1 (HFUnityV1) (Extractor)

    &emsp;游戏测试

    &emsp;&emsp;《アオナツライン》 Chs-Cht Release

    &emsp;&emsp;《Making Lovers FHD》 Chs-ChtRelease

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

* FutureRadio (CatSystem2 Unity) (Extractor)

    &emsp;游戏测试

    &emsp;&emsp;《未来ラジオと人工鳩》 Chs-Cht-Jpn-Eng Release

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

* NekoNyan (NekoNyan Unity) (Extractor)

    &emsp;游戏测试

    &emsp;&emsp;《蒼の彼方のフォーリズム PE/EXTRA1/EXTRA2》 Chs-Cht-Jpn-Eng Release

    &emsp;&emsp;《金色ラブリッチェ》 Chs-Cht-Jpn-Eng Release

    &emsp;&emsp;《Clover Day's Plus》 Chs-Cht-Jpn-Eng Release

    &emsp;&emsp;《恋と選挙とチョコレート》 Chs-Cht-Jpn-Eng Release

    &emsp;编译环境

    &emsp;&emsp;.Net 6.x

#### 999.Others

