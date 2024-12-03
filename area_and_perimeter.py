from graphics import rect,circle
from graphics.threedgraphics import cuboid,sphere
length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))
radius=int(input("Enter the radius of the circle: "))
height=int(input("Enter the height of the cuboid: "))
area=rect.area(length,breadth)
perimeter=rect.perimeter(length,breadth)
cir_area=circle.cir_area(radius)
cir_perimeter=circle.circ_perimeter(radius)
cub_area=cuboid.area_cub(length,breadth,height)
cub_perimeter=cuboid.perimeter_cub(length,breadth,height)
sp_area=sphere.area_sp(radius)
sp_perimeter=sphere.peri_sp(radius)
