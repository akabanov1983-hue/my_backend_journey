from app.info import get_health_payload, get_version_payload


def test_get_health_payload_returns_ok_dict():
    result = get_health_payload()
    assert result == {"status": "ok"}


def test_get_version_payload_returns_version_dict():
    result = get_version_payload("0.1.0")
    assert result == {"version": "0.1.0"}


def test_get_version_payload_uses_passed_argument():
    result = get_version_payload("1.2.3")
    assert result == {"version": "1.2.3"}