import authenticator
import pytest

def test_register():
    obj = authenticator.Authenticator()
    obj.register("user", "pass")
    assert obj.users["user"] == "pass"


def test_register_duplicate():
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        obj = authenticator.Authenticator()
        obj.register("user", "pass")
        obj.register("user", "pass")

def test_login():
    obj = authenticator.Authenticator()
    obj.register("user", "pass")
    result = obj.login("user", "pass")
    assert result == "ログイン成功"

def test_login_fail():
    obj = authenticator.Authenticator()
    obj.register("user", "pass")
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        result = obj.login("user", "wrong")
