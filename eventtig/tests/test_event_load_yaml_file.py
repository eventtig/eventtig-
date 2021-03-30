from eventtig.event import Event


def test_start_1():
    event = Event()
    event.load_from_yaml_data(
        "id", {"start": "2021-01-03 07:08", "end": "2021-01-03 08:08"}
    )
    assert event.start_year == 2021
    assert event.start_month == 1
    assert event.start_day == 3
    assert event.start_hour == 7
    assert event.start_minute == 8


def test_start_no_padding_1():
    event = Event()
    event.load_from_yaml_data(
        "id", {"start": "2021-01-03 7:8", "end": "2021-01-03 8:8"}
    )
    assert event.start_year == 2021
    assert event.start_month == 1
    assert event.start_day == 3
    assert event.start_hour == 7
    assert event.start_minute == 8
