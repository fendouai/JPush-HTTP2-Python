import nose
from jpush import device
from jpush import common
import jpush as jpush


# please put your app_key and master_secret here
app_key = u'6be9204c30b9473e87bad4dc'
master_secret = u'e62664ad421b67270e5c9d5b'

_jpush = jpush.JPush(app_key, master_secret)
device = _jpush.create_device()
_jpush.set_logging("DEBUG")


def test_create_device():
    reg_id = '160a3797c80d93ce897'
    entity = jpush.device_tag(jpush.add("ddd", "tageee"))
    result = device.set_devicemobile(reg_id, entity)
    assert result.status_code==200


def test_aliasuser():
    alias = "alias1"
    platform = "android,ios"
    result = device.get_aliasuser(alias, platform)
    assert result.status_code == 200


def test_remove_alias():
    alias = "alias1"
    platform = "android,ios"
    result = device.delete_alias(alias, platform)
    assert result.status_code == 200


def test_remove_tags():
    tag = "ddd"
    platform = "android,ios"
    result = device.delete_tag(tag, platform)
    assert result.status_code == 200


def test_tag_exist():
    tag = "ddd"
    registration_id = '090c1f59f89'
    result = device.check_taguserexist(tag, registration_id)
    assert result.status_code == 200


def test_tag_list():
    result = device.get_taglist()
    assert result.status_code == 200


def test_update_tagusers():
    tag = "ddd"
    entity = jpush.device_regid(jpush.add("090c1f59f89"))
    result = device.update_tagusers(tag, entity)
    assert result.status_code == 200


def test_set_device_mobile():
    reg_id = '160a3797c80d93ce897'
    entity = jpush.device_tag(jpush.add("ddd", "tageee"))
    result = device.set_devicemobile(reg_id, entity)
    assert result.status_code == 200


def test_device_mobile():
    reg_id = '160a3797c80d93ce897'
    entity = jpush.device_mobile("18588232140")
    result = device.set_devicemobile(reg_id, entity)
    assert result.status_code == 200

if __name__ == '__main__':
    nose.runmodule()