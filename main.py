from core.common.names import *
import core.common.resources as cr

from core.event_holder import EventHolder

pg.init()
scale = 20
aspect_ratio = Vector2(9, 18)

cr.screen = pg.display.set_mode(
    (aspect_ratio.x * scale, aspect_ratio.y * scale), SCALED | FULLSCREEN
)

cr.event_holder = EventHolder()


while not cr.event_holder.should_quit:
    cr.screen.fill("white")
    cr.event_holder.get_events()
    pg.display.update()
