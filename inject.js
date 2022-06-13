// user info
username = 'ef5100126'
password = 'huo520123'
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


let path = document.location.pathname;

if (path.endsWith('/userPage/login')) {
    document.getElementById('input_idCardNo').value = username
    document.getElementById('input_pwd').value = password
}

if (path.endsWith('/passInfo/confirmOrder')) {
    document.getElementById('TencentCaptcha').click()
}