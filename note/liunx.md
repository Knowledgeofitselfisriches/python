#  操作系统 --> /boot的内核文件 --> init --> 运行级别
   linux 特点
    免费，开源，安全，高效，稳定，高并发
   虚拟机网络链接
    1. 桥接 与other 系统通信，容易冲突
    2. NAT  网路地址转换
    3. 主机 不能访问外网
    设置共享文件夹 /mnt/hghn/

   linux 一切皆是文件
     

   Linux系统有7个运行级别(runlevel)：

    * 运行级别0：系统停机状态，系统默认运行级别不能设为0，否则不能正常启动
    * 运行级别1：单用户工作状态，root权限，用于系统维护，禁止远程登陆
    * 运行级别2：多用户状态(没有NFS)
    * 运行级别3：完全的多用户状态(有NFS)，登陆后进入控制台命令行模式
    * 运行级别4：系统未使用，保留
    * 运行级别5：X11控制台，登陆后进入图形GUI模式
    * 运行级别6：系统正常关闭并重启，默认运行级别不能设为6，否则不能正常启动
## apt命令(ubuntu 16版本以上) 早期版本apt-get
   apt ubuntu Advanced Packaging Tool下的安装包管理工具
   sudo 获取root权限
	1.安装软件
	  sudo apt install softwarename
	2.卸载软件
	  sudo apt remove  softwarename  
	3.更新可用软件包列表
	  sudo apt update
	4.更新已安装的包
  	  sudo apt upgrade   
## deb 格式 （Debian Linux）
	sudo dpkg -i <package.dep> 
	cd dir  进入目录
	cd ..   返回上一级
	ls -l   列出当前目录下的文件
	sudo apt install libindicator7
	sudo apt -f install 修复依赖
###安装sougou 
	1、先安装fcitx平台 ，语言支持选择fictx
    sudo add-apt-repository ppa:fcitx-team/nightly // 添加FCITX仓库.

    sudo apt-get update // 更新仓库.

    sudo apt-get install fcitx // 安装fcitx输入法框架.
    2、安装搜狗
    sudo apt install  sougou.deb
	sudo apt -f install 修复依赖
## linux 的进化
    bcpl语言--b语言--c语言--unix--unix version-7 闭源 -->minix --> linux 、
    有关的词汇
	GNU is not Unix GNU计划 ： knerul \shell \application
	GPL GNU通用公共许可证（GNU General Public License，GPL）
	GCC GNU编译器套件（GNU Compiler Collection）c/c++/java/python/go
	POSIX 规范
    组成 硬件 linux内核（系统api,终端命令）--发行版（应用层）
## 文件和目录结构
    linux 没有盘符的概念
	        根目录 /
	        	| 
	           home
	            |
	       user1    user2 
	       		      |
	        Document Desktop Game	
	/ 根目录        
	/ etc 系统配置文件       
	/ home 放置用户主目录
  / usr 用户应用和文件类似 program file
  / root 超级权限主目录
  / media linux 识别光驱，硬盘等挂载在此目录下
  / mnt 用户零食挂载的文件系统的
	/ bin 可执行文件 终端命令
	/ boot 系统内核文件 系统引导文件
	/ dev  系统设备文件cpu disl gpu 光驱等
  / opt 第三方软件安装目录
  / usr/local 这是给另一个主机额外安装软件的安装目录
  一般是编译源代码方式安装的程序
  / var
    存放经常变动的文件，如日志等
	用户尽量不要操作自己文件夹外的文件
## 常用命令
	查看目录
		ls      list         查看当前文件夹下的内容
		pwd     print work directory 查看当前目录
	切换目录
		目录]	change directory 切换目录 
	创建删除 touch rm mkdir
		touch[文件名] 如果不存在创建文件
		mkdir[目录] make directory 如果不存在创建目录
		rmdir[目录] remove directory 删除空目录
		rm -r [目录] 删除目录及目录下所有内容
		rm[文件名] remove file    删除文件
	拷贝和移动
		cp
		mv
	查看文件内容
		cat
		more
		grep
	其它
		echo
		重定向 > ,>>
		管道 |		

	clear  clear  清屏
	
### 格式 command [-options] [parameter]
	command : 命令
	options : 可选的 选项控制命令的执行 
	parameter: 传递给命令的参数
	固定格式
	--help 
	--version
	--context
### 查询命令的信息
    1、command --help 查询命令帮助信息
    2、man command 查询使用command手册	man---manual手册
      手册操作 ：
      		space 显示下一屏
      		enter 下一行
      		b     回滚一屏
      		f     前进一屏
      		q     退出手册
      		/str  搜索str	
### 小技巧
	ctrl shift = ---ctrl  + 放大终端字体
	ctrl - ---缩小终端字体

	自动补全 tab
		如果 输入目标没有歧义 会直接补全
		如果 有歧义，双击tab会列出选项
	↑↓ 选择已输入命令
	不执行命令并另起一行 ctrl c
	清屏 cls
	当前目录 .
	上一级目录 ..
### 命令扩展
	1.linux 文件和目录的特点
		1.长度不能超过256
		2.以.开头的文件为隐藏文件，需要用-a才能显示
		3.当前目录 是.
		4.上一级目录是..
	2.ubuntu 中 文件目录为蓝色 ，文件为白色	
		ls -a  列出所有文件 包含隐藏文件
		ls -l  列出文件的详细信息
		   -h  配合-l以人性化的方式显示文件的大小 将字节转为k/m/g
		total 总计大小  文件夹默认4k   
		drwxr-xr-x | 2 |caowenqi caowenqi    | 4096 |Jun  6 20:53 |test
		-rw-r--r-- | 1 |caowenqi caowenqi    |   0  |Jun  7 08:30 |b.txt
		目录操作方式|该目录下所有目录数量|用户及群组|大小| 日期时间    | 名字
		目录操作方式：第一个字符有 d --> 代表文件夹，- --> 代表普通文件，| --> 代表连接文件，接下来的9个字符，以3个一组，分别代表文件所有者、文件所有者所在用户组、其它用户对文件拥有的权限	。r 只读 w只写 x执行 -没有3种操作中的一种 合写选项 
    r  4
    w  2
    x  1
    s  比x弱
		ls -lha
	3.命令参数中使用通配符
		* 任意个数字符            
			ls g* 以g开头的所有文件
			ls *.txt 找到txt结尾的文件
			ls *3*   找到中间有3的文件
		？ 任意一个字符    
		    ls 1?1.txt 找到1开头 中间任意 1结尾.txt的文件    
		[] 匹配字符组中的任意一个
		[abd] 匹配a,b,d中的一个
		[a-f] 匹配a-f中的任意一个	
	4.cd命令
	  cd/cd ~ 切换到当前用户的主目录(/home/users)
	  cd . 
	  cd ..
	  cd -  可以在最近工作目录之间的切换	 
	5. touch 不存在则创建文件
	          存在就修改末次修改时间 
	6. mkdir 如果目录已存在则
	  -p 递归创建目录 mkdir test/python/0607 
	7. rm 文件删除后无法恢复
	   -f 强制删除 忽略不存在文件无需提示 如果不存在文件不加-f 会提示
	   -r 递归删除目录及其下的文件 	
	   rm -rf *  清除所有内容        
	8. 拷贝移动
	   tree  以树状图的方式列出当前文件目录结构 
	   tree [目录] 列出指定目录下的结构
	   tree~ 显示用户目录下的结构
	       -d 只显示目录	  
	   cp 源文件  目标目录   ~/Documents$ cp ./readme.txt ~/Desktop/
           -i 覆盖文件前提示
           -r 复制目录一级其下的所有内容 ，
       mv 源文件/目录 目标文件/目录 
       mv 源目录下的文件名 源目录新文件名  mv readme.txt about.txt   重命名
       	  注意如果新名字已存在则会用原文件内容覆盖它
       cat 文件名 concatenate  查看/创建/合并/追加文件内容
       	 - b  非空行显示行号 nl about.txt = cat -b aount.txt
       	 - n  显示所有行号	
       more 文件名 分屏显示文件内容
       	cat 适合查看内容较少的文件
       	more 适合查看内容很多的文件
       grep 文件名 搜索文本文件内容
         grep str about.txt
          -n 显示匹配及行号
          -v 不显示匹配
            显示不匹配的和行号 -vn
          -i 忽略大小写 
         str 中如果包含space 必须使用双引号  "Hello Python " 
         grep ^f about.txt 搜以f开头的文本
         grep f$ about.txt 搜以f结尾的文本
    9. 其它
       echo str 显示文字
       重定向
       		> 输出  ls -lh > test.txt
       		>>追加  echo str >> test.txt
      -echo str >/>> file 将str 输出(会覆盖)/追加到file 
       ps 显示进程
         -e  显示所有进程   
    10.管道|
       将一个命令的输出作为另一个命令的输入 通过| 连接 左 命令的输出 | 接收输入命令
       常用管道命令 more /grep
## 远程管理
    关机和重启
 	  shutdown -options time   默认1min后关机
 	         - r            重启
 	         - c            取消操作
 	                  now    代表现在 
 	                  20：25 在20.25执行
 	                  +10    10min后执行 
    halt 直接使用 等价于关机
    reboot 重启
    sync 将内存数据写入disk 防止丢失
    logout 退出登录 只有在运行级别3：及多用户情况下               
    网络 install net-tools
   	ifconfig 查看 网卡配置信息 ifconfig | grep inet
   	ping ip 检测与目标地址的链接  
###远程管理工具 secure shell  (ssh) 
     --. 数据传输加密防止泄露
     --. 数据传输压缩提升速度
   1.常见服务端口
     ssh   22
     web   80
     https 443
     FTP   21 
   2.基本格式 ssh [-p port] user@remote
    remote:ip/域名/别名	
    port SSH Server 监听的端口22
    exit 退出当前用户
    ubuntu 默认安装了客户端
    用cat /etc/ssh/sshd_config 命令查看是否安装了ssh服务端
    通过 ps -e | grep ssh 查看服务是否启用
        1309 ?        00:00:00 ssh-agent 客户端
  		4010 ?        00:00:00 sshd 服务端
    登录 	ssh [-p port] user@remote
    按yes
    输入密码
   3.远程拷贝文件 scp                                           
     scp -p port 源文件 user@remote:相对user路径或绝对路径        
    windows作为客户端 cmd命令下 ubuntu文件位置 ： 代表user目录下  目标路径
    从服务器复制文件
    scp -p 22 caowenqi@192.168.157.130:Pictures/ngnlzero.jpg  ./demo
    发送文件到服务器
    scp -p 22 miku.jpg caowenqi@192.168.157.130:Pictures/
       -r  发送/接收 文件夹
       -P（大写） + 端口号指定 SSH服务器端口号   
   4.有关ssh配置信息都保存在用户家目录的.ssh下 win 存于 user下
     known_hosts 保存有相应的文件信息
     免密登录
     配置公钥
       执行ssh-keygen 生成ssh钥匙
     上传公钥到服务器
       执行ssh-copy-id -p port user@remote,让服务器记住公钥
     本地使用私钥对数据进行加解密 id_rsa
     服务器使用公钥对数据进行加解密id_rsa_pub
     非对称加密算法
     使用公钥加密的数据，需使用私钥解密
     使用私钥加密的数据，需使用公钥解密

     配置别名
     在.ssh/config/追加
     touch config
     gedit config 打开文件
     
     Host m
     	HostName ip
     	User    username
     	Port    22  
              
## 用户 权限 组
    增加/减少权限 chmod +/- r/w/x 文件名/目录
    x 表示可访问权限
    1. root 超级用户
      substitule user 表示另一个用户的身份
      sudo 用其它身份执行，预设root
      输入密码 有5min有效期  
    2. groupadd +组名     添加组
      sudo groupadd dev
      groupdel +组名     删除组
      sudo groupdel dev
      cat /etc/group      确认组信息
      chgrp -R 组名 文件名/目录 修改所在组
      sudo chgrp -R dev demo
    3.  创建新用户/设置密码/删除用户
      useradd -m 自动建立用户家目录
              -g 指定用户所在组，否则建立同名的组
              -d  directory username 指定目录建立用户家目录

        sudo useradd -m -g dev liuwentao         
      passwd username 设置用户名  
        sudo passwd liuwentao  
      userdel  username 保留家目录删除
      userdel -r username 目录和家目录一起删除

      cat /etc/passwd | grep username
      切换用户 su username
      exit 返回原用户
### 查看用户信息
     id username 
    id 查看当前用户
      uid 用户id
      gid 组id
    cat -n /etc/passwd | grep username
    42 lwt:x:1001:1001::/home/lwt:/bin/sh
    username:passwd:uid:gid:usernameall:home目录：登录后使用的shell ubuntu默认dash
      adm:x:4:syslog,caowenqi
    cat -n /etc/group | grep groupname  
    18  cdrom:x:24:caowenqi  管理员
    21  sudo:x:27:caowenqi   root执行
    23  dip:x:30:caowenqi    
    35  plugdev:x:46:caowenqi
    55  lpadmin:x:116:caowenqi
    65  caowenqi:x:1000:
    66  sambashare:x:126:caowenqi
    who    查看当前所有登录的用户列表
    caowenqi :0 2018-06-07 22:58 (:0)
    ：0代表当前登录的 开机时间
    whoami 查看当前登录用户的账户名

### 主组和附加组
    主组 通常在新建用户的-g指定，及gid对应
    附加组 /etc/group 中的用户列表，用于指定用户的权限
    usermod 设置用户的主组/附加组/登录shell
    usermod -G group username 修改附加组
      sudo usermod -G sudo lwt
    usermod -g group username 修改主组
    usermod -s /bin/bash username  
     因为windows下dash不好用，改为bash

### which 
    /etc/passwd 是用于保存用户信息的文件
    /usr/bin/passwd 是用于修改用户密码的程序
    which 命令可以查看执行命令所在位置
    which ls       /bin/ls
    which useradd  /usr/sbin/useradd

    /bin (binary) 是二进制文件目录 具体应用
    /sbin(system binary)系统管理员的二进制代码目录，主要用于系统管理
    /usr/bin 安装的一些软件
    /usr/sbin root的一些管理程序
    which 无法查看cd
#### 切换目录
    01. su username 切换用户 su lwt pwd cd
        su-username 切换用户并切换目录
    02. exit 退出当前登录
#### 修改文件权限
    <权限范围>+<权限设置>：开启权限范围的文件或目录的该选项权限设置；
    <权限范围>-<权限设置>：关闭权限范围的文件或目录的该选项权限设置；
    <权限范围>=<权限设置>：指定权限范围的文件或目录的该选项权限设置；

    chown 修改拥有着权限 chown username file/dir
      chown user:market f01　　//把文件f01给uesr，添加到market组
      ll -d f1  查看目录f1的属性
    chgrp 修改组 chgrp -R groupname file/dir
    chmod 修改权限 chmod -R 755 file/dir
      own    group    other
    r  w  x r  w  x  r  w  x
    4  2  1 4  2  1  4  2  1
    rwx = 7
    r-x = 1
    --- = 0 
      chmod u+x,g+w f01　　//为文件f01设置自己可以执行，组员可以写入的权限
      chmod u=rwx,g=rw,o=r f01
      chmod 764 f01
      chmod a+x f01　　//对文件f01的u,g,o都设置可执行属性
## 查询系统信息
     时间和日期
       date
       cal -y 查看一年的日历
     磁盘和目录空间
       df -h 显示空闲空间 disk free
       du -h[dir] 显示目录下的文件大小 disk usage 
     进程信息
     ps 
       a :显示终端的所有进程（包括其它用户）
       u :显示进程的详细信息
       x :显示没有控制的终端的进程（所有正在执行的程序）
     top 动态显示正在运行的并排序的程序 退出q 监视异常
     kill[-9] processId   [-9]表示强行终止
### 查找文件
    find [路径] -name "*.py"
    linux 中的文件名和数据是分离的
    软硬链接 
      ln 硬链接   
      ln   -s 软链接  
      ln -s 绝对路径 链接名字 使用相对链接在移动后会出错
       |         | —— 文件名
          文件数据    
       |         | —— 硬链接（相当于别名）
       |         |
         文件数据   ——文件名 —— 软链接路径 —— 软连接名
       |         |
       删除文件后只是删除了文件名，软连接不可用了
       硬链接还有用 ，只有当没有链接指向文件数据时，文件才不可用

#### 计算机中单位
    1 B  = 8bit
    1 KB = 1024B 2^10
    1 MB = 1024KB
    1 GB = 1024MB
    1 TB = 1024GB
    1 PB = 1024TB
    1 EB = 1024PB
    1 ZB = 1024EB
    1 YB = 1024ZB
### 打包/解包
  win 使用 rar
  mac 使用 zip
  linux    tar.gz
  tar 负责打包文件但不压缩
   tar -cvf name.tar file/dir
   tar -xvf name.tar 
  gzip 负责压缩文件和解压缩
   tar -zcvf name.tar.gz file/dir 
   tar -zxvf name.tar.gz
   解压到指定路径
   tar -cvf name.tar -C 目标路径
  bzip2 负责压缩文件和解压缩 
   tar -jcvf name.tar.bz2 file/dir 
   tar -jxvf name.tar.bz2 [-C dir] 
### vi/vim的三种模式
   1. 正常模式
      可以使用快捷键
      命令行下 vim file 进入
      也可按esc进入
   2. 插入模式/编辑模式
      按i 可输入内容

   3. 命令行模式
      
        ：wq保存并退出
        ： q 退出
        ：q！不保存强制退出 
       可以提供特殊的命令
 	  yy 复制当前行 yy4 复制当前行4次
    p 粘贴
    ddN 删除几行  
    ：set nu/nonu 设置行号/取消行号
    G 文末 gg文首
    u 取消
    切换 行 输入行号 shift g 
##     

 
