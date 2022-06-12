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

function handle(path) {
    document.getElementById('input_idCardNo').value = username
    document.getElementById('input_pwd').value = password
}


let path = document.location.pathname;

document.getElementById('TencentCaptcha').click()

if (path.endsWith('/passInfo/confirmOrder')) {
    window.callbackName1 = function (res) {
        if (res.ret === 0) {
            isCanSubmit = true;
            ticket = res.ticket;
            randstr = res.randstr;
            submitReservation(ticket, randstr)
            alert('提交了')
        }
    }
}

if (path.endsWith('/login')) {
    handle(document.location.pathname);
}

if (path.endsWith('/userPage/userCenter')) {

}