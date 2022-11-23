# coding: utf-8
# license: GPLv3

from solar_input import write_graph

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""
r = 0

def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """
    global r
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        if r == 0:
            continue
        body.Fx += ((-body.x + obj.x)*body.m*obj.m*gravitational_constant)/r**3
        body.Fy += ((-body.y + obj.y)*body.m*obj.m*gravitational_constant)/r**3


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.Vx += ax * dt
    body.x += dt*body.Vx

    ay = body.Fy / body.m
    body.Vy += ay * dt
    body.y += dt * body.Vy


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
        if body.type == "planet":
            write_graph(dt, r, body.Vx, body.Vy)
    for body in space_objects:
        move_space_object(body, dt)



if __name__ == "__main__":
    print("This module is not for direct call!")
