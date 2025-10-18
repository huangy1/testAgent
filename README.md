. : 无法加载文件 C:\Users\16272\Documents\WindowsPowerShell\profile.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参
阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 3
+ . 'C:\Users\16272\Documents\WindowsPowerShell\profile.ps1'
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
#第一次设置conda报错（win powershell中）


test prompt:list and read file, base on your knowledge, tell me what lang each file use.

file:///C:/path/to/image.jpg #background 图片设置路径

form . import tools #__init__.py 需要

已追踪文件加入ignore,先
```bash
git rm --cached .env  
```
deepseek不支持openai的response API，所以用不了OpenAIResponsesModel