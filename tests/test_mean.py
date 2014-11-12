from mean import main

def test_mean2():
    assert int(main.avg(range(11))) == 5
