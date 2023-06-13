from leaf.repositories.users import get_user_by_email, get_active_user_by_email
from tests.factories.users import UserFactory
from leaf.models import User


def test_get_user_by_email(db):
    user = UserFactory.create()
    db_user = get_user_by_email(db, user.email)
    assert isinstance(db_user, User)
    assert db_user.id == user.id


def test_get_active_user_by_email_passed_case(db):
    user = UserFactory.create(disabled=False)
    db_user = get_active_user_by_email(db, user.email)
    assert isinstance(db_user, User)
    assert db_user.id == user.id


def test_get_active_user_by_email_not_passed_case(db):
    user = UserFactory.create(disabled=True)
    db_user = get_active_user_by_email(db, user.email)
    assert db_user is None


def test_create_one(db):
    create_one(db, email="create_one_test@test.com", hashed_password="test", first_name="test", last_name="test", disabled=True)
    db_user = get_user_by_email(db, email="create_one_test@test.com")
    assert db_user is not None
