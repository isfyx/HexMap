import numpy as np
import cairo

def inscribe_polygon(
    context : cairo.Context,
    sides   : int,
    radius  : float = 1,
    cx      : float = 0,
    cy      : float = 0,
    offset  : float = 0
) -> None :
    """
    Inscribes a regular polygon of the given number of sides, within a circle
    of the given radius, centered at (cx, cy), rotated counter clock-wise by
    the offset given in radians.

    Arguments:
        context (cairo.Context): The context in which to draw the polygon.
        sides   (int):           The number of sides.
        radius  (float):         The radius to inscribe. (default 1)
        cx      (float):         The center x-coordinate. (default 0)
        cy      (float):         The center y-coordinate. (default 0)
        offset  (float):         The offset to rotate the polygon by, given
                                 in radians. (default 0)
    """

    if (sides < 3):
        raise ValueError("Can't inscribe polygon with less than 3 sides.")

    x = cx + np.cos(offset) * radius
    y = cy - np.sin(offset) * radius

    context.move_to(x, y)

    theta = 2*np.pi/sides

    for i in range(sides):
        x = cx + np.cos((i+1) * theta + offset) * radius
        y = cy - np.sin((i+1) * theta + offset) * radius
        context.line_to(x, y)


def circumscribe_polygon(
    context : cairo.Context,
    sides   : int,
    radius  : float = 1,
    cx      : float = 0,
    cy      : float = 0,
    offset  : float = 0
) -> None :
    """
    Circumscribes a regular polygon of the given number of sides, along a
    circle of the given radius, centered at (cx, cy), rotated counter
    clock-wise by the offset given in radians.

    Arguments:
        context (cairo.Context): The context in which to draw the polygon.
        sides   (int):           The number of sides.
        radius  (float):         The radius to circumscribe. (default 1)
        cx      (float):         The center x-coordinate. (default 0)
        cy      (float):         The center y-coordinate. (default 0)
        offset  (float):         The offset to rotate the polygon by, given
                                 in radians. (default 0)
    """

    theta   = np.pi/sides
    tan     = np.tan(theta)
    cos     = np.cos(theta)
    radius *= cos + cos * tan*tan

    return inscribe_polygon(context, sides, radius, cx, cy, offset)