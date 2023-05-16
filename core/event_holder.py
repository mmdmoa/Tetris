from gui.common.names import *


class EventHolder:
    def __init__(self):
        self.event_list: list[pg.Event] = []

        self.pressed_keys = []
        self.released_keys = []
        self.held_keys = []
        self.window_focus = True

        self.wheel = 0
        self.mouse_moved = False
        self.mouse_pos = Vector2(0, 0)
        self.mouse_pressed_keys = [False, False, False]
        self.mouse_released_keys = [False, False, False]
        self.mouse_held_keys = [False, False, False]
        self.mouse_focus = False
        self.should_render_debug = False
        self.activity: Optional[Activity] = None
        self.should_quit = False
        self.determined_fps = 60
        self.final_fps = 0
        self.focus_gain_timer = -100
        self.mouse_focus_gain_timer = -100
        self.clock = pg.time.Clock()
        self.dt = 0

    @property
    def delta_time(self):
        return self.dt
        # delta = 1 / (self.final_fps if self.final_fps!=0 else 60)
        # return delta

    @property
    def mouse_rect(self) -> Rect:
        return Rect(self.mouse_pos.x - 1, self.mouse_pos.y - 1, 2, 2)

    def get_events(self):
        self.event_list.clear()
        self.pressed_keys.clear()
        self.released_keys.clear()
        self.mouse_pressed_keys = [False, False, False]
        self.mouse_released_keys = [False, False, False]

        self.wheel = 0
        self.mouse_moved = False
        self.final_fps = self.clock.get_fps()
        self.dt = self.clock.tick(self.determined_fps) / 1000

        for event in pg.event.get():
            self.event_list.append(event)

            if event.type == MOUSEWHEEL:
                self.wheel = event.y

            if event.type == WINDOWFOCUSLOST:
                self.window_focus = False
            if event.type == WINDOWFOCUSGAINED:
                self.window_focus = True
                self.focus_gain_timer = pg.time.get_ticks() / 1000

            if event.type == WINDOWENTER:
                self.mouse_focus = True
                self.mouse_focus_gain_timer = pg.time.get_ticks() / 1000
            if event.type == WINDOWLEAVE:
                self.mouse_focus = False

            if event.type == WINDOWENTER or MOUSEMOTION:
                self.mouse_pos = Vector2(pg.mouse.get_pos())

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.should_quit = True

            if event.type == MOUSEMOTION:
                self.mouse_moved = True

            if event.type == KEYDOWN:
                self.pressed_keys.append(event.key)
                if event.key not in self.held_keys:
                    self.held_keys.append(event.key)

            if event.type == KEYUP:
                self.released_keys.append(event.key)
                if event.key in self.held_keys:
                    self.held_keys.remove(event.key)

            if event.type == MOUSEBUTTONDOWN:
                self.mouse_pressed_keys = list(pg.mouse.get_pressed())
                self.mouse_held_keys = list(pg.mouse.get_pressed())

            if event.type == MOUSEBUTTONUP:
                self.mouse_released_keys = list(pg.mouse.get_pressed())
                self.mouse_held_keys = list(pg.mouse.get_pressed())
