from producer_1 import get_data

def test_get_data_returns_dict():
    data = get_data()
    assert isinstance(data, dict)
    assert 'event_time' in data.keys()
    assert 'stock' in data.keys()
    assert 'price' in data.keys()