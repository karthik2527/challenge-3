from nested_dict_value_extractor import value_extractor


def test_nested_dict_value_extractor():
    assert value_extractor("c", {"a": {"b": {"c": "d"}}}) == "d"
    assert value_extractor("y", {"x": {"y": {"z": "a"}}}) == {"z": "a"}


def test_nested_dict_value_extractor_negative():
    assert value_extractor("a", {"a": {"b": {"c": "d"}}}) != "d"
