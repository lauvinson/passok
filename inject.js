// user info
username = 'ef5100126'
password = 'huo520123'
checkinDate = '2022-06-14'
t = '1655172000001'
s = 'bac2e56f23b3a2ce1b5cbd2941b015aa'
let path = document.location.pathname;
if (path.endsWith('/userPage/userCenter') || path.endsWith('/error/index')) {
    window.location.replace('https://hk.sz.gov.cn:8118/passInfo/confirmOrder?checkinDate=' + checkinDate + '&t=' + t + '&s=' + s)
}

Element.prototype.remove = function () {
    this.parentElement.removeChild(this);
}

NodeList.prototype.remove = HTMLCollection.prototype.remove = function () {
    for (let i = this.length - 1; i >= 0; i--) {
        if (this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}
document.getElementsByClassName("mask").remove()
document.getElementsByClassName("winpop").remove()

if (path.endsWith('/userPage/login')) {
    document.getElementById('input_idCardNo').value = username
    document.getElementById('input_pwd').value = password
}

if (path.endsWith('/passInfo/confirmOrder')) {
    document.getElementById('TencentCaptcha').click()
}