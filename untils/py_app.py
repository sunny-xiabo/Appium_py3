"""
 # coding: utf-8
 # @Author：xiabo
 # @File : py_app.py
 # @Date ：2021/6/17 上午10:57
 
"""

'''
appium的一个简单封装
'''

class driver_encap(object):

    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, method, path):
        if method == 'id':
            se = self.driver.find_elements_by_id(path)
        elif method == 'xpath':
            se = self.driver.find_elements_by_xpath(path)
        elif method == 'css':
            se = self.driver.find_elements_by_css_selector(path)
        elif method == 'and':
            #这里在使用的时候比如使用text，那么这里的path为text('123')
            se = self.driver.find_elements_by_android_uiautomator('new Uiselector().{}'.format(path))
        elif method == 'class':
            se = self.driver.find_elements_by_class_name(path)
        elif method == 'name':
            se = self.driver.find_elements_by_name(path)
        elif method == 'acces':
            se = self.driver.find_elements_by_accessibility_id(path)
        elif method == 'text':
            se = self.driver.find_elements_by_link_text(path)
        elif method == 'partial':
            se = self.driver.find_elements_by_partial_link_text(path)
        elif method == 'tag':
            se = self.driver.find_elements_by_tag_name(path)
        else:
            raise NameError('no element,please send tag,xpath,text,id,css,name,tag')
        return se


    def find_elemens(self, method, path):
        if method == 'id':
            se = self.driver.find_elements_by_id(path)
        elif method == 'xpath':
            se = self.driver.find_elements_by_xpath(path)
        elif method == 'css':
            se = self.driver.find_elements_by_css_selector(path)
        elif method == 'and':
            # 这里在使用的时候比如使用text，那么这里的path为text('123')
            se = self.driver.find_elements_by_android_uiautomator(
                'new Uiselector().%s' % path)
        elif method == 'class':
            se = self.driver.find_elements_by_class_name(path)
        elif method == 'name':
            se = self.driver.find_elements_by_name(path)
        elif method == 'acces':
            se = self.driver.find_elements_by_accessibility_id(path)
        elif method == 'text':
            se = self.driver.find_elements_by_link_text(path)
        elif method == 'partial':
            se = self.driver.find_elements_by_partial_link_text(path)
        elif method == 'tag':
            se = self.driver.find_elements_by_tag_name(path)
        else:
            raise NameError('no element,please send tag,xpath,text,id,css,name,tag')
        return se


    def ins(self, path):#安装APP
        self.driver.install_app(path)

    def rem(self, packagename):#卸载app
        self.driver.remove_app(packagename)

    def rem_ios(self, bundleId):#ios
        self.driver.remove_app(bundleId)

    def close(self):#关闭APP
        self.driver.close_app()

    def reset(self):#重置APP
        self.driver.reset()

    def hide_keyb(self):#隐藏键盘
        self.driver.hide_keyboard()

    def send_keyevent(self, event):#只有安卓有
        self.driver.keyevent(event=event)

    def send_press_keycode(self, keycode):#安卓有
        self.driver.press_keycode(keycode=keycode)

    def long_press_keycode(self,keycode):#长按发送
        self.driver.long_press_keycode(keycode)

    def current_activity(self):#当前的活动
        activity = self.driver.current_activity()
        return activity

    def wait_activity(self, activity, times):#等待的活动
        self.driver.wait_activity(activity, time=times, interval=1)


    def run_back(self, second):
        self.driver.background_app(seconds=second)

    def is_app_installed(self, package):#ios需要buildid
        self.driver.is_app_installed(package)


    def launch_app(self):#启动APP
        self.driver.launch_app()

    def start_acti(self, app_package, app_activity):
        self.driver.start_sctivity(app_package, app_activity)

    def ios_lock(self, locktime):
        self.driver.lock(locktime)

    def shake_phone(self):#摇手机
        self.driver.shake()

    def open_notif(self):#安卓api 18以上
        self.driver.open_notifications()

    def renturn_network(self):#返回网络
        network_type = self.driver.network_connection
        return network_type

    def set_network_type(self, type):#网络类型
        from appium.webdriver.connectiontype import ConnectionType
        if type == 'wifi' or type == 'WIFI' or type == 'w' or type == 'WIFI_ONLY':
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)

        elif type == 'data' or type == 'DATA' or type == 'd' or type == 'DATA_ONLY':
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)

        elif type == 'all' or type == 'ALL' or type == 'a' or type == 'ALL_NETWORK_ON':
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

        elif type == 'no' or type == 'NO' or type == 'n' or type == 'NO_CONNECTION':
            self.driver.set_network_connection(ConnectionType.NO_CONNECTION)

        elif type == 'air' or type == 'AIRPLANE_MODE' or type == 'ar' or type == 'fly':
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)

        else:
            raise NameError('please check wifi,data,all,no,fly')


    def run_typewriting(self):#输入法
        typewriting = self.driver.available_ime_engines
        return typewriting

    def typewrite_active(self):
        check = self.driver.is_ime_activer
        return check

    def active_typewite(self, engine):
        self.driver.activate_ime_engine(engine)

    def close_typewrite(self):
        self.driver.deactivate_ime_engine()

    def open_location(self): #打开定位
        self.driver.togoogle_location_services()

    def set_position(self, latitude, longitude, altitude): #设置纬度，经度，海拔
        self.driver.set_location(latitude, longitude, altitude)

    def get_size(self):#获取尺寸
        size = self.driver.se.size
        return size

    def text(self):
        text = self.driver.text
        return text

    def is_dis(self):#是否显示
        dis = self.driver.se.is_displayed()
        return dis

    def screet(self, filename):
        self.driver.get_screenshot_as_base64(filename)

    def clos(self):
        self.driver.close()

    def kill(self):
        self.driver.quit()

    def screet_wind(self):
        me = self.driver.get_screenshot_as_file()
        return me #返回  true,flase

    def get_wiow_size(self):#获取窗口大小
        return self.driver.get_window_size()

    def enlarge(self, element): #放大
        self.driver.zoom(element)

    def narrow(self, element): #缩小
        self.driver.pinch(element)

    def fast_flide(self, s_x, s_y, e_x, e_y):#从一点到另一个点
        self.driver.flick(s_x, s_y, e_x, e_y)

    def flide(self, s_x, s_y, e_x, e_y, duration=None):
        self.driver.swipe(s_x, s_y, e_x, e_y)

    def touch(self,x, y, duration=None):
        self.driver.tap([(x, y)], 500)

    def scroll(self, x, y):#滚动元素
        self.driver.scroll(x, y)

    def drag_and_drop(self, e1, e2):#移动元素
        self.driver.drag_and_drop(e1, e2)

    def contexts_is(self):#可用
        self.driver.contexts()

    def push(self, data, path):
        self.driver.push_file(data, path)

    def pull(self, path):
        self.driver.pull_file(path)

    def wait(self, seconde):
        self.driver.wait_activity(seconde)

    def send_key(self, pas):
        self.driver.send_keys(pas)