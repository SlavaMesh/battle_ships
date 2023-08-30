dot = Dot()
dot.set_dot(1, 1)
ship = Ship(dot.get_dot(), 3, horizontal=True)
board1.add_ship(ship.dots(), ship.get_specification())

dot = Dot()
dot.set_dot(1, 6)
ship = Ship(dot.get_dot(), 2, horizontal=False)
board1.add_ship(ship.dots(), ship.get_specification())

dot = Dot()
dot.set_dot(4, 4)
ship = Ship(dot.get_dot(), 2, horizontal=False)
board1.add_ship(ship.dots(), ship.get_specification())

dot = Dot()
dot.set_dot(6, 1)
ship = Ship(dot.get_dot(), 1, horizontal=False)
board1.add_ship(ship.dots(), ship.get_specification())

dot = Dot()
dot.set_dot(5, 3)
ship = Ship(dot.get_dot(), 1, horizontal=False)
board1.add_ship(ship.dots(), ship.get_specification())

dot = Dot()
dot.set_dot(3, 1)
ship = Ship(dot.get_dot(), 1, horizontal=False)
board1.add_ship(ship.dots(), ship.get_specification())

dot = Dot()
dot.set_dot(4, 6)
ship = Ship(dot.get_dot(), 1, horizontal=False)
board1.add_ship(ship.dots(), ship.get_specification())


for i in range(1, 7):
    for j in range(1, 7):
        board1.shot((i, j))
        Board.render_board(board1)
        print(f'ships_area: {board1.ships_area}')
        print(f'ships: {board1.ships}')
        print(f'ships_alive: {board1.ships_alive}')