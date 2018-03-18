class Settings(object):

    def __init__(self):

        # 屏幕设置
        self. screen_width = 1000
        self.screen_height = 560
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 0.8

        # 子弹设置
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3