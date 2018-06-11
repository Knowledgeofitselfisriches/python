
#git & github 
	版本控制
		意义：
	       个人开发迭代：方便修改代码
	       团队处理： 处理修改冲突
	    分类：
	    	集中式 svn 有单点故障问题
	    	分布式 git  

	工具功能
		协同修改
		数据备份
		版本管理
			svn 增量管理
			git 文件快照
		权限控制
			权限控制
			git审核开发团队外人提交的代码
		历史纪录
		分支管理       
## git 简介
	  git的优势：
	  	1. 大部分操作本地完成无需联网
	  	2. 完整性保证 hash 操作
	  	3. 尽可能添加数据而不是添加和修改数据
	  	4. 分支操作流畅快捷
	  	5. 兼容linux命令	
	  工作区 暂存区  本地库
	  代码托管中心：维护远程库

	  团队内操作
	   	  本地库 <--- clone github	
		  本地库 push--->   github
		  本地库	<---- pull  github
		  
	  团队外贡献者
	  	  fork 远程库 复制一个远程库
	  	  本地库 <--- clone github 	
	  	  本地库 push--->   github
		  本地库	 pull request -->审核-->merge合并-->  github
### Git命令行操作
	1. 本地库初始化
	   git init 创建.git	  
	2. 设置签名
	   用户名： 
	   Email: 
	   作用： 区分不同的开发人员
	   命令 ： 
	    	项目级别：本地库级别   
	    		git config user.name caowenqi
	    		git config user.email learningandliving@163.com 信息保存在.git/config
	    	系统用户：操作系统级别 
	    		git config --global 
	    		git config --global
	    		信息保存于用户目录下.gitconfig
	    	优先级别  
	    	    项目优先
	    	
	    	    
	3.  查看状态操作和添加提交
	    * 状态查看 工作区和暂存区状态
			git status  
			在工作区使用vim file 创建编辑 后按esc退出
			编辑状态并输入
			：set nu 设置行号
			：wq再完成创建
		* 添加文件  从本地区填入暂存区
			git add file 将文件填入暂存区
		* 删除暂存区文件	
			git rm --cached file 将文件从缓存区删除
		* 提交操作
			git commit -m 'str' file/dir 提交到远程库
			
			当修改完文件后
			可使用git add file 填入缓存区
			git commit -m 'str' file/dir
	4. 历史版本操作
		1 . 查看历史信息
			git log 完整显示log信息
			git log --pretty=oneline 以整齐的格式显示log信息
				hashstr (HEAD -> master) test log history
				hashstr second commit,modify readme.md
				hashstr	hello git

			git log --oneline
				fefc3a4 (HEAD -> master) test log history
				892eb24 second commit,modify readme.md
				72ac9d6 hello git

			git reflog	
				fefc3a4 (HEAD -> master) HEAD@{0}: commit: test log history
				892eb24 HEAD@{1}: commit: second commit,modify readme.md
				72ac9d6 HEAD@{2}: commit (initial): hello git
        2. 历史操作
		    (HEAD -> master)头指针 显示版本 	HEAD@{N}需移动n步
		    基于索引值搜索版本
			    * git reset --hard [局部index]
			    git reset --hard 892eb24 将指针移到892324版本
			使用^符号：只能后退版本    
		    	git reset --hard HEAD^ 一个表示后退一步，n个表示退n步
		    使用~符号：只能前进版本
		    	git reset --hard HEAD~n
		3. 前进后退
			
			git help reset 查看命令
		4. reset 的三个命令对比
			
			--soft  仅仅在本地库移动指针 
			--mixed 在本地库移动指针 同时重置暂存区
			--hard	在本地库移动指针 同时重置暂存区与本地区  
		5. 删除文件
			rm file
			git add file
			git commit 'str' file

		  前提：删除前，文件存在时的状态提到本地库
		  操作：git reset --hard[指针位置]	

		    * 删除操作已提交到本地库，指针位置指向历史纪录
		    * 删除操作未提交到本地库，指针位置使用HEAD 
		6 .比较修改
			git diff 比较所有文件差异
			git diff file 将工作区与暂存区的文件进行比较 
			git diff[本地库中历史版本][file]将本地文件与本地库中的历史文件比较
        
	5. 分支管理
	   > 同时并行推进多个功能开发，提高开发效率
	   > 各个分支在开发过程中，如果某个分支失败，不会对其它分支有影响
	   ![分支](C:\Users\caowenqi\Pictures)
	   1.分支操作
	   	创建分支
	   		git branch name 
	   	查看分支
	   		git branch -v
	   	切换分支
	   		git checkout [name]		
	   	合并分支
	   		先切换到需要接受合并的分支
	   		git merge [更新的分支name]		
		解决冲突
			1. 编辑文件，删除特殊符号
			2. 修改文件
			3. git add [ file ]
			4. git commit -m 'logging'
			      注意commit不能带文件名
### git 原理
    1. hash算法的特点
    	MD5 SHA1 CRC32
    	* 加密结果长度固定
    	* 输入数据不变，输出结果不变
    	* 输入变化，结果变化很大
    	* 不可逆
    	* git 底层采用SHA-1算法
    	* 可用来验证文件
    				sha-1
    	server.file ----- result
    	client.file ----- result
    	result == result 
    	为True 则为丢失信息
    2. git 管理历史信息 
    	文件快照：
    		没别修改的文件，就通过指针引用

    	* 通过将每个修改的文件进行hash
    	并生成tree保存hash信息
    	* 新建commit 对象 保存tree 信息
    	和上个commit 对象的has自己的hash信息
    	  形成 链表结构	
    	3. 分支管理 
    		实际也是操作指针指向某个具体的版本
    	修改分支只移动了指针，不会影响其它分支
## github
	创建远程库
	 获取地址 https/ssh 地址
	查看远程库地址
	 git remote -v
	 git remote add origin addr
	 origin  addr (fetch) 取回
	 origin  addr (push)  推送

	 git push origin 分支	 