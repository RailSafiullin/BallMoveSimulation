import pytest
from Factory import Factory
from initWindow import InitWindow
from Storage import Storage
from ballMoveSimulation import BallMoveSimulation


@pytest.fixture(scope="module")
def app():
    app = Factory.create(InitWindow)
    yield app


@pytest.fixture(scope="module")
def storage():
    storage = Storage()
    yield storage


def test_storage_get_version(storage):
    result = storage.get_version()
    type(result) == str


def test_storage_get_help(storage):
    result = storage.get_help()
    type(result) == str


@pytest.fixture
def simulation():
    return BallMoveSimulation()

def test_init(simulation):
    assert simulation.WINDOW_WIDTH == 900
    assert simulation.WINDOW_HEIGHT == 600
    #assert simulation.ball_x == 450
    #assert simulation.ball_y == 20
    assert simulation.BALL_RADIUS == 20
    assert simulation.BALL_COLOR == (25, 25, 105)
    assert simulation.ball_vx == 0.0
    assert simulation.ball_vy == 0.0
    assert simulation.ball_ax == 0.0 
    assert simulation.ball_ay == 9.8 / simulation.clock_tick 
    assert simulation.k == 1.0
    assert simulation.clock_tick == 120
    assert simulation.escape_height == 10.0

def test_true_check_exit_condition(simulation):
    simulation.ball.y = 570
    simulation.ball.vy = -0.05
    simulation.ball.radius = 20
    simulation.escape_height = 10.0
    assert simulation.check_exit_condition() == True

def test_false_check_exit_condition(simulation):
    simulation.ball.y = 570
    simulation.ball.vy = -2.0
    simulation.ball.radius = 20
    simulation.escape_height = 10.0
    assert simulation.check_exit_condition() == False

def test_false2_check_exit_condition(simulation):
    simulation.ball.y = 500
    simulation.ball.vy = -0.05
    simulation.ball.radius = 20
    simulation.escape_height = 10.0
    assert simulation.check_exit_condition() == False