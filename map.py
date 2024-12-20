# Coordinates: (x, y)

grid_size = 24


IntersectionPoints = {
    # OUTER BOUNDS
    # Start Row 0
    (0, 0): {(15, 0): 15, (23, 0): 23},
    # Start Row 1
    (1, 1): {(14, 1): 13, (22, 1): 21},
    # Start Col 0
    (0, 23): {(0, 8): 15, (0, 0): 23},
    # Start Col 1
    (1, 22): {(1, 9): 13, (1, 1): 21},
    # Start Row 22
    (22, 22): {(13, 22): 9, (1, 22): 21},
    # Start Row 23
    (23, 23): {(12, 23): 11, (0, 23): 23},
    # Start Col 22
    (22, 1): {(22, 10): 9, (22, 22): 21, (22, 16): 15},
    # Start Col 23
    (23, 0): {(23, 11): 11, (23, 23): 23, (23, 17): 17},

    # ROW 16 & 17 STREET
    # Left Street
    (12, 17): {(6, 17): 6, (8, 17): 4, (12, 1): 16},
    (13, 17): {(6, 17) : 5, (13, 11): 6},
    # Options in Col 0 & 1
    (0, 17): {(0, 8): 9, (0, 0): 17, (0, 6): 11},
    (1, 16): {(1, 9): 7, (1, 1): 15, (1, 6): 10},
    # Right Street
    (14, 17): {(22, 17) : 6},
    (15, 16): {(23, 16) : 7},
    # Options in Col 22 & 23
    (22, 17): {(22, 22): 5},
    (23, 16): {(23, 23): 7},

    # ROW 8-11 STREET
    # Upper Left Street
    (12, 11) : {(6, 11): 6, (0, 11): 12, (12, 10): 1},
    (12, 10) : {(5, 10): 7, (1, 10): 11, (12, 9): 1},
    # Options in Col 0 & 1
    (0, 11): {(0, 8): 3, (0, 0): 11, (0, 6): 5},
    (1, 10): {(1, 9): 1, (1, 1): 4, (1, 6): 9},
    # Lower Left Street
    (0, 8): {(6, 8): 6, (12, 8): 12},
    (1, 9): {(7, 9): 6, (12, 9): 11},
    #ROUNDABOUT OPTIONS OF STREET
    (12, 9): {(12, 8): 1},
    # Upper Right Street
    (22, 10) : {(18, 10): 4, (15, 10): 7},
    (23, 11) : {(19, 11): 4, (15, 11): 8},
    # ROUNDABOUT OPTIONS OF STREET
    (15, 10): {(15, 11): 1},
    (15, 11): {(15, 23): 12, (14, 11): 1},
    # Lower Right Street
    (15, 9): {(22, 9): 7, (15, 10): 1},
    (15, 8): {(23, 8): 8, (15, 9): 1},
    # Options in Col 22 & 23
    (23, 8): {(23, 11): 3, (23, 23): 15, (23, 14): 6},
    (22, 9): {(22, 10): 1, (22, 22): 13, (22, 14): 5},

    # COL 12-15 STREET
    # Left Street
    (12, 23): {(12, 19): 4, (12, 17): 6, (12, 13): 10, (12, 11): 12},
    (13, 22): {(13, 19): 3, (13, 16): 6, (13, 13): 9, (13, 11): 11},
    # Roundabout Options
    (13, 11): {(12, 11): 1},
    # Right Street
    (14, 11): {(14, 13): 2, (14,17): 6, (14, 22): 11, (13, 11) : 1},
    (15, 11): {(15, 13): 2, (15,16): 5, (15, 23): 12, (14, 11): 1},
    # Options in Row 22 & 23
    (14, 22): {(13, 22): 1, (1, 22): 13, (9, 22): 5},
    (15, 23): {(12, 23): 3, (0, 23): 15, (9, 23): 6},

    # COL 5 & 6 STREET
    (5, 10): {(5, 13): 3, (5, 16): 6},
    (6, 11): {(6, 13): 2, (6, 17): 6},
    # Options in Col 0 & 1
    (5, 16): {(1, 16) : 4},

    # COL 6 & 7 STREET
    (6, 8): {(6, 3) : 5, (6, 0): 8},
    (7, 9): {(7, 3): 6, (7, 1): 8},
    # Options in Row 0 & 1
    (6, 0): {(15, 0): 9, (23, 0): 17},
    (7, 1): {(14, 1): 7, (22, 1): 15},

    # COL 12 & 13 LOWER STREET
    (12, 8): {(12, 0): 8, (13, 8): 1},
    (13, 8): {(13, 1): 7, (14, 8): 1},
    # Options in Row 0 & 1
    (12, 0): {(15, 0): 3, (23, 0): 11},
    (13, 1): {(14, 1): 1, (22, 1): 9},

    # COL 14 & 15 LOWER STREET
    (14, 1): {(14, 8): 7},
    (15, 0): {(15, 8): 8},
    # ROUNDABOUT OPTIONS OF STREET
    (14, 8): {(15, 8): 1},


    # ROW 4 & 5 STREET
    (22, 4): {(19, 4): 3, (17, 4): 5, (14, 4): 8},
    (23, 5): {(19, 5): 4, (17, 5): 6, (15, 5): 8},
    # Options in Col 14 & 15
    (14, 4): {(14, 8): 4},
    (15, 5): {(15, 8): 3},

    # COL 18 & 19  STREET
    # Upper Street
    (18, 23): {(18, 20): 3, (18, 19):4, (18, 16): 7},
    (19, 22): {(19, 20): 2, (19, 19):3, (19, 17): 5},
    # Lower Street
    (19, 11): {(19, 16): 5},
    (18, 10): {(18, 17): 7},
    # Options for Both Streets
    (18, 16): {(23, 16): 5},
    (18, 17): {(22, 17): 4},
    (19, 16): {(23, 16): 4},
    (19, 17): {(22, 17): 3},

    # REACHES PARKING LOTS
    # PL 1
    (1, 14): {(1, 22): 22, (2, 14): 1},
    (0, 14): {(0, 23): 23, (0, 14): 2},
    # PL 2
    (3, 23): {(3, 21): 2, (23, 23): 20},
    (3, 22): {(3, 21): 1, (22, 22): 22},
    # PL 3
    (3, 5): {(3, 6): 1, (6, 5): 3},
    (3, 4): {(3, 6): 2, (6, 4): 3},
    # PL 4
    (4, 11): {(4, 12): 1, (6, 11): 2, (13, 11): 7, (16, 11): 12},
    (4, 10): {(4, 12): 2, (6, 10): 2, (13, 10): 7, (16, 11): 2},
    # PL 5
    (4, 5): {(4, 3): 2, (6, 5): 2},
    (4, 4): {(4, 3): 1, (6, 4): 2},
    # PL 6
    (6, 17): {(5, 17): 1, (6, 11): 6},
    (7, 17): {(5, 17): 2, (7, 11): 6 },
    # PL 7
    (7, 15): {(8, 15): 1, (7, 11): 4},
    (6, 15): {(8, 15): 2, (6, 11): 4},
    # PL 8
    (9, 1): {(9, 2): 1, (0, 1): 9},
    (9, 0): {(9, 2): 2, (0, 0): 9},
    # PL 9
    (10, 17): {(10, 19): 2, (5, 16): 3},
    (10, 18): {(10, 19): 1, (6, 17): 4},
    # PL 10
    (10, 11): {(10, 12): 1, (12, 11): 2},
    (10, 10): {(10, 12): 2, (13, 11): 2},
    # PL 11
    (10, 9): {(10, 9): 2, (15,16): 3, (15, 23): 10},
    (10, 8): {(10, 7): 1, (14,17): 4, (14, 22): 9},
    # PL 12
    (17, 22): {(17, 21): 1, (23, 22): 6},
    (17, 23): {(17, 21): 2, (23, 23): 6},
    # PL 13
    (18, 6): {(17, 6): 1, (18, 1) : 5},
    (19, 6): {(17, 6): 2, (19, 1) : 5},
    # PL 14 
    (18, 4): {(17, 4): 1, (18, 1): 3},
    (19, 4): {(17, 4): 2, (19, 1): 3},
    # PL 15 & 16
    (20, 17): {(20, 18): 1, (22, 17): 2},
    (20, 16): {(20, 15): 2, (22, 16): 2},
    #PL 17
    (18, 4): {(20, 4): 2, (18, 1): 3},
    (19, 4): {(20, 4): 1, (19, 1): 1},

    # Emerges From Parking Lots
    (2, 14): {(1, 14): 1, (0, 14): 2},      #P1
    (3, 21): {(3, 23): 2, (3, 22): 1},      #P2
    (3, 6): {(3, 5): 1, (3, 4): 2},         #P3
    (4, 12): {(4, 11): 1, (4, 10): 2},      #P4
    (4, 3): {(4, 5): 1, (4, 4): 2},         #P5
    (5, 17): {(6, 17): 1, (7, 17): 2},      #P6
    (8, 15): {(7, 15): 1, (6, 15): 2},      #P7
    (9, 2): {(9, 1): 1, (9, 0): 2},         #P8
    (10, 19): {(10, 17): 2, (10, 18): 1},   #P9
    (10, 12): {(10, 11): 1, (10, 10): 2},   #P10
    (10, 7): {(10, 9): 2, (10, 8): 1},      #P11
    (17, 21): {(17, 22): 1, (17, 23): 2},   #P12
    (17, 6): {(18, 6): 1, (19, 6): 2},      #P13
    (17, 4): {(18, 4): 1, (19, 4): 2},      #P14
    (20, 18): {(20, 17): 1, (20, 16): 2},   #P15
    (20, 15): {(20, 17): 2, (20, 16): 1},   #P16
    (20, 4): {(18, 4): 2, (19, 4): 1},      #P17
}

# Parking lots
Parkings = [(2, 14), #P1,
            (3, 21), #P2
            (3, 6),  #P3
            (4, 12), #P4            
            (4, 3),  #P5
            (5, 17), #P6
            (8, 15), #P7
            (9, 2),  #P8
            (10, 19),#P9
            (10, 12),#P10 
            (10, 7), #P11
            (17, 21),#P12
            (17, 6), #P13
            (17, 4), #P14
            (20, 18),#P15
            (20, 15),#P16 
            (20, 4)  #P17
            ] 

# Buildings
Buildings = [((2, 21), '#3b0504'), ((4, 21), '#3b0504'), ((5, 21), '#3b0504'), ((8, 21), '#3b0504'), ((9, 21), '#3b0504'), ((10, 21), '#3b0504'), ((11, 21), '#3b0504'), ((16, 21), '#3b0504'),  ((18, 21), '#3b0504'), ((19, 21), '#3b0504'), ((20, 21), '#3b0504'), ((21, 21), '#3b0504'),                                                            # y:21 row
             ((2, 20), '#3b0504'), ((3, 20), '#3b0504'), ((4, 20), '#3b0504'), ((5, 20), '#3b0504'), ((8, 20), '#3b0504'), ((9, 20), '#3b0504'), ((10, 20), '#3b0504'), ((11, 20), '#3b0504'), ((16, 20), '#3b0504'), ((17, 20), '#3b0504'), ((18, 20), '#3b0504'), ((19, 20), '#3b0504'), ((20, 20), '#3b0504'), ((21, 20), '#3b0504'),                # y:20 row
             ((2, 19), '#3b0504'), ((3, 19), '#3b0504'), ((4, 19), '#3b0504'), ((5, 19), '#3b0504'), ((8, 19), '#3b0504'), ((9, 19), '#3b0504'), ((11, 19), '#3b0504'), ((16, 19), '#3b0504'), ((17, 19), '#3b0504'), ((18, 19), '#3b0504'), ((19, 19), '#3b0504'), ((20, 19), '#3b0504'), ((21, 19), '#3b0504'),                                       # y:19 row
             ((2, 18), '#3b0504'), ((3, 18), '#3b0504'), ((4, 18), '#3b0504'), ((5, 18), '#3b0504'), ((16, 18), '#3b0504'), ((17, 18), '#3b0504'), ((18, 18), '#3b0504'), ((19, 18), '#3b0504'), ((21, 18), '#3b0504'),                                                                                                                                 # y:18 row
             ((2, 17), '#3b0504'), ((3, 17), '#3b0504'), ((4, 17), '#3b0504'), ((2, 17), '#3b0504'), ((3, 17), '#3b0504'), ((4, 17), '#3b0504'), 
             ((2, 16), '#3b0504'), ((3, 16), '#3b0504'), ((4, 16), '#3b0504'), ((5, 16), '#3b0504'), ((8, 16), '#3b0504'), ((9, 16), '#3b0504'),  ((10, 16), '#3b0504'),  ((11, 16), '#3b0504'),                                                                                                                                                        # y:17 row
             ((2, 15), '#3b0504'), ((3, 15), '#3b0504'), ((4, 15), '#3b0504'), ((5, 15), '#3b0504'), ((9, 15), '#3b0504'), ((10, 15), '#3b0504'), ((11, 15), '#3b0504'), ((16, 15), '#3b0504'), ((17, 15), '#3b0504'), ((18, 15), '#3b0504'), ((19, 15), '#3b0504'), ((21, 15), '#3b0504'),                                                            # y:15 row
             ((3, 14), '#3b0504'), ((4, 14), '#3b0504'), ((5, 14), '#3b0504'), ((8, 14), '#3b0504'), ((9, 14), '#3b0504'), ((10, 14), '#3b0504'), ((11, 14), '#3b0504'), ((16, 14), '#3b0504'), ((17, 14), '#3b0504'), ((18, 14), '#3b0504'),  ((19, 14), '#3b0504'),((20, 14), '#3b0504'), ((21, 14), '#3b0504'),                                     # y:14 row
             ((2, 13), '#3b0504'), ((3, 13), '#3b0504'), ((4, 13), '#3b0504'), ((5, 13), '#3b0504'), ((8, 13), '#3b0504'), ((9, 13), '#3b0504'), ((10, 13), '#3b0504'), ((11, 13), '#3b0504'), ((16, 13), '#3b0504'), ((17, 13), '#3b0504'), ((18, 13), '#3b0504'), ((19, 13), '#3b0504'), ((20, 13), '#3b0504'), ((21, 13), '#3b0504'),                                                                                                          # y:13 row
             ((2, 12), '#3b0504'), ((3, 12), '#3b0504'), ((5, 12), '#3b0504'), ((8, 12), '#3b0504'), ((9, 12), '#3b0504'), ((11, 12), '#3b0504'), ((16, 12), '#3b0504'), ((17, 12), '#3b0504'), ((18, 12), '#3b0504'), ((19, 12), '#3b0504'), ((20, 12), '#3b0504'), ((21, 12), '#3b0504'),                                                             # y:12 row                                                                                                                                                                                                                                                      # y:9 row
             ((2, 7), '#3b0504'), ((3, 7), '#3b0504'), ((4, 7), '#3b0504'), ((5, 7), '#3b0504'), ((8, 7), '#3b0504'), ((9, 7), '#3b0504'), ((11, 7), '#3b0504'), ((16, 7), '#3b0504'), ((17, 7), '#3b0504'),((20, 7), '#3b0504'), ((21, 7), '#3b0504'),
             ((2, 6), '#3b0504'), ((4, 6), '#3b0504'), ((5, 6), '#3b0504'), ((8, 6), '#3b0504'), ((9, 6), '#3b0504'), ((10, 6), '#3b0504'), ((11, 6), '#3b0504'), ((16, 6), '#3b0504'), ((20, 6), '#3b0504'), ((21, 6), '#3b0504'),
             ((16, 5), '#3b0504'), ((17, 5), '#3b0504'), ((20, 5), '#3b0504'), ((21, 5), '#3b0504'),
             ((16, 4), '#3b0504'), ((21, 4), '#3b0504'),
             ((2, 3), '#3b0504'), ((3, 3), '#3b0504'), ((5, 3), '#3b0504'), ((8, 3), '#3b0504'), ((9, 3), '#3b0504'), ((10, 3), '#3b0504'), ((11, 3), '#3b0504'), ((16, 3), '#3b0504'), ((17, 3), '#3b0504'), ((20, 3), '#3b0504'), ((21, 3), '#3b0504'),
             ((2, 2), '#3b0504'), ((3, 2), '#3b0504'), ((4, 2), '#3b0504'), ((5, 2), '#3b0504'), ((8, 2), '#3b0504'), ((10, 2), '#3b0504'), ((11, 2), '#3b0504'), ((16, 2), '#3b0504'), ((17, 2), '#3b0504'), ((20, 2), '#3b0504'), ((21, 2), '#3b0504'),
             ((13, 10), '#c9a40c'), ((14, 10), '#c9a40c'),  # ROTONDA                                                                                                                                                                                                                                                                                  # y:10 row
             ((13, 9), '#c9a40c'), ((14, 9), '#c9a40c'),    #ROTONDA
             #((18, 4), '#ed61ae'), #prueba
             #((18, 16), '#ad61ae'), #prueba
            
            ]
# Semaphores
Semaphores = [((6, 21), 'green'), ((7, 21), 'green'), ((8, 23), 'red'), ((8, 22), 'red'), ((8, 18), 'red'), ((8, 17), 'red'), ((6, 16), 'green'),
               ((7, 16), 'green'), ((17, 8), 'red'), ((17, 9), 'red'), ((0, 6), 'green'), ((1, 6), 'green'), 
               ((5, 0), 'red'), ((5, 1), 'red'), ((18, 7), "green"), ((19, 7), "green"), 
               ((6, 2), "green"), ((7, 2), "green"), ((2, 4), "red"), ((2, 5), "red") ]