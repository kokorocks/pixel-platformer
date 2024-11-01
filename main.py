def on_overlap_tile(sprite, location):
    global Current_level
    Current_level += 1
    Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    Drop_fireball()
    pause(100)
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        myTile10
    """),
    on_overlap_tile2)

def Goto_checkpoint():
    tiles.place_on_random_tile(Character, assets.tile("""
        myTile13
    """))

def on_overlap_tile3(sprite3, location3):
    global Checkpoint
    Checkpoint = True
    Character.start_effect(effects.fountain, 500)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile13
    """),
    on_overlap_tile3)

def on_a_pressed():
    Jump(-150)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile4(sprite4, location4):
    pause(100)
    music.stop_all_sounds()
    info.change_life_by(-1)
    if Checkpoint:
        Goto_checkpoint()
    else:
        Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile4)

def Drop_fireball():
    if not (Buttontuched):
        pause(100)
        tiles.place_on_random_tile(Fire_ball, assets.tile("""
            myTile5
        """))
        Fire_ball.start_effect(effects.fire, 500000)
        if Current_level == 1 and not (Buttontuched):
            Fire_ball.ax = randint(-10, 10)
            Fire_ball.ay = 75
        else:
            Fire_ball.ax = randint(125, 325)
            Fire_ball.ay = 15

def on_overlap_tile5(sprite5, location5):
    global Buttontuched
    Buttontuched = True
    tiles.set_tile_at(location5, assets.tile("""
        transparency16
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile12
    """),
    on_overlap_tile5)

def on_left_pressed():
    Character.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f . . . . . 
                . . . . f 2 f e e e e f f . . . 
                . . . f 2 2 2 f e e e e f f . . 
                . . . f e e e e f f e e e f . . 
                . . f e 2 2 2 2 e e f f f f . . 
                . . f 2 e f f f f 2 2 2 e f . . 
                . . f f f e e e f f f f f f f . 
                . . f e e 4 4 f b e 4 4 e f f . 
                . . . f e d d f 1 4 d 4 e e f . 
                . . . . f d d d e e e e e f . . 
                . . . . f e 4 e d d 4 f . . . . 
                . . . . f 2 2 e d d e f . . . . 
                . . . f f 5 5 f e e f f f . . . 
                . . . f f f 9 f f f f 9 f . . . 
                . . . . 9 9 9 . . . 9 9 . . . .
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile6(sprite6, location6):
    pause(100)
    music.stop_all_sounds()
    info.change_life_by(-1)
    if Checkpoint:
        Goto_checkpoint()
    else:
        Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Wall fire
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite7, location7):
    global Current_level
    info.set_life(3)
    Current_level += 1
    Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile7)

def on_overlap_tile8(sprite8, location8):
    Drop_fireball()
    pause(100)
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        Wall fire
    """),
    on_overlap_tile8)

def Jump(Height: number):
    if Character.is_hitting_tile(CollisionDirection.BOTTOM):
        Character.vy = Height
        music.play(music.melody_playable(music.jump_up),
            music.PlaybackMode.UNTIL_DONE)

def on_right_pressed():
    Character.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f . . . . . 
                . . . f f e e e e f 2 f . . . . 
                . . f f e e e e f 2 2 2 f . . . 
                . . f e e e f f e e e e f . . . 
                . . f f f f e e 2 2 2 2 e f . . 
                . . f e 2 2 2 f f f f e 2 f . . 
                . f f f f f f f e e e f f f . . 
                . f f e 4 4 e b f 4 4 e e f . . 
                . f e e 4 d 4 1 f d d e f . . . 
                . . f e e e e e d d d f . . . . 
                . . . . f 4 d d e 4 e f . . . . 
                . . . . f e d d e 2 2 f . . . . 
                . . . f f f e e f 5 5 f f . . . 
                . . . f 9 f f f f 9 f f f . . . 
                . . . . 9 9 . . . 9 9 9 . . . .
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    Character.ay = -75
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def Level():
    global Buttontuched, Checkpoint
    if Current_level == 1:
        effects.blizzard.end_screen_effect()
        effects.clouds.start_screen_effect()
        scene.set_background_color(9)
        tiles.set_current_tilemap(tilemap("""
            level0
        """))
        tiles.place_on_random_tile(Character, assets.tile("""
            myTile0
        """))
        Buttontuched = False
        Checkpoint = False
    elif Current_level == 2:
        Character.ax = randint(-0.25, -7.5)
        effects.blizzard.start_screen_effect()
        scene.set_background_color(0)
        tiles.set_current_tilemap(tilemap("""
            Level2 mybiggestfan
        """))
        tiles.place_on_random_tile(Character, assets.tile("""
            myTile0
        """))
        Buttontuched = False
        Checkpoint = False
    else:
        game.game_over(True)

def on_overlap_tile9(sprite9, location9):
    global Current_level
    info.set_life(3)
    Current_level += 1
    Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile9)

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_overlap_tile10(sprite10, location10):
    pause(100)
    music.stop_all_sounds()
    info.change_life_by(-1)
    if Checkpoint:
        Goto_checkpoint()
    else:
        Level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile10
    """),
    on_overlap_tile10)

def on_overlap_tile11(sprite11, location11):
    Drop_fireball()
    pause(100)
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile11)

def on_on_overlap(sprite12, otherSprite):
    info.change_life_by(-1)
    sprites.destroy(Fire_ball, effects.rings, 5000000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

Buttontuched = False
Checkpoint = False
Current_level = 0
Character: Sprite = None
Fire_ball: Sprite = None
Fire_ball = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 2 2 2 5 2 2 2 . . . . . . 
            . . e 5 5 5 4 2 2 2 e . . . . . 
            . 2 5 5 5 5 4 2 2 2 2 2 . . . . 
            . 2 5 5 5 5 4 2 2 2 2 2 . . . . 
            . 2 5 5 5 5 4 2 2 2 2 2 . . . . 
            . 5 4 4 4 4 4 4 4 4 4 5 . . . . 
            . 2 2 2 2 2 4 5 5 5 5 2 . . . . 
            . 2 2 2 2 2 4 5 5 5 5 2 . . . . 
            . 2 2 2 2 2 4 5 5 5 5 2 . . . . 
            . . e 2 2 2 4 5 5 5 e . . . . . 
            . . . 2 2 2 5 2 2 2 . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
scene.set_background_color(0)
Character = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f . . . . . 
            . . . f f e e e e f 2 f . . . . 
            . . f f e e e e f 2 2 2 f . . . 
            . . f e e e f f e e e e f . . . 
            . . f f f f e e 2 2 2 2 e f . . 
            . . f e 2 2 2 f f f f e 2 f . . 
            . f f f f f f f e e e f f f . . 
            . f f e 4 4 e b f 4 4 e e f . . 
            . f e e 4 d 4 1 f d d e f . . . 
            . . f e e e e e d d d f . . . . 
            . . . . f 4 d d e 4 e f . . . . 
            . . . . f e d d e 2 2 f . . . . 
            . . . f f f e e f 5 5 f f . . . 
            . . . f 9 f f f f 9 f f f . . . 
            . . . . 9 9 . . . 9 9 9 . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Character, 79, 0)
scene.camera_follow_sprite(Character)
Current_level = 1
Level()
Drop_fireball()
music.play(music.string_playable("E G G F B A C5 B ", 120),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
Fire_ball.set_bounce_on_wall(True)
info.set_life(3)

def on_on_update():
    Character.set_bounce_on_wall(True)
    Character.ay = 500
    if Character.is_hitting_tile(CollisionDirection.BOTTOM) or Character.is_hitting_tile(CollisionDirection.TOP):
        Character.vy = 0
        Character.ay = 0
    game.set_game_over_effect(False, effects.melt)
game.on_update(on_on_update)

def on_on_update2():
    if Buttontuched:
        Character.ax = 0
game.on_update(on_on_update2)
