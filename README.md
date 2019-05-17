## sqlmap-ui
sqlmap GUI, using PyGObject(gtk+3)  
use sqlmap-wx, if you want to run it in win  

congratulations about sqlmap ported to python3!  
from sqlmap's FAQ:  
"Both Python 2 and 3 are supported from May of 2019"  

#### SCREENSHORT
![screenshot](https://github.com/needle-wang/sqlmap-ui/blob/master/screenshots/sqlmap-ui1.png)

#### INSTALLATION
1. **REQUIRED**  
  - python3.5+, GTK+3.20  
  - pygobject: `pip3 install PyGObject` or `apt-get install python3-gi`  
  - requests: `pip3 install requests`  
  - latest [sqlmap](https://github.com/sqlmapproject/sqlmap): `git clone` it.  
2. **GET**
  - `git clone https://github.com/needle-wang/sqlmap-ui.git`
3. **RUN**  
  - `./sqlmap_gtk.py`

#### TODO
- ~~UI重新排版~~
- ~~分离并完善tooltip等提示信息~~
- ~~细节优化(margin, padding啥的)~~
- ~~打从加了filechooserbutton起, 启动就慢了一倍:  
   根据line_profiler输出: gtk.FileChooserButton()有性能问题!~~
- ~~重构~~
- ~~添加session功能(v0.2.2)~~
- ~~重构成MVC模式(结构重构改动很大, v0.3)~~
- ~~将管道流集成到UI里(无法实现, 改用pty实现成功)~~
- ~~添加API区(实现sqlmapapi client)~~
- ~~修复: 修改filechooserbutton(常有什么network path超时警告, 启动加快),  
  输出滚动不准确, file entry补全, G_VALUE_HOLDS_INT警告~~
- 继续重构, 优化

#### ABOUT
1. V0.3.4  
   2019-05-17 21:35  
   作者: needle wang ( needlewang2011@gmail.com )  
2. 使用PyGObject(Gtk+3: python3-gi)重写sqm.py  
3. 感谢[sqm](https://github.com/kxcode/gui-for-sqlmap)带来的灵感, 其作者: [KINGX](https://github.com/kxcode) (sqm UI 使用的是python2 + tkinter)  

#### REFERENCE
1. Gtk+3教程: https://python-gtk-3-tutorial.readthedocs.io/en/latest/  
2. Gtk+3 API: https://lazka.github.io/pgi-docs/Gtk-3.0/  
