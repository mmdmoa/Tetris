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
cr.event_holder.should_render_debug = True

rect = Rect(0, 0, 15, 15)
edges = [rect.copy() for i in range(4)]

edges[1].x = cr.screen.get_width() - edges[1].w
edges[2].x = cr.screen.get_width() - edges[2].w
edges[2].y = cr.screen.get_height() - edges[2].h
edges[3].y = cr.screen.get_height() - edges[3].h


while not cr.event_holder.should_quit:
    cr.screen.fill("gray")
    cr.event_holder.get_events()


    if cr.event_holder.should_render_debug:
        for rect in edges:
            pg.draw.rect(cr.screen,"black",rect,width=2)

    pg.display.update()
