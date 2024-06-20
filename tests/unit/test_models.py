"""This module is for testing model purpose."""

def test_new_owner(new_owner):
    """
    GIVEN an Owner model
    WHEN a new Owner is created
    THEN check the fields are defined correctly
    """
    assert new_owner.name == 'John De'
    assert new_owner.address == '123 Main St'
    assert new_owner.city == 'Somewhere'
    assert new_owner.telephone == '126543651423'
