from freezegun import freeze_time
from datetime import datetime, timezone

@freeze_time("2022-08-27 20:00:00", tz_offset=0)
def test_freeze_time():
    from functionality.zadania import calc_diff

    case = {
        "start_time": "2021-11-03T09:22:28+00:00",
        "end_time": None,  # None means that case is currently going on
    }
    assert datetime.now() == datetime(2022, 8, 27, 20, 0, 0)

    start_time_obj = datetime.fromisoformat("2021-11-03T09:22:28+00:00")
    timer = (datetime.now(timezone.utc) - start_time_obj).total_seconds()

    assert timer == calc_diff(case)